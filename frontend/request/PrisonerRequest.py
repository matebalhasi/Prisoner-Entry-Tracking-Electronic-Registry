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
    
    def add_prisoner(self, data: dict):
        """Új fogvatartott felvétele"""
        try:
            r = requests.post(f"{self.backend_url}/prisoners/add", json=data)
            return r.json()
        except:
            return {"error": "backend error"}
        
    def move_prisoner(self, pid: int, new_cell: int):
        """Fogvatartott áthelyezése cella szerint"""
        try:
            r = requests.put(
                f"{self.backend_url}/prisoners/{pid}/move",
                json={"new_cell": new_cell}
            )
            return r.json()
        except:
            return {"error": "backend error"}
