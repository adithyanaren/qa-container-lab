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

def test_health_response_time():
    import os
    import requests
    import time

    base_url = os.getenv("BASE_URL", "http://localhost:8080")

    start = time.time()
    r = requests.get(f"{base_url}/health")
    end = time.time()

    response_time = end - start
    assert response_time < 1
