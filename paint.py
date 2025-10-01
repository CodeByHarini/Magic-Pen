import cv2
import numpy as np
import mediapipe as mp
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

canvas = None
brush_color = (0, 0, 255)
brush_size = 8
eraser_size = 40
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 255)]
prev_index = None
prev_pinky = None

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot access camera")
    exit()

# Color palette
palette_start_x = 20
palette_start_y = 20
palette_size = 50
palette_spacing = 20

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Draw color palette
    for i, color in enumerate(colors):
        x = palette_start_x + i * (palette_size + palette_spacing)
        y = palette_start_y
        cv2.rectangle(frame, (x, y), (x + palette_size, y + palette_size), color, -1)
        if brush_color == color:
            cv2.rectangle(frame, (x-2, y-2), (x + palette_size+2, y + palette_size+2), (255,255,255), 2)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            h, w, c = frame.shape
            landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]

            index_x, index_y = landmarks[8]
            index_pip_y = landmarks[6][1]
            pinky_x, pinky_y = landmarks[20]
            pinky_pip_y = landmarks[18][1]

            # Check if index finger is touching a color box
            for i, color in enumerate(colors):
                x = palette_start_x + i * (palette_size + palette_spacing)
                y = palette_start_y
                if x <= index_x <= x + palette_size and y <= index_y <= y + palette_size:
                    brush_color = color

            # PRIORITY: Pinky erases first
            if pinky_y < pinky_pip_y:
                if prev_pinky is None:
                    prev_pinky = (pinky_x, pinky_y)
                cv2.line(canvas, prev_pinky, (pinky_x, pinky_y), (0,0,0), eraser_size)
                prev_pinky = (pinky_x, pinky_y)
                prev_index = None  # prevent index from drawing
            # Else draw with index finger only
            elif index_y < index_pip_y and index_y > palette_start_y + palette_size:
                if prev_index is None:
                    prev_index = (index_x, index_y)
                cv2.line(canvas, prev_index, (index_x, index_y), brush_color, brush_size)
                prev_index = (index_x, index_y)
            else:
                prev_index = None
                prev_pinky = None

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    frame = cv2.bitwise_or(frame, canvas)
    cv2.imshow("Virtual Painter", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows() 