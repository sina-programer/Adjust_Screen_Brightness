from tkinter import *
from tkinter import messagebox
import screen_brightness_control as sbc
import webbrowser
import os

class Indicator:
    def __init__(self, master, text, from_, to, x, y):
        self.__variable = IntVar()
        
        self.__label = Label(master, text=text)
        self.__label.place(x=x, y=y)
        
        self.__scale = Scale(master, from_=from_, to=to, variable=self.__variable, orient=HORIZONTAL)
        self.__scale.place(x=x+95, y=y-19)
        self.__scale.bind('<MouseWheel>', lambda event: self.__rolling(event))
                
    def __rolling(self, event):
        current = self.__variable.get()
        delta = event.delta
        if delta>0:
            current += 1
        else:
            current -= 1
        self.set(current)
        
    def set(self, value):
        self.__variable.set(value)
        
    def get(self):
        return self.__variable.get()

 
class ASB:
    ''' Adjust Screen Brightness '''
    def __init__(self, master):
        self.window = master
        self.window.config(menu=self.init_menu())
        self.window.bind('<Escape>', lambda _: self.reset())
        self.window.bind('<Return>', lambda _: self.adjust(self.indicator.get()))
        
        self.indicator = Indicator(self.window, 'Brightness Level: ', 0, 100, 10, 18)
        self.adjust_btn = Button(self.window, text='Adjust', width=8, command= lambda:self.adjust(self.indicator.get()))
        self.adjust_btn.place(x=230, y=15)
        self.first_level = sbc.get_brightness()
        self.reset()
        
    def adjust(self, level):
        sbc.set_brightness(level)
        
    def reset(self):
        self.indicator.set(self.first_level)

    def show_about(self):
        dialog = Tk()
        dialog.title('About us')
        dialog.iconbitmap(icon)
        dialog.geometry('300x100+550+350')
        dialog.focus_force()
        
        print('\a')
        Label(dialog, text='This program made by Sina.f').pack(pady=12)
        Button(dialog, text='GitHub', width=8, command=lambda: webbrowser.open('https://github.com/sina-programer')).place(x=30, y=50)
        Button(dialog, text='Instagram', width=8, command=lambda: webbrowser.open('https://www.instagram.com/sina.programer')).place(x=120, y=50)
        Button(dialog, text='Telegram', width=8, command=lambda: webbrowser.open('https://t.me/sina_programer')).place(x=210, y=50)
        
        dialog.mainloop()
        
    def init_menu(self):
        menu = Menu(self.window)
        menu.add_command(label='Help', command=lambda: messagebox.showinfo('Help', help_msg))
        menu.add_command(label='About us', command=self.show_about)
        
        return menu


help_msg = '''
You can change your screen brightness easily now!\n
Shortcuts
<Enter> Adjust screen brightness
<Esc>     Reset to first brightness level'''

icon = r'Files\icon.ico'


if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    root.title('Adjust Screen Brightness')
    root.geometry('310x55+550+300')
    
    if os.path.exists(icon):
        root.geometry('310x75+550+300')
        root.iconbitmap(icon)
        
    app = ASB(root)
    
    root.mainloop()