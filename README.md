# Hand-detector-opencv
Hand Detector is a real-time computer vision application that tracks hand movements using a webcam. It identifies 21 key points on each hand, determines which fingers are raised, and displays the finger count on screen instantly.

README.md
markdown
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
Create a virtual environment 

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

🧪 Example Code
python
import cv2
from hand_module import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img)
    
    if lm_list:
        fingers = detector.fingers_up()
        finger_count = fingers.count(1)
        cv2.putText(img, f'Fingers: {finger_count}', (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
    
    cv2.imshow("Hand Detector", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
📸 Sample Output
Green dots → landmarks

Red lines → connections

Text → number of fingers detected

🔧 Customization
Change detection confidence:
HandDetector(detection_con=0.7, tracking_con=0.7)

Show/hide bounding box:
detector.find_hands(img, draw_bbox=True/False)

📌 Requirements
See requirements.txt:

text
opencv-python==4.8.1.78
mediapipe==0.10.7
numpy==1.24.3
📈 Future Improvements
Gesture recognition (peace, thumbs up, etc.)

Mouse/volume control via hand gestures

Support for multiple hands

Save detected hand images

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.


👨‍💻 Author
Srijita Ghosh
GitHub : https://github.com/srijitag448-jpg

⭐ Show Your Support
If this project helped you, please give it a ⭐ on GitHub!

text

---

    main()
