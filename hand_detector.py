import cv2
from hand_module import HandDetector

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    
    while True:
        success, img = cap.read()
        if not success:
            break
            
        img = detector.find_hands(img)
        lm_list = detector.find_position(img)
        
        if lm_list:
            detector.lm_list = lm_list
            fingers = detector.fingers_up()
            total = fingers.count(1)
            
            cv2.putText(img, f'Fingers: {total}', (10, 70),
                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        
        cv2.imshow("Hand Detector", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()