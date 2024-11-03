from locust import HttpUser, task, between
import json
import random

class VirixAPIUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.health_center_id = None
        self.test_center = {
            "name": "TEST Health Center",
            "address": "123 F Street",
            "phone_number": "+1234567890",
            "services": "COVID-19 Testing",
            "latitude": 40.7128,
            "longitude": -74.0060
        }

    @task(3)
    def get_heatmap_data(self):
        """Test the heatmap endpoint - highest priority"""
        self.client.get("/heatmap-data")

    @task(2)
    def get_health_centers(self):
        """Test getting health centers list"""
        self.client.get("/health_centers/")

    @task(1)
    def crud_health_centers(self):
        """Test CRUD operations for health centers"""
        # Create
        with self.client.post("/health_centers/", 
                            json=self.test_center,
                            catch_response=True) as response:
            if response.status_code == 200:
                self.health_center_id = response.json().get("_id")
                response.success()
            else:
                response.failure(f"Failed to create health center: {response.text}")

        if self.health_center_id:
            # Update
            updated_data = self.test_center.copy()
            updated_data["name"] = f"Updated Center {random.randint(1, 1000)}"
            self.client.put(f"/health_centers/{self.health_center_id}", 
                          json=updated_data)

            # Delete
            self.client.delete(f"/health_centers/{self.health_center_id}")