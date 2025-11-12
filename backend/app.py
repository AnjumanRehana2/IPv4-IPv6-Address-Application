from flask import Flask, request, jsonify
import ipaddress
import requests 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def ipv4_to_ipv6(ipv4_addr):
    """Convert IPv4 to IPv6-mapped address."""
    try:
        ipv4 = ipaddress.IPv4Address(ipv4_addr)
        ipv6_mapped = ipaddress.IPv6Address('::ffff:' + str(ipv4))
        return str(ipv6_mapped)
    except Exception:
        return None

def ipv6_to_ipv4(ipv6_addr):
    """Convert IPv6-mapped address to IPv4 (if possible)."""
    try:
        ipv6 = ipaddress.IPv6Address(ipv6_addr)
        if ipv6.ipv4_mapped:
            return str(ipv6.ipv4_mapped)
        else:
            return None
    except Exception:
        return None

def validate_ip(ip):
    """Check if given IP is valid and return version."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        return {"valid": True, "version": ip_obj.version}
    except ValueError:
        return {"valid": False, "version": None}

@app.route('/')
def home():
    return jsonify({"message": "IPv4–IPv6 Conversion API is running!"})

@app.route('/validate', methods=['POST'])
def validate():
    """Validate if IP is valid and identify its version."""
    data = request.get_json()
    ip = data.get('ip', '')
    result = validate_ip(ip)
    # Map version number to string for API response
    version_str = None
    if result["version"] == 4:
        version_str = "IPv4"
    elif result["version"] == 6:
        version_str = "IPv6"
    return jsonify({"input": ip, "valid": result["valid"], "version": version_str})

@app.route('/convert', methods=['POST'])
def convert():
    """Convert between IPv4 and IPv6 (mapped) if possible."""
    data = request.get_json()
    ip = data.get('ip', '')

    result = validate_ip(ip)
    if not result["valid"]:
        return jsonify({"error": "Invalid IP address"}), 400

    if result["version"] == 4:
        converted = ipv4_to_ipv6(ip)
        return jsonify({
            "input": ip,
            "type": "IPv4",
            "converted_to": "IPv6-mapped",
            "result": converted
        })
    elif result["version"] == 6:
        converted = ipv6_to_ipv4(ip)
        if converted:
            return jsonify({
                "input": ip,
                "type": "IPv6-mapped",
                "converted_to": "IPv4",
                "result": converted
            })
        else:
            return jsonify({
                "input": ip,
                "type": "IPv6 (non-mapped)",
                "message": "This IPv6 address cannot be converted to IPv4"
            })
    else:
        return jsonify({"error": "Unknown IP type"}), 400


#geolocatien endpoint
@app.route('/geolocate', methods=['POST'])
def geolocate():
    """Fetch geolocation info for an IP using ip-api.com."""
    data = request.get_json()
    ip = data.get("ip", "").strip()

    # Validate IP before lookup
    valid_check = validate_ip(ip)
    if not valid_check["valid"]:
        return jsonify({"error": "Invalid IP address"}), 400

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        info = response.json()

        if info.get("status") == "fail":
            return jsonify({"error": info.get("message", "Lookup failed")}), 400

        result = {
            "ip": info.get("query"),
            "country": info.get("country"),
            "region": info.get("regionName"),
            "city": info.get("city"),
            "isp": info.get("isp"),
            "timezone": info.get("timezone"),
            "lat": info.get("lat"),
            "lon": info.get("lon"),
        }

        return jsonify(result)

    except requests.RequestException as e:
        return jsonify({"error": f"Request failed: {str(e)}"}), 500


# Comment out the Flask development server run block for production Docker usage
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5050, debug=True)
