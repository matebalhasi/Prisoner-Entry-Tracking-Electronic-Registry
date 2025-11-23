import tkinter as tkinter
import requests
from tkinter import messagebox
import sys

def check_connection(backendurl):
        BACKEND_URL = backendurl
        try:
            valasz = requests.get(BACKEND_URL+"/check_connection")
            if valasz.status_code == 200:
                return (200)
        except requests.exceptions.RequestException as e:
            kapcsolodasi_hiba(e)

def kapcsolodasi_hiba(e):
      messagebox.showerror("Kapcsolódási hiba", "Hiba türtént az alkalmazás indításakor. ({e})! \n \n Kérem forduljon az üzemeltetőkhöz!")
      sys.exit()