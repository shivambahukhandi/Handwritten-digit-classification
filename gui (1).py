from tkinter import *
import win32gui
from PIL import ImageGrab,Image
import tkinter.messagebox
import tensorflow as tf

def clear():
    canvas.delete("all")

def predict():
    x0 = canvas.winfo_rootx() + 8
    y0 = canvas.winfo_rooty() + 3
    x1 = x0 + 425
    y1 = y0 + 470

    img = ImageGrab.grab((x0, y0, x1, y1))
    plt.imshow(img)
    img = img.resize((28, 28)).convert("L")
    img = np.array(img)
    img = img.reshape((1, 28, 28, 1))
    img = img / 255.0
    value = np.argmax(model.predict(img))
    tkinter.messagebox.showinfo("Prediction", "it's a " + str(value))

def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw(event):
    global lasx, lasy
    canvas.create_oval((lasx, lasy, event.x, event.y), 
                      fill='white', outline='white', 
                      width=15)
    lasx, lasy = event.x, event.y



model = tf.keras.models.load_model("model.h5")
window = Tk()
window.geometry("350x400+1+1")
window.title("Character Recognization.")

canvas = Canvas(window, bg='black',height="370",width="340")
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw)

button_frame = tk.Frame(window)
clear_button = tk.Button(button_frame, text="Clear", command=clear)
predict_button = tk.Button(button_frame, text="Predict", command=predict)

canvas.pack(expand= FALSE)
clear_button.pack(side="left")
predict_button.pack(side="right")
button_frame.pack(side = "bottom")

window.mainloop()	