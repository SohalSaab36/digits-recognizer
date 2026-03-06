# Handwritten Digit Recognizer 🧠

A simple AI project that recognizes handwritten digits using a neural network trained on the MNIST dataset.

This project allows you to:

* Train a neural network to recognize digits
* Predict digits from image files
* Draw digits with your mouse and let the AI predict them

---

## 🚀 Features

* Neural network trained on the MNIST handwritten digit dataset
* Image prediction using OpenCV
* Interactive drawing interface using Tkinter
* Lightweight Keras model (~1.4 MB)

---

## 📁 Project Structure

```
digit-recognizer-ai/
│
├── train.py           # Train the neural network
├── checkdigits.py     # Test the model on digit images
├── drawable.py        # Draw digits with mouse and predict
├── handwritten.keras  # Trained neural network model
└── digits/            # Folder containing test digit images
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/digit-recognizer-ai.git
cd digit-recognizer-ai
```

Install dependencies:

```
pip install tensorflow opencv-python numpy matplotlib pillow
```

---

## 🧠 Train the Model

```
python train.py
```

This trains the neural network using the MNIST dataset and saves the model as:

```
handwritten.keras
```

---

## 🔍 Predict Digits from Images

Place images inside the **digits** folder.

Example file names:

```
digit1.png
digit2.png
digit3.png
```

Run:

```
python checkdigits.py
```

The model will print the predicted digit.

---

## ✏️ Draw Digits with Mouse

Run:

```
python drawable.py
```

A window will open where you can **draw a digit using your mouse**, and the AI will predict it.

---

## 📚 Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Tkinter
* Matplotlib

---

## 🎯 Future Improvements

* Show prediction confidence
* Add better preprocessing for drawn digits
* Convert to a web app
* Improve model accuracy

---

## 👨‍💻 Author

Created by **SohalSaab36**
AI / ML enthusiast and programmer.

---

⭐ If you like this project, consider giving it a star!
