import cv2

cap = cv2.VideoCapture(0)  # 0 for webcam, or provide a video path
if not cap.isOpened():
    print("Error: Could not open video capture")
    exit()
count = 0
back_ground = None
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print("Error converting frame to grayscale:", str(e))
        break

    if count == 10 and back_ground is None:
        back_ground = gray.copy()

    # Background subtraction
    if count > 10 and back_ground is not None:
        diff = cv2.absdiff(back_ground, gray)  # Calculate the absolute difference
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)  # Thresholding
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Find contours
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter small contours
                x, y, w, h = cv2.boundingRect(contour)  # Get bounding box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Frame', frame)
    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
