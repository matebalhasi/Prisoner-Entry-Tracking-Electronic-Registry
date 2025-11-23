import customtkinter as ctk
from frontend.interface.BaseUI import BaseWindow


class PrisonerMoveUI(BaseWindow):
    def __init__(self, backend_url, prisoner_request):
        super().__init__("Fogvatartott áthelyezése")

        self.req = prisoner_request
        self.backend_url = backend_url

        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(padx=30, pady=30, fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text="Fogvatartott áthelyezése",
            font=ctk.CTkFont(size=26, weight="bold")
        ).pack(pady=20)

        self.pid = self._input(frame, "Fogvatartott ID")
        self.new_cell = self._input(frame, "Új cellaszám")

        ctk.CTkButton(
            frame,
            text="Áthelyezés",
            width=300,
            fg_color="#2A8AC0",
            hover_color="#1F6AA5",
            command=self.move_prisoner
        ).pack(pady=25)

    def _input(self, parent, placeholder):
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder, width=350)
        entry.pack(pady=8)
        return entry

    def move_prisoner(self):
        pid = int(self.pid.get())
        new_cell = int(self.new_cell.get())

        response = self.req.move_prisoner(pid, new_cell)
        print("Backend válasz:", response)
