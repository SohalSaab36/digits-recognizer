import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf
import cv2

# load trained model
model = tf.keras.models.load_model("handwritten.keras")

# canvas size
width = 280
height = 280

# create window
window = tk.Tk()
window.title("Draw a Digit")

canvas = tk.Canvas(window, width=width, height=height, bg="black")
canvas.pack()

# PIL image (for processing)
image = Image.new("L", (width, height), "black")
draw = ImageDraw.Draw(image)

def draw_lines(event):
    x, y = event.x, event.y
    r = 8

    canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
    draw.ellipse([x-r, y-r, x+r, y+r], fill="white")

canvas.bind("<B1-Motion>", draw_lines)

def predict_digit():

    img = np.array(image)

    # resize to MNIST format
    img = cv2.resize(img, (28,28))

    # normalize
    img = img / 255.0

    img = np.array([img])

    prediction = model.predict(img)

    digit = np.argmax(prediction)

    print("Prediction:", digit)

def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0,0,width,height], fill="black")

predict_btn = tk.Button(window, text="Predict", command=predict_digit)
predict_btn.pack()

clear_btn = tk.Button(window, text="Clear", command=clear_canvas)
clear_btn.pack()

window.mainloop()
