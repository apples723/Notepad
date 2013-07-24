import Tkinter as tk
import sys
from tkFileDialog import *
from Tkinter import Frame
import tkMessageBox
from tkMessageBox import askokcancel
class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)    
        self.text = text
    def settext(self, text='', file=None):
        if file: 
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                   
        self.text.insert('1.0', text)                  
        self.text.mark_set(INSERT, '1.0')              
        self.text.focus()                                
    def gettext(self):                               
        return self.text.get('1.0', END+'-1c') 
class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._menubar()
        self.text = tk.Text()
        self.text.pack(side="top", fill="both", expand=True)
        self.title("Multi-Purpose Text Editor")
    def _menubar(self):
        
        self.menubar = tk.Menu()
        self.configure(menu=self.menubar)

        file_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.onsave)
        file_menu.add_command(label="Quit", command=self.on_quit)
    
        edit_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", underline=2, command=self.on_cut)
        edit_menu.add_command(label="Copy", underline=0, command=self.on_copy)
        edit_menu.add_command(label="Paste", underline=0, command=self.on_paste)

        help_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Notepad Help", underline=0, command=self.on_help)
        help_menu.add_command(label="About", underline=0, command=self.on_about)
    def gettext(self):                               
        return self.text.get('0.0')
    def on_help(self):
        tkMessageBox.showinfo("Help", """
Instruction:
1. Start typing.
2. Type what you want
3. Press save.
4. When done click close
F.A.Q.
Q: Does this application have shortcuts?
A: Yes. It has the standard Edit commnads. I doesnot support the ctrl+s to save a file yet.
Q: How do I open a file?
A: You can't yet I'm working on a way to open a file.
""")
    def on_about(self):
        tkMessageBox.showinfo("About", """
Created by: Grant
Designed in python using tkinter.
""")
    def onsave(self):
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('Text Files', '.txt'), ('Python File', '.py'), ("All Files", ".*")]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'Type File Name Here'
        options['title'] = 'Save'

        filename = asksaveasfilename(**self.file_opt)
        if filename:
            alltext = self.gettext()                      
            open(filename, 'w').write(alltext) 
        
    def on_cut(self): 
        try:
            text = self.text.get(SEL_FIRST, SEL_LAST)        
            self.text.delete(SEL_FIRST, SEL_LAST)           
            self.clipboard_clear()              
            self.clipboard_append(text)
        except AttributeError:
            pass
        except NameError:
            pass
    def on_paste(self): 
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert('insert', text)
        except AttributeError:
            pass
        except NameError:
            pass
        except TclError:
            pass
    def on_copy(self):
        try:
            self.clipboard_clear()
            text = self.get("sel.first", "sel.last")
            self.clipboard_append(text)
        except AttributeError:
            pass
        except NameError:
            pass
    def on_quit(self):
        ans = askokcancel("Confirm Exit", "Sure you want to quit?")
        if ans: sys.exit()
if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
