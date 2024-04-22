import tkinter as tk
from tkinter import messagebox


class PlaylistCreatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Playlist Creator")
        self.name = None
        self.date = None
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Your name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.date_label = tk.Label(self, text="Which day do you want to find the best artist from? (Format YYYY-MM-DD)")
        self.date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        self.create_button = tk.Button(self, text="Create Playlist", command=self.playlist_created)
        self.create_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self, text="Delete Playlist", command=self.playlist_deleted)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def playlist_created(self):
        if self.date_entry.get() and self.name_entry.get():
            self.name = self.name_entry.get()
            self.date = self.date_entry.get()
            messagebox.showinfo("Playlist Created", f"Playlist created for {self.name} with date {self.date}")
        else:
            messagebox.showwarning("Missing Information", "Please enter both date and name before creating playlist")

    def playlist_deleted(self):
        if self.name and self.date:
            messagebox.showinfo("Playlist Deleted", f"Playlist deleted for {self.name} with date {self.date}")
        else:
            messagebox.showwarning("Playlist not created", "You have to first create playlist to delete it")
        return True

