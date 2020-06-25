import tkinter as tk
from tkinter import filedialog, Text
import os

# The main frame
root = tk.Tk()
apps=[]

# To rectify any redundancy
if os.path.isfile("save.txt"):
    with open("save.txt", 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        # remove white spaces from the text file
        apps = [x for x in tempApps if x.strip()]


# The method to select any app
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables",  "*.exe"), ("all files", "*.*")))

    # Adding app to the canvas frame
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="teal")
        label.pack()


# The method to run the selected app
def runApp():
    for app in apps:
        os.startfile(app)


 # The canvas
canvas = tk.Canvas(root, height=620, width=400, bg="#184d47")

# Generating the canvas
canvas.pack()

# Ataching a frame to it
frame = tk.Frame(root, bg="white")

# Placing the frame into the center of the canvas
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

# Adding a button to open files
openFile = tk.Button(root, padx=10, pady=5, text="Open File", fg="white", bg="#254d47", command=addApp)
openFile.pack()

# Adding a button to run apps
runApps = tk.Button(root, padx=10, pady=5, text="Run Apps", fg="white", bg="#254d47", command=runApp)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Each time an app is open it saves a text file of it to luanch it in the next boot
with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")