import customtkinter as ctk
from frontend.interface.BaseUI import BaseWindow


class GuardScheduleUI(BaseWindow):
    def __init__(self, backend_url, guard_request):
        super().__init__("Őr beosztása")

        self.request = guard_request
        self.backend_url = backend_url

        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(padx=30, pady=30, fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text="Őr beosztás megtekintése",
            font=ctk.CTkFont(size=26, weight="bold")
        ).pack(pady=20)

        self.guard_id_entry = ctk.CTkEntry(frame, placeholder_text="Őr ID", width=300)
        self.guard_id_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Beosztás lekérése",
            fg_color="#2A8AC0",
            hover_color="#1F6AA5",
            width=300,
            command=self.load_schedule
        ).pack(pady=15)

        self.list_frame = ctk.CTkScrollableFrame(frame)
        self.list_frame.pack(pady=20, fill="both", expand=True)

    def load_schedule(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        guard_id = self.guard_id_entry.get()

        schedule = self.request.get_guard_schedule(int(guard_id))

        if not schedule:
            ctk.CTkLabel(self.list_frame, text="Nincs beosztás.").pack()
            return

        for s in schedule:
            text = f"Nap: {s['Day']}  |  Műszak: {s['Shift']}"
            ctk.CTkLabel(self.list_frame, text=text).pack(anchor="w", padx=10, pady=5)
