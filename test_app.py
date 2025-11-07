import json
from backend.app import app

# Use Flask’s built-in test client
def test_validate_ipv4():
    client = app.test_client()
    response = client.post("/validate", json={"ip": "8.8.8.8"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["valid"] is True
    assert data["version"] == "IPv4"

def test_validate_ipv6():
    client = app.test_client()
    response = client.post("/validate", json={"ip": "2606:4700:4700::1111"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["valid"] is True
    assert data["version"] == "IPv6"

def test_convert_ipv4_to_ipv6():
    client = app.test_client()
    response = client.post("/convert", json={"ip": "139.130.4.5"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "result" in data

def test_invalid_ip():
    client = app.test_client()
    response = client.post("/validate", json={"ip": "999.999.999.999"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["valid"] is False
