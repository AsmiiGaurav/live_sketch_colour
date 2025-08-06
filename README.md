# 🖌️ Live Sketching & Coloring App

This is a fun and interactive computer vision project built using Python. It allows you to:

- 📸 Capture a live photo using your device’s webcam
- ✏️ Automatically convert the photo into a coloring book-style sketch using edge detection
- 🎨 Use your keyboard to paint the sketch with various colors using your mouse

---

##  Demo

<!-- Add your GIF or screenshot after running the project -->
![demo](https://user-images.githubusercontent.com/yourusername/demo.gif)

---

##  Features

- Real-time sketch generation with webcam input
- Clean edge-based sketch output like in coloring books
- Simple coloring tool using Pygame
- Keyboard-based color selection
- Saves final sketch and colored image locally

---

## 🧰 Technologies Used

- **Python 3**
- **OpenCV** – for webcam input and edge detection
- **Pygame** – for interactive coloring

---

## 🚀 Getting Started

### 1. Clone the repository

bash

git clone https://github.com/AsmiiGaurav/live-sketching-coloring-app.git
cd live-sketching-coloring-app

## Install dependencies

pip install opencv-python pygame

## Run the app

python main.py

## 🎮 Controls

| Key / Action             | Function                            |
|--------------------------|-------------------------------------|
| `Enter`                 | Capture photo and generate sketch   |
| `Left Mouse Button`     | Click and drag to draw on the sketch |
| `R`                     | Change brush color to Red           |
| `G`                     | Change brush color to Green         |
| `B`                     | Change brush color to Blue          |
| `Y`                     | Change brush color to Yellow        |
| `C`                     | Change brush color to Cyan          |
| `M`                     | Change brush color to Magenta       |
| `O`                     | Change brush color to Orange        |
| `P`                     | Change brush color to Purple        |
| `K`                     | Change brush color to Black         |
| `W`                     | Change brush color to White         |
| Window Close (`X` icon) | Save colored image and exit         |

## Future Improvements

- Add brush size adjustment (small, medium, large)
- Implement undo/redo features for coloring
- Support loading previously saved sketches for later coloring
- Add touchscreen support for tablets and phones
- Build a user-friendly UI for sketch capture and color selection using a GUI framework (e.g., Tkinter, PyQt, or a web-based UI)

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, feel free to open an issue or pull request.

