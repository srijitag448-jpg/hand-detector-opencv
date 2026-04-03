
# ✋ Hand Detector

A real-time hand detection and tracking system built with **OpenCV** and **MediaPipe**. This project detects hands in a webcam feed, draws landmarks, counts fingers, and can be extended for gesture control.



---

## 🚀 Features

- ✅ Real-time hand detection (left & right)
- ✅ 21 hand landmarks with connections
- ✅ Finger count (0–5) displayed on screen
- ✅ Bounding box around hand
- ✅ FPS counter
- ✅ Lightweight and fast

---

## 📦 Tech Stack

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

---

## 🧠 How It Works

1. **MediaPipe Hands** detects hand landmarks in each frame.
2. Landmarks are drawn using OpenCV.
3. Finger state (up/down) is determined by comparing landmark y-coordinates.
4. Total fingers counted and displayed.

---

## 📁 Project Structure
hand-detector/
│
├── hand_detector.py # Main detection script
├── hand_module.py # Reusable hand detection class
├── requirements.txt # Dependencies
├── README.md # This file


text

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/srijitag448-jpg/hand-detector-opencv.git
cd hand-detector-opencv
Create a virtual environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
🎮 Usage
Run the main script:

bash
python hand_detector.py
Press ESC or q to exit.
