import requests


class CellsRequest:
    def __init__(self, backend_url):
        self.backend_url = backend_url

    def get_all_blocks(self):
        try:
            r = requests.get(f"{self.backend_url}/blocks")
            return r.json().get("data", []) if r.status_code == 200 else []
        except:
            return []

    def get_cells_by_block(self, block_id: int):
        """Lekéri a cellákat az adott Block_ID alapján"""
        try:
            r = requests.get(f"{self.backend_url}/cells/blocks/{block_id}")
            print(r.status_code)
            print(r.headers.get('Content-Type'))
            print(r.text)
            return r.json() if r.status_code == 200 else []
        except:
            return []

    def get_prisoner_in_cell(self, cell_number: int):
        """Lekéri a cellában lévő fogvatartott(ak?) adatait"""
        try:
            r = requests.get(f"{self.backend_url}/cells/{cell_number}/prisoners")
            return r.json() if r.status_code == 200 else []
        except:
            return []
