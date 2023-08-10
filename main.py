import cv2
from camera import webcam

camera = webcam.WebcamCamera(1)


while True:
    key = cv2.waitKey(1) & 0xFF  # 1ms 대기 후 키 이벤트 처리
    if key == ord('q'):
        break  # 'q' 키를 누르면 루프 종료
    cv2.imshow("img", camera.take_photo())

cv2.destroyAllWindows()
