import customtkinter as ctk
from frontend.interface.BaseUI import BaseWindow
from tkinter import messagebox

class GuardScheduleUI(BaseWindow):
    def __init__(self, guard_request, master=None):
        if master:
            self.root = ctk.CTkToplevel(master)
            self.root.transient(master)
            #self.root.grab_set()
        else:
            self.root = ctk.CTk()
        self.root.title("Őr beosztása")
        self.root.geometry("800x500")

        self.request = guard_request

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
        # Régi widgetek törlése
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        guard_id_str = self.guard_id_entry.get()
        if not guard_id_str.isdigit():
            messagebox.showerror("Hiba", "Az Őr ID csak szám lehet.")
            return

        guard_id = int(guard_id_str)

        try:
            schedule_data = self.request.get_guard_schedule(guard_id)
            print("DEBUG schedule_data:", schedule_data)
        except Exception as e:
            messagebox.showerror("Hiba", f"Beosztás lekérése sikertelen: {str(e)}")
            return

        # Ha nincs adat vagy üres lista
        if not schedule_data or ("data" in schedule_data and not schedule_data["data"]):
            ctk.CTkLabel(self.list_frame, text="Nincs beosztás.").pack(pady=10)
            return

        # Feldolgozás
        shifts = schedule_data.get("data", schedule_data)  # lehet lista vagy dict['data']
        for s in shifts:
            day = s.get("Shift_Day", "?")
            shift_type = s.get("Shift_Type", "?")
            start_time = s.get("Start_Time", "?")
            end_time = s.get("End_Time", "?")
            text = f"Nap: {day}  |  Műszak: {shift_type}  |  Kezdés: {start_time}  |  Befejezés: {end_time}"
            ctk.CTkLabel(self.list_frame, text=text, font=ctk.CTkFont(size=16)).pack(anchor="w", padx=10, pady=5)