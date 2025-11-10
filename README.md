# IPv4 ↔ IPv6 Utility App

A simple, full-stack application to validate, convert, and geolocate IPv4 and IPv6 addresses. Backend is built with Python (Flask), and the app is now fully containerized with Docker for easy team testing and deployment.

## Features

* Validate IPv4 and IPv6 addresses
* Convert between IPv4 ↔ IPv6 formats
* Geolocate IP addresses (country, city, ISP, timezone)
* Modern web frontend (HTML/CSS/JS)
* CLI frontend for terminal testing
* Automated backend tests with `pytest`
* Continuous Integration (CI) using GitHub Actions

## Quick Start (Docker)

**Recommended for all team members!**

1. **Build the Docker image:**
   ```sh
   docker build -t ipv4-ipv6-app .
   ```
2. **Run the app in a container:**
   ```sh
   docker run -p 5050:5050 ipv4-ipv6-app
   ```
3. **Test the API:**
   - Visit [http://localhost:5050](http://localhost:5050) in your browser or use Postman/curl to test endpoints.
   - Open `index.html` in your browser for the web UI.

## Manual Setup (for development)

1. **Clone the repository:**
   ```sh
   git clone https://github.com/<AnjumanRehana2>/<IPv4-IPv6-Address-Application>.git
   cd <IPv4-IPv6-Address-Application>
   ```
2. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```
3. **Install dependencies:**
   ```sh
   pip install -r backend/requirements.txt
   ```
4. **Run the backend (dev only):**
   ```sh
   python3 backend/app.py
   ```
   * Flask backend runs on `http://127.0.0.1:5050`

## Running Tests

```sh
pytest -v
```

* Validates endpoints for IPv4, IPv6, conversion, and invalid IPs

## Folder Structure
```
project/
│
├─ backend/
│   ├─ app.py            # Flask backend
│   ├─ requirements.txt  # Python dependencies
│   └─ ...
├─ index.html            # Web frontend
├─ style.css             # Web frontend CSS
├─ app.js                # Web frontend JS
├─ Dockerfile            # Containerization
├─ test_app.py           # Automated tests
└─ .github/
    └─ workflows/
        └─ ci.yml        # GitHub Actions workflow
```

## Notes

* Use Docker for easiest setup and consistent results.
* Make sure the backend is running before opening the web frontend.
* All API results are JSON formatted.
* CI/CD ensures new changes are tested automatically.

## Example Test IPs

| Type | IP | Notes |
|------|-----|-------|
| IPv4 | 8.8.8.8 | Google DNS |
| IPv4 | 139.130.4.5 | Australia (Telstra) |
| IPv4 | 103.233.58.1 | Nepal Telecom |
| IPv6 | 2606:4700:4700::1111 | Cloudflare |
| IPv6 | 2405:200:8000::1 | Nepal Telecom |

## References

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Flask-CORS](https://flask-cors.readthedocs.io/)
* [GitHub Actions](https://docs.github.com/en/actions)
* [IP API](https://ip-api.com/)
