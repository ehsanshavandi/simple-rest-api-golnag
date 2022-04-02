from locust import HttpUser, task


class PerfTestExmp(HttpUser):
    @task
    def v1_test_api(self):
        self.client.get("/v1/test")
