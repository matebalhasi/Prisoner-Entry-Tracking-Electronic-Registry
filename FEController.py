import tkinter as tk
from tkinter import messagebox
from api_requests.PrisonerRequest import PrisonerRequest

from api_requests.Connection import check_db_connection

from frontend.MainMenuUI import MainMenuUI


def start_frontend():
    db_ok = check_db_connection()

    if not db_ok:
        root = tk.Tk()
        root.withdraw()  # Hide root window
        messagebox.showwarning(
            "Database Unavailable",
            "The database is currently unreachable.\n"
            "If you continue, no data will be loaded."
        )

    menu = MainMenuUI()
    menu.run()


if __name__ == "__main__":
    start_frontend()
