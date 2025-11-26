import requests


class GuardRequest:
    def __init__(self, backend_url):
        self.backend_url = backend_url

    def get_all_guards(self):
        """Őrök listázása"""
        try:
            r = requests.get(f"{self.backend_url}/guards")
            json_data = r.json() if r.status_code == 200 else {}
            return json_data.get("data", [])  # itt kivesszük a 'data' kulcsot
        except Exception as e:
            return []


    def get_guard_schedule(self, guard_id: int):
        """Őr beosztás lekérése"""
        try:
            r = requests.get(f"{self.backend_url}/guards/{guard_id}/schedule")
            return r.json() if r.status_code == 200 else []
        except Exception as e:
            print("Hiba a get_guard_schedule hívásnál:", e)
            return {"status": 500, "data": [], "error": str(e)}
