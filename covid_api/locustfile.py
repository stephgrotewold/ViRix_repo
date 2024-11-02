from locust import HttpUser, task, between
import random

class HealthCenterTestUser(HttpUser):
    wait_time = between(1, 3)
    existing_ids = [22209, 22216, 22218, 22226, 22232, 22237, 22240, 22244, 22250]  # Sample IDs for PUT and other tasks

    @task
    def get_health_centers(self):
        response = self.client.get("/health_centers/")
        if response.status_code == 200:
            print("GET /health_centers/ completed successfully")
        else:
            print(f"GET /health_centers/ failed with status {response.status_code}")

    @task
    def create_health_center(self):
        payload = {
            "name": "New Center",
            "address": "Test Address",
            "phone_number": "123456789",
            "services": "Testing Services",
            "latitude": 40.7128,
            "longitude": -74.006
        }
        response = self.client.post("/health_centers/", json=payload)
        if response.status_code == 201:
            new_id = response.json().get("id")
            print(f"POST /health_centers/ created with ID {new_id}")
            if new_id:
                self.existing_ids.append(new_id)
        else:
            print(f"POST /health_centers/ failed with status {response.status_code}")

    @task
    def update_health_center(self):
        if not self.existing_ids:
            print("No available IDs to update")
            return

        update_id = random.choice(list(self.existing_ids))
        payload = {
            "name": "Updated Center",
            "address": "Updated Address",
            "phone_number": "987654321",
            "services": "Updated Services",
            "latitude": 40.7128,
            "longitude": -74.006
        }
        response = self.client.put(f"/health_centers/{update_id}", json=payload)
        if response.status_code == 200:
            print(f"PUT /health_centers/{update_id} updated successfully")
        elif response.status_code == 404:
            print(f"ID {update_id} not found for update")
            self.existing_ids.remove(update_id)
        else:
            print(f"PUT /health_centers/{update_id} failed with status {response.status_code}")

    @task
    def get_heatmap_data(self):
        response = self.client.get("/heatmap-data")
        if response.status_code != 200:
            print(f"GET /heatmap-data failed with status {response.status_code}")

    @task
    def get_covid_data_by_country(self):
        country = "Brazil"
        response = self.client.get(f"/covid-data?location={country}")
        if response.status_code != 200:
            print(f"GET /covid-data for {country} failed with status {response.status_code}")