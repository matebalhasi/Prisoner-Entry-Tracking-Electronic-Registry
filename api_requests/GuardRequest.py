import api_requests


class GuardRequest:
    def __init__(self, backend_url):
        self.backend_url = backend_url

    def get_all_guards(self):
        """Őrök listázása"""
        try:
            r = api_requests.get(f"{self.backend_url}/guards")
            return r.json() if r.status_code == 200 else []
        except:
            return []

    def get_guard_schedule(self, guard_id: int):
        """Őr beosztás lekérése"""
        try:
            r = api_requests.get(f"{self.backend_url}/guards/{guard_id}/schedule")
            return r.json() if r.status_code == 200 else []
        except:
            return []
