import tkinter as tk
from tkinter import font
from tkinter import *
import subprocess

def execute_commands():
    commands = [
        "slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX",
        "slmgr /skms kms.digiboy.ir",
        "slmgr /ato"
    ]
    
    for command in commands:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Activation Windows 10/11 Pro")
root.geometry("450x130")
root.resizable(False, False)
root.configure(bg='#838B83')
root.iconbitmap(r'C:\Windows\System32\credwiz.exe')

# Ajout d'un bouton pour exécuter les commandes
label_font = font.Font(size=11,weight="bold")
label = tk.Label(root, text="Activation Windows 10 and 11 Edition Professionnel",fg="black", bg="#838B83", font=label_font )
#url = tk.Label(root, text="https://www.youtube.com/@zakourinos9712/videos",justify="right",fg="blue", bg="#838B83", font=label_font )




# Boucle principale de l'application
label.pack()
btn_execute = tk.Button(root,fg='#97FFFF',bg='#008000', text="🔑 Activation Windows",font=10,activebackground='#63B8FF',command=execute_commands)
btn_execute.pack(pady=20)
tk.Button(root,fg='red',bg='black', text="Exit",font=label_font , command=root.destroy).pack() 
#url.pack()
root.mainloop()
