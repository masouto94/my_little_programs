from typing import Type
from files_organizer.data_abm import DatabaseConnector
import tkinter as tk
import tkinter.ttk as ttk

class InterfaceParser():
    def __init__(self, db:Type[DatabaseConnector]) -> None:
        self._pairing = {}
        self.db =db

    @property
    def pairing(self):
        return self._pairing
    
    @pairing.setter
    def pairing(self, val):
        self._pairing = val

    def parse_input_values(self,input):
        stripped=input.strip()
        if stripped[0] != '.':
            return '.'+stripped
        return stripped
    
    def handle_addition(self,event):
        new_pair={}
        new_pair["name"]=self.search_key.get()
        new_pair["values"]= list(map(self.parse_input_values, self.search_value.get().split(',')))
        self.pairing = new_pair
        self.db.new_pairing_batch(self.pairing['name'], self.pairing['values'])
        self.result.config(text=f"Added pairings for {self.search_key}")
        self.search_key.delete(0,'end')
        self.search_value.delete(0,'end')

    def handle_deletion(self,event):
        to_delete={}
        print(to_delete)

    def launch(self):
        window = tk.Tk()
        window.title("Customize routes")
        self._addition_widgets(window)
        self._deletion_widgets(window)
        self.result = tk.Label()
        self.result.grid(columnspan=3, row=6)
        window.mainloop()
    
    def _addition_widgets(self, window):
        tk.Label(window, text="New values input").grid(columnspan=3,row=0)
        tk.Label(window, text="Key").grid(column=0,row=1)
        self.search_key = tk.Entry(window)
        self.search_key.grid(column=0,row=2)
        self.search_key.focus()
        tk.Label(window, text="Values (separated by comma)").grid(column=1,row=1)
        self.search_value = tk.Entry(window)
        self.search_value.grid(column=1,row=2)
        add_pair = tk.Button(window, text="add")
        add_pair.bind("<Button-1>", self.handle_addition)
        add_pair.grid(column=2, row=2)

    def _deletion_widgets(self, window):
        tk.Label(window, text="To delete").grid(columnspan=3,row=3)
        tk.Label(window, text="Key").grid(column=0,row=4)
        self.deletion_key = tk.Entry(window)
        self.deletion_key.grid(column=0,row=5)
        self.deletion_key.focus()
        tk.Label(window, text="Values (separated by comma)").grid(column=1,row=4)
        self.deletion_value = tk.Entry(window)
        self.deletion_value.grid(column=1,row=5)
        delete_pair = tk.Button(window, text="delete")
        delete_pair.bind("<Button-1>", self.handle_deletion)
        delete_pair.grid(column=2, row=5)
