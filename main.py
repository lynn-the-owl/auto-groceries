import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
import tkinter as tk
from utils import get_price_and_product_title_from_big_c

# Global variable to track if a barcode has been detected
barcode_detected = False


def show_price_screen(canvas, product_code):
    global barcode_detected
    barcode_detected = True

    # Clear the canvas
    canvas.delete("all")
    price = get_price_and_product_title_from_big_c(product_code)

    canvas.create_text(320, 240, text=price, font=("Arial", 24), fill="red")

    # Add a "Scan Another" button
    button = tk.Button(root, text="Scan Another",
                       command=lambda: reset_camera_view(video_capture, canvas))
    button_window = canvas.create_window(
        320, 320, anchor=tk.CENTER, window=button)


def detect_and_display_barcode(frame, canvas):
    # Convert frame to PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Decode barcodes
    decoded_objects = decode(image)
    if decoded_objects:
        for obj in decoded_objects:
            product_code = obj.data.decode('utf-8')
            show_price_screen(canvas, product_code)
        return
    else:
        # Convert image to ImageTk and display it
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        canvas.image = image_tk

    # Update GUI if no barcode detected
    if not barcode_detected:
        root.after(10, update_frame, video_capture, canvas)


def update_frame(video_capture, canvas):
    if not barcode_detected:
        ret, frame = video_capture.read()
        if ret:
            detect_and_display_barcode(frame, canvas)


def reset_camera_view(video_capture, canvas):
    global barcode_detected
    barcode_detected = False
    canvas.delete("all")
    update_frame(video_capture, canvas)


# Set up GUI
root = tk.Tk()
root.title("Barcode Detection")

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

video_capture = cv2.VideoCapture(0)

update_frame(video_capture, canvas)

root.mainloop()
video_capture.release()
