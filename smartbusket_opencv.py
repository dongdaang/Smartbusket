import cv2
import time


class Camera:
    def turn_on_video(self):
        self.cap = cv2.VideoCapture(0)      # 카메라 연동
        time.sleep(0.2)
        self.ret, self.frame = self.cap.read()      # 화면 캡쳐
        time.sleep(0.3)
        cv2.imwrite('product.jpg', self.frame)      # 캡쳐 화면 저장
        
        
        
# ------------------이미지 데이터 수집용-------------------
    
#     def turn_on_video(self, i):
#         print(f'{i}번째 사진')
#         self.cap = cv2.VideoCapture(0)      # 카메라 연동
#         time.sleep(0.2)
#         self.ret, self.frame = self.cap.read()      # 화면 캡쳐
#         time.sleep(0.3)
#         cv2.imwrite(f'train_data/cocacola_{i}.jpg', self.frame)      # 캡쳐 화면 저장
        
        
# for i in range(1, 201):
#     test = Camera()
#     test.turn_on_video(i)