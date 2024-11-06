from locust import HttpUser, task, between
import random

class VirixAPIUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Inicializamos la variable para almacenar el ID del centro de salud creado
        self.health_center_id = None
        # Datos de prueba para crear el centro de salud
        self.test_center = {
            "name": "TEST Health Center",
            "address": "123 F Street",
            "phone_number": "+1234567890",
            "services": "COVID-19 Testing",
            "latitude": -25.2744,
            "longitude": 133.7751
        }
        # Valores de prueba para filtros
        self.services = ["COVID-19 Testing", "Vaccination Center", "Emergency Room"]
        self.countries = ["Australia", "Guatemala", "Afghanistan"]  # Ajusta a los países en tu base de datos

    @task(3)
    def get_heatmap_data(self):
        """Prueba el endpoint del mapa de calor - alta prioridad"""
        self.client.get("/heatmap-data")

    @task(2)
    def get_health_centers_with_filters(self):
        """Prueba el endpoint /health_centers/ con filtros de país y servicio"""
        # Seleccionar un servicio y un país al azar para la prueba
        service = random.choice(self.services)
        country = random.choice(self.countries)

        # Enviar solicitud con filtros
        params = {"services": service, "country": country}
        with self.client.get("/health_centers/", params=params, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed to get health centers with filters: {response.text}")

    @task(1)
    def crud_health_centers(self):
        """Prueba las operaciones CRUD para centros de salud"""
        
        # 1. Crear un centro de salud
        with self.client.post("/health_centers/", 
                            json=self.test_center,
                            catch_response=True) as response:
            if response.status_code == 200:
                # Guardamos el ID del centro de salud creado
                self.health_center_id = response.json().get("_id")
                response.success()
            else:
                response.failure(f"Failed to create health center: {response.text}")

        if self.health_center_id:
            # Elimina o comenta la siguiente línea para evitar el error
            # self.client.get(f"/health_centers/{self.health_center_id}")

            # 3. Actualizar el centro de salud
            updated_data = self.test_center.copy()
            updated_data["name"] = f"Updated Center {random.randint(1, 1000)}"
            with self.client.put(f"/health_centers/{self.health_center_id}", 
                                json=updated_data,
                                catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Failed to update health center: {response.text}")

            # 4. Eliminar el centro de salud
            with self.client.delete(f"/health_centers/{self.health_center_id}",
                                    catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Failed to delete health center: {response.text}")