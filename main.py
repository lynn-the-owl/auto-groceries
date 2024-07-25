import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
import tkinter as tk
from utils import getPriceFromBigC


def show_price_screen(canvas, product_code):
    # Clear the canvas
    canvas.delete("all")
    price = getPriceFromBigC(product_code)

    canvas.create_text(320, 240, text=price,
                       font=("Arial", 24), fill="red")


def detect_and_display_barcode(frame, canvas):
    # Convert frame to PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Decode barcodes
    decoded_objects = decode(image)
    if decoded_objects:
        for obj in decoded_objects:

            product_code = obj.data.decode('utf-8')
            show_price_screen(canvas, product_code)
           # Stop video feed update
        return
    else:
        # Convert image to ImageTk and display it
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        canvas.image = image_tk

    # Update GUI
    root.after(10, update_frame, video_capture, canvas)


def update_frame(video_capture, canvas):
    ret, frame = video_capture.read()
    if ret:
        detect_and_display_barcode(frame, canvas)


# Set up GUI
root = tk.Tk()
root.title("Barcode Detection")

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

video_capture = cv2.VideoCapture(0)

update_frame(video_capture, canvas)

root.mainloop()
video_capture.release()
