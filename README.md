# IPv4 ↔ IPv6 Utility App

A modern, full-stack application to validate, convert, and geolocate IPv4 and IPv6 addresses. Built with Python (Flask) backend, HTML/CSS/JS frontend, and automated testing & CI using pytest and GitHub Actions.

## Features

* Validate IPv4 and IPv6 addresses
* Convert between IPv4 ↔ IPv6 formats
* Geolocate IP addresses (country, city, ISP, timezone)
* CLI frontend for terminal testing
* Modern web frontend with responsive dark-glass UI
* Automated backend tests with `pytest`
* Continuous Integration (CI) using GitHub Actions

## Team Roles

| Member | Role | Responsibilities |
|--------|------|------------------|
| Member 1 | Project Manager / Research Lead | Coordinates team, manages timeline, researches IP standards. |
| Member 2 | Backend Developer | Implements IP validation, conversion, and geolocation endpoints. |
| Member 3 | Frontend Developer / UI Designer | Designs CLI & web UI for easy interaction with backend. |
| Member 4 | Tester / DevOps Engineer | Writes automated tests, sets up CI/CD, manages deployment. |

## Tech Stack

* **Backend:** Python 3, Flask, Flask-CORS, Requests
* **Frontend:** HTML, CSS, JavaScript
* **Testing:** Pytest
* **Automation:** GitHub Actions (CI)
* **Version Control:** Git / GitHub

## Setup & Installation

### Clone the repository
```bash
git clone https://github.com/<AnjumanRehana2>/<IPv4-IPv6-Address-Application>.git
cd <IPv4-IPv6-Address-Application>
```

### Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the Flask backend
```bash
python3 app.py
```

* Flask backend runs on `http://127.0.0.1:5050`
* CORS is enabled for web frontend

### Run CLI frontend (optional)
```bash
python3 cli_app.py
```

### Run Web Frontend

* Open `index.html` in your browser
* Enter any IPv4 or IPv6 address and test Validate / Convert / Geolocate

## Running Tests
```bash
pytest -v
```

* Validates your endpoints automatically
* Tests IPv4, IPv6, conversion, and invalid IP handling

## GitHub Actions CI

* Runs all tests automatically on push or pull request to `main` branch
* Ensures code quality and prevents breaking changes

## Example Test IPs

| Type | IP | Notes |
|------|-----|-------|
| IPv4 | 8.8.8.8 | Google DNS |
| IPv4 | 139.130.4.5 | Australia (Telstra) |
| IPv4 | 103.233.58.1 | Nepal Telecom |
| IPv6 | 2606:4700:4700::1111 | Cloudflare |
| IPv6 | 2405:200:8000::1 | Nepal Telecom |


## Folder Structure
```
project/
│
├─ app.py              # Flask backend
├─ cli_app.py          # CLI frontend
├─ index.html          # Web frontend
├─ style.css           # Web frontend CSS
├─ app.js              # Web frontend JS
├─ requirements.txt    # Python dependencies
├─ test_app.py         # Automated tests
└─ .github/
    └─ workflows/
        └─ ci.yml      # GitHub Actions workflow
```

## Notes

* Make sure the Flask backend is running before opening the web frontend.
* All results are JSON formatted and syntax-highlighted in the web UI.
* CI/CD ensures that new changes won't break the application.

## References

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Flask-CORS](https://flask-cors.readthedocs.io/)
* [GitHub Actions](https://docs.github.com/en/actions)
* [IP API](https://ip-api.com/)
