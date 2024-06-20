import cv2
tttt = cv2.HoughLines
ttt = cv2.HoughLinesP
# Open a connection to the video stream
cap = cv2.VideoCapture('http://192.168.0.111:81/stream')
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # Set buffer size if needed
# cap = cv2.VideoCapture(4) # 2 e 4
# ret, _ = cap.read()

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the resulting frame
    cv2.imshow('ESP32-CAM Stream', frame)

    # Exit the stream on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
