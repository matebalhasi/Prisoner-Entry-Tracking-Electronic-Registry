import requests 

class PrisonerRequest:
    def __init__(self, backend_url):
        self.backend_url = backend_url.rstrip("/")  

    def get_all_prisoners(self):
        """Fogvatartottak lekérése a backendről"""
        try:
            response = requests.get(f"{self.backend_url}/prisoners")
            response.raise_for_status()  
            return response.json()  
        except requests.RequestException as e:
            print("Hiba a get_all_prisoners hívásnál:", e)
            return {"status": 500, "data": [], "error": str(e)}
    
    def add_prisoner(self, data: dict):
        """Új fogvatartott felvétele"""
        try:
            r = requests.post(f"{self.backend_url}/prisoners/add", json=data)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print("Hiba az add_prisoner hívásnál:", e)
            return {"status": 500, "error": str(e)}
        
    def move_prisoner(self, pid: int, new_cell: int):
        """Fogvatartott áthelyezése cella szerint"""
        url = f"{self.backend_url}/prisoners/{pid}/move"
        try:
            response = requests.put(url, json={"new_cell": new_cell}, timeout=5)
            # Ha HTTP hiba, kivétel lesz itt:
            try:
                response.raise_for_status()
            except requests.HTTPError:
                # Megpróbáljuk kiolvasni a hibaválaszt (JSON vagy sima szöveg)
                try:
                    return response.json()
                except ValueError:
                    return {"status": response.status_code, "error": response.text}

            # Sikeres válasz kezelése
            try:
                return response.json()
            except ValueError:
                # Nem JSON válasz, adjunk vissza konzisztenst objektumot
                return {"status": response.status_code, "data": None, "error": response.text}

        except requests.RequestException as e:
            print("Hiba a move_prisoner hívásnál:", e)
            return {"status": 500, "error": str(e)}