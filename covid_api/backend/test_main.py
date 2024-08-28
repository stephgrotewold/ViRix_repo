from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_covid_stats():
    response = client.get("/covid-stats/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

if __name__ == "__main__":
    test_read_covid_stats()
    print("All tests passed successfully!")