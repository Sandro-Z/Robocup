import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("摄像头无法打开！")
        break
    cv2.imshow("Capture", frame)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
