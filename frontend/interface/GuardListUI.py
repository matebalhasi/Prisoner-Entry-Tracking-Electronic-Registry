import customtkinter as ctk
from frontend.interface.BaseUI import BaseWindow


class GuardListUI(BaseWindow):
    def __init__(self, backend_url, guard_request):
        super().__init__("Őrök listája")

        self.request = guard_request
        self.backend_url = backend_url

        self.frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame.pack(padx=30, pady=30, fill="both", expand=True)

        ctk.CTkLabel(
            self.frame,
            text="Őrök listája",
            font=ctk.CTkFont(size=26, weight="bold")
        ).pack(pady=20)

        self.list_frame = ctk.CTkScrollableFrame(self.frame, width=700, height=400)
        self.list_frame.pack(expand=True)

        self.load_guards()

    def load_guards(self):
        guards = self.request.get_all_guards()

        if not guards:
            ctk.CTkLabel(self.list_frame, text="Nincs megjeleníthető adat.").pack()
            return

        for g in guards:
            text = f"{g['F_Name']} {g['L_Name']} | Rang: {g['Rank']} | Block: {g['Block_ID']}"
            ctk.CTkLabel(
                self.list_frame,
                text=text,
                font=ctk.CTkFont(size=16)
            ).pack(anchor="w", padx=10, pady=5)
