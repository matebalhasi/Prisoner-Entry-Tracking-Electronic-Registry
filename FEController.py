

from Frontend import MainMenuUI

import os
#from dotenv import load_dotenv, dotenv_values

class FEController:
#"""Minimalis kontroller, ami csak elindítja a GUI-t."""

    fomenu_ablak = MainMenuUI.MainMenuUI()
    fomenu_ablak.run()
