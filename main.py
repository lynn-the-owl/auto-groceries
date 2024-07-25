import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
import tkinter as tk


def detect_and_display_barcode(frame, canvas):
    # Convert frame to PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Decode barcodes
    decoded_objects = decode(image)
    for obj in decoded_objects:
        print(f"Type: {obj.type}")
        print(f"Data: {obj.data.decode('utf-8')}")

    # Convert image to ImageTk
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
