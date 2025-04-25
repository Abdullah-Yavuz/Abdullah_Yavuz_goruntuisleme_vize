
"""
Abdullah Yavuz - Görüntü İşleme Vize Projesi
Bu proje, MediaPipe kullanarak gerçek zamanlı el takibi ve bir çöp toplama oyunu içerir.
"""

import cv2
import mediapipe as mp
import random
import time
import math

# MediaPipe eller modülü başlatılır
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Kamera başlatılır
cap = cv2.VideoCapture(0)

# Oyun için başlangıç verileri
score = 0
obj_radius = 30
obj_x = random.randint(100, 500)
obj_y = random.randint(100, 400)
last_hit_time = time.time()

def is_touching(x1, y1, x2, y2, radius):
    """
    İki nokta arasındaki mesafenin belirli bir yarıçap içinde olup olmadığını kontrol eder.
    """
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance < radius

def draw_hand_landmarks(img, hand_landmarks):
    """
    Tespit edilen el üzerindeki anahtar noktaları çiz.
    """
    mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

def update_game_object():
    """
    Çöp nesnesini rastgele bir konuma yeniden yerleştir.
    """
    return random.randint(100, 500), random.randint(100, 400)

def main():
    global score, obj_x, obj_y, last_hit_time

    while True:
        success, img = cap.read()
        if not success:
            break

        # Görüntüyü çevir ve BGR'den RGB'ye çevir
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        h, w, _ = img.shape

        # Çöp nesnesi çizilir
        cv2.circle(img, (obj_x, obj_y), obj_radius, (0, 255, 255), -1)

        # El tespiti yapıldıysa
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                draw_hand_landmarks(img, hand_landmarks)

                # İşaret parmağı ucu koordinatları alınır
                index_finger_tip = hand_landmarks.landmark[8]
                finger_x = int(index_finger_tip.x * w)
                finger_y = int(index_finger_tip.y * h)

                # Temas kontrolü
                if is_touching(finger_x, finger_y, obj_x, obj_y, obj_radius):
                    current_time = time.time()
                    if current_time - last_hit_time > 1:
                        score += 1
                        obj_x, obj_y = update_game_object()
                        last_hit_time = current_time

        # Skor gösterilir
        cv2.putText(img, f"Skor: {score}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)

        # Görüntü gösterilir
        cv2.imshow("Cop Toplama Oyunu", img)

        # Çıkmak için 'q' tuşuna basılır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
