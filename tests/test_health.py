import os
import requests

def test_health_endpoint():
    base_url = os.getenv("BASE_URL", "http://localhost:8080")
    r = requests.get(f"{base_url}/health", timeout=10)
    assert r.status_code == 200
print("QA Pipeline Trigger Test")

def test_health_response_body():
    import os
    import requests

    base_url = os.getenv("BASE_URL", "http://localhost:8080")
    r = requests.get(f"{base_url}/health")

    data = r.json()
    assert data["status"] == "UP"
