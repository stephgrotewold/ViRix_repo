import cProfile
import pstats
from fastapi.testclient import TestClient
from main import app
import json
from bson import ObjectId


def profile_api():
    profiler = cProfile.Profile()
    client = TestClient(app)

    # Test data
    test_center = {
        "name": "Test Health Center",
        "address": "123 Test Street",
        "phone_number": "+1234567890",
        "services": "COVID-19 Testing",
        "latitude": 40.7128,
        "longitude": -74.0060
    }

    # Start profiling
    profiler.enable()

    try:
        # Test GET /heatmap-data
        print("\nTesting GET /heatmap-data")
        response = client.get("/heatmap-data")
        print(f"Status: {response.status_code}")

        # Test POST /health_centers/
        print("\nTesting POST /health_centers/")
        response = client.post("/health_centers/", json=test_center)
        print(f"Status: {response.status_code}")

        if response.status_code == 200:
            center_id = response.json().get("_id")

            # Test GET /health_centers/
            print("\nTesting GET /health_centers/")
            response = client.get("/health_centers/")
            print(f"Status: {response.status_code}")

            # Test PUT /health_centers/{center_id}
            print(f"\nTesting PUT /health_centers/{center_id}")
            test_center["name"] = "Updated Test Center"
            response = client.put(f"/health_centers/{center_id}", json=test_center)
            print(f"Status: {response.status_code}")

            # Test DELETE /health_centers/{center_id}
            print(f"\nTesting DELETE /health_centers/{center_id}")
            response = client.delete(f"/health_centers/{center_id}")
            print(f"Status: {response.status_code}")

    finally:
        # Stop profiling
        profiler.disable()

        # Print results
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')

        # Save detailed results to a file
        with open('profiling_results_4.txt', 'w') as f:
            stats = pstats.Stats(profiler, stream=f)
            stats.sort_stats('cumulative')
            stats.print_stats()

            # Print function calls by time
            f.write("\n\nFunction Calls by Time:\n")
            stats.sort_stats('time')
            stats.print_stats(20)

            # Print callers for expensive functions
            f.write("\n\nCallers of Expensive Functions:\n")
            stats.print_callers()


if __name__ == "__main__":
    profile_api()