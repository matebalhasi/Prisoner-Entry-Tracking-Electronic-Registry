import customtkinter as ctk
from frontend.interface.BaseUI import BaseWindow


class PrisonerListUI(BaseWindow):
    def __init__(self, backend_url, prisoner_request):
        super().__init__("Fogvatartottak listája")

        self.backend_url = backend_url
        self.request = prisoner_request

        self.frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(
            self.frame,
            text="Fogvatartottak listája",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        ).pack(pady=20)

        self.list_frame = ctk.CTkScrollableFrame(self.frame, width=700, height=400)
        self.list_frame.pack(expand=True)

        self.load_prisoner_list()

    def load_prisoner_list(self):
        prisoners = self.request.get_all_prisoners()

        if not prisoners:
            ctk.CTkLabel(
                self.list_frame,
                text="Nincs megjeleníthető adat.",
                text_color="gray"
            ).pack()
            return

        for p in prisoners:
            item = ctk.CTkLabel(
                self.list_frame,
                text=f"{p['F_Name']} {p['L_Name']} | Cell: {p['Cell_Number']} | Danger: {p['Danger_Level']} | Birth date: {p['Birth_Date']}",
                font=ctk.CTkFont(size=16),
                text_color="white"
            )
            item.pack(anchor="w", padx=10, pady=5)
