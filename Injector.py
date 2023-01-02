import time
import tkinter
import customtkinter
from pymem import *
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.title("DLL Injector")
app.geometry("200x210")
app.resizable(False, False)


def click():
    headerLbl._text = "Status : Success"
    dll_path = customtkinter.CTkInputDialog(text="DLL path:", title="DLL path")
    process_name = customtkinter.CTkInputDialog(text="Process name:", title="Name of process")
    try:
        dll = bytes(dll_path.get_input(), "UTF-8")
        file = Pymem(process_name.get_input())
        process.inject_dll(file.process_handle, dll)
        print("Success")
    except:
        print("UnSuccess")


headerLbl = customtkinter.CTkLabel(master=app, text="DLL Injector")
headerLbl.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
creditsLbl = customtkinter.CTkLabel(master=app, text="by KittyNeverDies")
creditsLbl.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=app, text="Inject", command=click)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
app.mainloop()
