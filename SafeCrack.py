import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry
import hashlib


# Function to create an MD5 hash of the password
def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()


# Custom popup dialog class
class CustomPopup(Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        self.transient(parent)  # Set to be a transient window of the main application
        self.geometry("300x150")  # Window size
        self.configure(bg="lightgray")

        # Center the window over the parent
        self.update_idletasks()  # Update the geometry of the widget
        x = parent.winfo_x() + (parent.winfo_width() // 2) - (self.winfo_width() // 2)
        y = parent.winfo_y() + (parent.winfo_height() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")  # Set the position

        # Message
        Label(
            self,
            text=message,
            font=("Calibri", 12),
            wraplength=280,
            bg="lightgray",
            fg="black",
        ).pack(pady=20, padx=10)

        # Close button
        close_button = Button(self, text="Close", command=self.destroy)
        close_button.pack(pady=10)
        close_button.focus_set()  # Set focus on the close button
        self.bind(
            "<Return>",
            lambda event: self.destroy(),  # Bind Return key to destroy the popup
        )


# Function to display the popup
def show_popup(message, title="Info"):
    popup = CustomPopup(root, title, message)
    popup.grab_set()  # Grab all events
    root.wait_window(popup)  # Wait for the popup to close


# Function to check the password entered by the user
def check_password(event=None):
    if password_entry.get() == "YOURPASSWORDHERE":
        show_popup(
            "You have uncovered the password to the safe. Pass this message on to the cyberteam to let them know you cracked it. Send 'For all that is sacred and holy' to <Your Email Address here>",
            "Success",
        )
    else:
        show_popup("Try again", "Incorrect")


# Setting up the main window
root = tk.Tk()
root.title("SafeCracker2k24")

# Optionally set an icon if the file is available
# root.iconbitmap('path_to_your_icon.icns')  # Uncomment and adjust the path as necessary

root.configure(bg="gray")

# Center the window on the screen
window_width = 300
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Password entry with character limit
password_entry = Entry(root, font=("Arial", 14), show="*")
password_entry.pack(pady=20)
password_entry.focus_set()
password_entry.bind(
    "<Return>", check_password
)  # Bind the Return key to check_password function

# Restrict the number of characters to 64
password_var = tk.StringVar()
password_entry.config(textvariable=password_var)


def on_write(*args):
    value = password_var.get()
    if len(value) > 64:
        password_var.set(value[:64])


password_var.trace("w", on_write)

# Submit button
submit_button = Button(root, text="Unlock Safe", command=check_password)
submit_button.pack()

# Displaying the MD5 hash of the password
hash_label = Label(root, text=md5_hash("YOURPASSWORDHERE"), bg="gray")
hash_label.pack(side="bottom")

# Run the GUI
root.mainloop()
