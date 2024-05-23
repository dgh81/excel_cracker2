import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_ALL
from PIL import Image
from idlelib.tooltip import Hovertip
import cracker

def main():
    
    class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.TkdndVersion = TkinterDnD._require(self)
    
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')

    global root
    root = Tk()

    root.geometry('600x400')
    # root.iconbitmap('./images/icon.ico')
    root.title('Excel Sheets Password Cracker')
    
    global crack_button
    
    def get_path(event):
        filepathVar = event.data
        xl_file_path.configure(placeholder_text=filepathVar)
        crack_button.pack(padx=60, pady=20, side=ctk.BOTTOM, fill=ctk.BOTH, expand=False)

    label_heading = ctk.CTkLabel(root, text='Crack me a river', font=('Ariel', 24))
    label_heading.pack(padx=60, pady=20, side=ctk.TOP, fill=ctk.BOTH, expand=False)

    label_pic = ctk.CTkLabel(root, image=ctk.CTkImage(Image.open("1.0/images/fawkes.jpg"), size=(100,100)), text='')
    label_pic.pack(padx=60, pady=20, side=ctk.TOP, fill=ctk.BOTH, expand=False)
    
    xl_file_path = ctk.CTkEntry(root, placeholder_text="+ Smid fil her", justify='center')
    xl_file_path.pack(padx=60, pady=20, side=ctk.BOTTOM, fill=ctk.BOTH, expand=False)

    xl_file_path.drop_target_register(DND_ALL)
    xl_file_path.dnd_bind("<<Drop>>", get_path)

    global label_done
    label_done = ctk.CTkLabel(root, text='', font=('Ariel', 16))

    
    def crack_selected_xl_file():
        result = xl_file_path.cget("placeholder_text")
        if result[0] == "{":
            result = result[1:-1]
        if cracker.crack(result):
            label_done.pack(padx=60, pady=20, side=ctk.BOTTOM, fill=ctk.BOTH, expand=False)
            label_done.configure(text='DONE')

    crack_button = ctk.CTkButton(root, text='CRACK DET!', font=('Ariel', 16), command=crack_selected_xl_file)

    root.mainloop()

if __name__ == '__main__':
    main()