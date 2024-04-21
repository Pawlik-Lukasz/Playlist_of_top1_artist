import tkinter as tk
from tkinter import messagebox


class PlaylistCreatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Playlist Creator")
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Your name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.date_label = tk.Label(self, text="From which date You want to search for top 1 artist? (Format YYYY-MM-DD)")
        self.date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        self.create_button = tk.Button(self, text="Create Playlist", command=self.playlist_created)
        self.create_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def playlist_created(self):
        if self.date_entry.get() and self.name_entry.get():
            name = self.name_entry.get()
            date = self.date_entry.get()
            messagebox.showinfo("Playlist Created", f"Playlist created for {name} with date {date}")
            self.quit()
            return name, date
        else:
            messagebox.showwarning("Missing Information", "Please enter both date and name before creating playlist")

