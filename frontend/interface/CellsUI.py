import customtkinter as ctk
from frontend.interface.BaseUI import BaseWindow


class CellsUI(BaseWindow):
    def __init__(self, backend_url, cells_request, block_id):
        super().__init__("Cella térkép")

        self.req = cells_request
        self.backend_url = backend_url
        self.block_id = block_id

        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        title = ctk.CTkLabel(
            frame,
            text=f"Cella lista – Blokk: {block_id}",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        title.pack(pady=10)

        # Cella gombok helye
        self.cell_frame = ctk.CTkScrollableFrame(frame, width=700, height=350)
        self.cell_frame.pack(pady=15)

        # Fogvatartott adatok helye
        self.result_frame = ctk.CTkFrame(frame, fg_color="transparent")
        self.result_frame.pack(pady=10, fill="both", expand=True)

        self.load_cells()


    # Cella gombok
    def load_cells(self):
        cells = self.req.get_cells_by_block(self.block_id)

        if not cells:
            ctk.CTkLabel(self.cell_frame, text="Nincs cella ebben a blokkban.").pack()
            return

        for c in cells:
            cell_number = c["Cell_Number"]

            ctk.CTkButton(
                self.cell_frame,
                text=f"Cella {cell_number}",
                width=200,
                fg_color="#2A8AC0",
                hover_color="#1F6AA5",
                command=lambda cn=cell_number: self.load_cell_prisoners(cn)
            ).pack(pady=6)

    
    # Fogvatartottak a cellában
    def load_cell_prisoners(self, cell_number):
        # Eredmény terület törlése
        for w in self.result_frame.winfo_children():
            w.destroy()

        prisoners = self.req.get_prisoners_in_cell(cell_number)

        ctk.CTkLabel(
            self.result_frame,
            text=f"Cella {cell_number} – Fogvatartottak:",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=5)

        if not prisoners:
            ctk.CTkLabel(self.result_frame, text="A cella üres.").pack()
            return

        for p in prisoners:
            text = (
                f"{p['L_Name']} {p['F_Name']} {p['Birth_Date']}  |  "
                f"Veszélyességi szint: {p['Danger_Level']}"
            )
            ctk.CTkLabel(
                self.result_frame,
                text=text,
                font=ctk.CTkFont(size=16)
            ).pack(anchor="w", pady=4)
