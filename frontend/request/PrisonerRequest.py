import requests

class PrisonerRequest:
    def __init__(self, backend_url):
        self.backend_url = backend_url

    def get_all_prisoners(self):
        """Fogvatartottak lekérése a backendről"""
        try:
            response = requests.get(f"{self.backend_url}/prisoners")
            if response.status_code == 200:
                return response.json()
            return []
        except:
            return []
