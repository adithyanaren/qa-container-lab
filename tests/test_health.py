import os
import requests

def test_health_endpoint():
    base_url = os.getenv("BASE_URL", "http://localhost:8080")
    r = requests.get(f"{base_url}/health", timeout=10)
    assert r.status_code == 200
