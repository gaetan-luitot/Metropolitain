"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable
import os
import sys

os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tcl8.6.8'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tk8.6.8'

base = None    
if sys.platform == "win32":    
    base = "Win32GUI"    

# On appelle la fonction setup
setup(
    name = "Metropolitain : 2078",
    version = "1.0",
    description = "Un jeu de rôle dans le métropolitain parisien en 2078",
    options = {"build_exe": {"includes": ["tkinter"], "include_files": ["S1.save", "brouillage.gif","tcl86t.dll", "tk86t.dll"]}},
    executables = [Executable("p_Jeu.py", base = base)],
)
