const BASE_URL = "http://127.0.0.1:5050";

//just uncomment line number 4 to user deployed server
//const BASE_URL = "https://ipv4-ipv6-address-application-1.onrender.com "
const resultBox = document.getElementById("resultBox");

document.getElementById("validateBtn").addEventListener("click", () => handleAction("/validate"));
document.getElementById("convertBtn").addEventListener("click", () => handleAction("/convert"));
document.getElementById("geoBtn").addEventListener("click", () => handleAction("/geolocate"));

async function handleAction(endpoint) {
  const ip = document.getElementById("ipInput").value.trim();
  if (!ip) {
    showResult({ error: "Please enter an IP address first." });
    return;
  }

  try {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ip }),
    });

    const data = await response.json();
    showResult(data);
  } catch (error) {
    showResult({ error: "Connection error. Please check backend." });
  }
}

function showResult(data) {
  resultBox.innerHTML = `<pre class="json-output">${syntaxHighlight(data)}</pre>`;
}

// Adds color highlighting for JSON
function syntaxHighlight(json) {
  if (typeof json != "string") json = JSON.stringify(json, undefined, 4);
  json = json.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  return json.replace(
    /("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|\b[0-9.]+\b)/g,
    match => {
      let cls = "number";
      if (/^"/.test(match)) {
        cls = /:$/.test(match) ? "key" : "string";
      } else if (/true|false/.test(match)) {
        cls = "boolean";
      } else if (/null/.test(match)) {
        cls = "null";
      }
      return `<span class="${cls}">${match}</span>`;
    }
  );
}
