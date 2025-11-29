import sys
import os
import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller --onefile.
    """
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def create_qr_image(data, size=(280, 250)):
    """
    Return a PIL image of the QR code resized to `size`.
    """
    img = qrcode.make(data)
    return img.resize(size)


def createQR(event=None):
    data = text_entry.get().strip()
    if data:
        res_img = create_qr_image(data)
        tkimage = ImageTk.PhotoImage(res_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        # keep reference so image isn't garbage-collected
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Warning", "Enter Data in Entry First")


def saveQR(event=None):
    data = text_entry.get().strip()
    if data:
        res_img = create_qr_image(data)
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if path:
            try:
                res_img.save(path)
                messagebox.showinfo("Success", "QR Code is Saved")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")
    else:
        messagebox.showwarning("Warning", "Enter Data in Entry First")


def main():
    global root, qr_canvas, text_entry

    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("300x380")
    root.config(bg="white")
    root.resizable(False, False)

    frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
    frame1.place(x=10, y=5, width=280, height=250)

    frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    frame2.place(x=10, y=260, width=280, height=100)

    # Try to load cover image; if not available, create a blank white image.
    cover_path = resource_path("qr.png")
    try:
        cover_pil = Image.open(cover_path).convert("RGBA")
        cover_pil = cover_pil.resize((280, 250))
    except Exception:
        cover_pil = Image.new("RGBA", (280, 250), (255, 255, 255, 255))

    coverImg = ImageTk.PhotoImage(cover_pil)

    qr_canvas = tk.Canvas(frame1, width=280, height=250)
    qr_canvas.create_image(0, 0, anchor=tk.NW, image=coverImg)
    qr_canvas.image = coverImg  # keep reference
    qr_canvas.bind("<Double-1>", saveQR)
    qr_canvas.pack(fill=tk.BOTH, expand=True)

    text_entry = ttk.Entry(frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
    text_entry.bind("<Return>", createQR)
    text_entry.place(x=5, y=5)

    btn_1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
    btn_1.place(x=25, y=50)

    btn_2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
    btn_2.place(x=100, y=50)

    btn_3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
    btn_3.place(x=175, y=50)

    root.mainloop()


if __name__ == "__main__":
    main()
