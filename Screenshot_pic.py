import tkinter as tk
from tkinter import filedialog
import pyautogui
from PIL import ImageGrab

def take_screenshot():
    screenshot = ImageGrab.grab()
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        screenshot.save(save_path)

root = tk.Tk()
root.title("Screenshot App")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack()

root.mainloop()
