from typing import Type
from files_organizer.data_abm import DatabaseConnector
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno, showwarning

class InterfaceParser():
    def __init__(self, db:Type[DatabaseConnector]) -> None:
        self._window =  tk.Tk()
        self._pairing = {}
        self._to_delete = {}
        self.db =db

    @property
    def window(self):
        return self._window
    @property
    def pairing(self):
        return self._pairing
    
    @pairing.setter
    def pairing(self, val):
        self._pairing = val

    @property
    def to_delete(self):
        return self._to_delete
    
    @to_delete.setter
    def to_delete(self, val):
        self._to_delete = val

    def parse_input_values(self,input):
        stripped=input.strip()
        if stripped[0] != '.':
            return '.'+stripped
        return stripped
    
    def handle_addition(self,event):
        new_pair={}
        if not self.search_key.get() or not self.search_value.get():
            showwarning(title="Invalid input",message="You must provide both key and values")
            return "break"
        new_pair["name"]=self.search_key.get()
        new_pair["values"]= list(map(self.parse_input_values, self.search_value.get().split(',')))
        self.pairing = new_pair
        self.db.new_pairing_batch(self.pairing['name'], self.pairing['values'])
        self.result.config(text=f"Added pairings for {self.pairing['name']}")
        self.search_key.delete(0,'end')
        self.search_value.delete(0,'end')

    def handle_deletion(self,event):
        to_delete={}
        to_delete["name"]=self.deletion_key.get()
        if not to_delete["name"]:
            return "break"

        if self.deletion_value.get():
            confirm_deletion = askyesno(title='Warning: Deleting pairings',
            message=f"Are you sure that you want to delete pairings for {to_delete['name']}?")
            if not confirm_deletion:
                return "break"
            to_delete["values"]= list(map(self.parse_input_values, self.deletion_value.get().split(',')))
            self.to_delete = to_delete
            self.db.delete_pairing_batch(self.to_delete['name'], self.to_delete['values'])
            self.result.config(text=f"Deleted pairings for {to_delete['name']}")
        else:
            confirm_deletion = askyesno(title='Warning: Deleting pairings',
            message=f"Are you sure that you want to delete ALL values for {to_delete['name']}?")
            if not confirm_deletion:
                return "break"
            self.to_delete = to_delete
            self.db.delete_key(self.to_delete['name'])
            self.result.config(text=f"Deleted {self.to_delete['name']} key and its values")
        self.deletion_key.delete(0,'end')
        self.deletion_value.delete(0,'end')
        return "break"

    def handle_modification(self,event):
        new_pair={}
        if not self.modification_key.get() or not self.modification_value.get():
            showwarning(title="Invalid input",message="You must provide both key and new name")
            return "break"
        new_pair["name"] = self.modification_key.get()
        new_pair["new_name"] = self.modification_value.get()
        self.pairing = new_pair
        if self.db.modify_key(self.pairing['name'], self.pairing['new_name']) > 0:
            self.result.config(text=f"Renamed {self.pairing['name']} to {self.pairing['new_name']}")
        else:
            self.result.config(text=f"No keys named {self.pairing['name']}")
        self.modification_key.delete(0,'end')
        self.modification_value.delete(0,'end')
        return "break"
    
    def handle_exit(self,event):
        confirm = askyesno(title='Quit',
                    message='Are you sure that you want to quit?')
        if confirm:
            self.window.quit()
        return "break"

    def launch(self):
        self.window.title("Customize routes")
        self._addition_widgets(self.window)
        self._deletion_widgets(self.window)
        self._modification_widgets(self.window)
        self.result = tk.Label()
        self.result.grid(columnspan=3, row=9)
        exit_button = tk.Button(self.window, text="Quit")
        exit_button.bind("<Button-1>", self.handle_exit)
        exit_button.grid(columnspan=3, row=10)
        self.window.mainloop()
    
    def _addition_widgets(self, window):
        tk.Label(window, text="Insert new values").grid(columnspan=3,row=0)
        tk.Label(window, text="Key").grid(column=0,row=1)
        self.search_key = tk.Entry(window)
        self.search_key.grid(column=0,row=2)
        self.search_key.focus()
        tk.Label(window, text="Values (separated by comma)").grid(column=1,row=1)
        self.search_value = tk.Entry(window)
        self.search_value.grid(column=1,row=2)
        add_pair = tk.Button(window, text="Add")
        add_pair.bind("<Button-1>", self.handle_addition)
        add_pair.grid(column=2, row=2)

    def _deletion_widgets(self, window):
        tk.Label(window, text="Delete keys or values").grid(columnspan=3,row=3)
        tk.Label(window, text="Key").grid(column=0,row=4)
        self.deletion_key = tk.Entry(window)
        self.deletion_key.grid(column=0,row=5)
        self.deletion_key.focus()
        tk.Label(window, text="Values (separated by comma)").grid(column=1,row=4)
        self.deletion_value = tk.Entry(window)
        self.deletion_value.grid(column=1,row=5)
        delete_pair = tk.Button(window, text="Delete")
        delete_pair.bind("<Button-1>", self.handle_deletion)
        delete_pair.grid(column=2, row=5)
    
    def _modification_widgets(self, window):
        tk.Label(window, text="Modify key").grid(columnspan=4,row=6)
        tk.Label(window, text="Key").grid(column=0,row=7)
        self.modification_key = tk.Entry(window)
        self.modification_key.grid(column=0,row=8)
        self.modification_key.focus()
        tk.Label(window, text="New name").grid(column=1,row=7)
        self.modification_value = tk.Entry(window)
        self.modification_value.grid(column=1,row=8)
        modify_pair = tk.Button(window, text="Modify")
        modify_pair.bind("<Button-1>", self.handle_modification)
        modify_pair.grid(column=2, row=8)