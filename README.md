# ✋ Hand Detector

A real-time hand detection and tracking system built with **OpenCV** and **MediaPipe**. This project detects hands in a webcam feed, draws landmarks, counts fingers, and can be extended for gesture control.

![Demo](https://via.placeholder.com/800x400?text=Hand+Detection+Demo)  
*(Replace with actual GIF/screenshot)*

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
