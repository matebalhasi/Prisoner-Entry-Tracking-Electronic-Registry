import customtkinter as ctk
from tkinter import messagebox, simpledialog, Toplevel, Label
from frontend.interface.BaseUI import BaseWindow


class CellsUI(BaseWindow):
    def __init__(self, cells_request, master = None):
        if master:
            self.root = ctk.CTkToplevel(master)
            self.root.transient(master)
            #self.root.grab_set()
        else:
            self.root = ctk.CTk()
        
        self.root.title("Cella Lista")
        self.root.geometry("800x600")

        self.req = cells_request
        self.block_id = None
        
        frame = ctk.CTkFrame(self.root, fg_color="transparent")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        title = ctk.CTkLabel(
            frame,
            text="Cella keresés",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        title.pack(pady=10)



        

        self.cell_frame = ctk.CTkScrollableFrame(frame, width=700, height=400)
        self.cell_frame.pack(pady=10, fill="both", expand=True)


        self.ask_block_id()
    def ask_block_id(self):
        block_id = simpledialog.askinteger(
            "Blokk kiválasztása",
            "Add meg a blokk ID-t:",
            parent = self.root
        )
        if block_id is None:
            self.root.destroy()
            return
        
        self.block_id = block_id
        self.load_cells()
    
    
    def load_cells(self):

        for w in self.cell_frame.winfo_children():

            w.destroy()
        try:
            cells = self.req.get_cells_by_block(self.block_id)
            print("DEBUG: Visszakapott JSON:", cells)

        except Exception as e:
            messagebox.showerror("Hiba",f"A backend nem elérhető: {str(e)}")
            cells = []
        if not cells:
            ctk.CTkLabel(
                self.cell_frame, 
                text=f"Nincs cella a {self.block_id}. blokkban."
            ).pack(pady=10)
            return
        for c in cells:
            cell_number = c.get("Cell_Number", "?")
            lbl = ctk.CTkLabel(
                self.cell_frame,
                text=f"Cella {cell_number}",
                font=ctk.CTkFont(size=16),
                fg_color="#2A8AC0",
                corner_radius=5,
                width=200,
                pady=5
            )
            lbl.pack(pady=5, padx=10, anchor="w")
            lbl.bind("<Double-1>", lambda e, cn=cell_number: self.open_prisoners(cn))

    
    
    def open_prisoners(self, cell_number):
        try:
            prisoners = self.req.get_prisoner_in_cell(cell_number)
        except Exception as e:
            messagebox.showerror("Hiba", f"A backend nem elérhető: {str(e)}")
            prisoners = []
        win = Toplevel(self.root)
        win.title(f"Fogvatartottak - Cella {cell_number}")
        win.geometry("500x400")

        if not prisoners:
            Label(win, text="A cella üres.").pack(pady=10)
            return

        Label(
            win, 
            text=f"Fogvatartottak a {cell_number} cellában:", 
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        for p in prisoners:
            text = (
                f"{p.get('L_Name', '?')} {p.get('F_Name', '?')} | "
                f"Születési dátum: {p.get('Birth_Date', '?')} | "
                f"Veszélyességi szint: {p.get('Danger_Level', '?')}"
            )
            Label(
                win, 
                text=text, 
                anchor="w", 
                justify="left"
            ).pack(fill="x", padx=10, pady=4)

    