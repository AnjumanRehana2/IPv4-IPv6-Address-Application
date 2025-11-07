import requests
import json

BASE_URL = "http://127.0.0.1:5050"  

def print_menu():
    print("\n==============================")
    print("   IP Converter & Validator   ")
    print("==============================")
    print("1. Validate IP")
    print("2. Convert IP (IPv4 ↔ IPv6)")
    print("3. Geolocate IP")
    print("4. Exit")
    print("==============================")

def validate_ip():
    ip = input("Enter an IP address: ").strip()
    response = requests.post(f"{BASE_URL}/validate", json={"ip": ip})
    if response.status_code == 200:
        data = response.json()
        print(f"\n✅ IP Validation Result:")
        print(f"Input: {data['input']}")
        print(f"Valid: {data['valid']}")
        print(f"Version: {data['version']}")
    else:
        print("Error: Could not validate IP.")

def convert_ip():
    ip = input("Enter an IP address: ").strip()
    response = requests.post(f"{BASE_URL}/convert", json={"ip": ip})
    data = response.json()
    if response.status_code == 200:
        print("\n🔁 Conversion Result:")
        print(json.dumps(data, indent=4))
    else:
        print(f"Error: {data.get('error', 'Conversion failed')}")

def geolocate_ip():
    ip = input("Enter an IP address: ").strip()
    response = requests.post(f"{BASE_URL}/geolocate", json={"ip": ip})
    data = response.json()
    if response.status_code == 200:
        print("\n🌍 Geolocation Info:")
        print(json.dumps(data, indent=4))
    else:
        print(f"Error: {data.get('error', 'Lookup failed')}")

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            validate_ip()
        elif choice == "2":
            convert_ip()
        elif choice == "3":
            geolocate_ip()
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Connecting to Flask API...")
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("Connected successfully!")
            main()
        else:
            print("Flask API not responding properly.")
    except requests.exceptions.ConnectionError:
        print("Unable to connect to Flask backend. Make sure it's running!")
