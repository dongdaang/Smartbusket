import numpy as np
import pandas as pd
import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class object_detection:
    def __init__(self):
        self.IMAGE_SIZE = 224
        # self.IMAGE_SIZE = (400, 300)
        # self.new_model=tensorflow.keras.models.load_model('sojubeer_cnn1.h5')
        # self.new_model=tensorflow.keras.models.load_model('effb3_400_new1.h5')
        # self.new_model=tensorflow.keras.models.load_model('effb4_400_new1.h5')
        # self.new_model=tensorflow.keras.models.load_model('resnet_800_gen1.h5')
        # self.new_model=tensorflow.keras.models.load_model('resnet_800_gen2.h5')
        # self.new_model=tensorflow.keras.models.load_model('efficient_600_new1.h5')
        # self.new_model=tensorflow.keras.models.load_model('new_resnet_400_gen1.h5')
        # self.new_model=tensorflow.keras.models.load_model('xception_400_gen1.h5')
        # self.new_model=tensorflow.keras.models.load_model('xception_800_gen1.h5')
        # self.new_model=tensorflow.keras.models.load_model('xception_800_gen2.h5')
        # self.new_model=tensorflow.keras.models.load_model('resnet50v2_600.h5')
        # self.new_model=tensorflow.keras.models.load_model('resnet50v2_900.h5')
        # self.new_model=tensorflow.keras.models.load_model('resnet50v2_1200.h5')
        # self.new_model=tensorflow.keras.models.load_model('efficientb3_600.h5')
        # self.new_model=tensorflow.keras.models.load_model('efficientb3_900.h5')
        # self.new_model=tensorflow.keras.models.load_model('efficientb3_1200.h5')
        # self.new_model=tensorflow.keras.models.load_model('xception_600.h5')
        # self.new_model=tensorflow.keras.models.load_model('xception_900.h5')
        self.new_model=tensorflow.keras.models.load_model('xception_1200.h5')
        
        self.product = {0 : 'BEER', 1 : 'COCACOLA', 2 : 'CORNCHIP', 3 : 'HARIBO',
                        4 : 'PEPSI', 5 : 'SOJU'}
        self.test_generator = ImageDataGenerator(rescale=1/255.)
        self.test_df = pd.DataFrame({'path':['product.jpg'], 'dataset':['test'],
                        'label':['label']})
        
    def make_test_generator(self, list_frame):      # 이미지제너레이터 활용 테스트 데이터 생성
        test_flow_gen = self.test_generator.flow_from_dataframe(dataframe=self.test_df
                                            ,x_col='path'
                                            ,y_col='label'
                                            ,target_size=(self.IMAGE_SIZE, self.IMAGE_SIZE)
                                            # ,target_size=self.IMAGE_SIZE
                                            ,class_mode='categorical'
                                            ,shuffle=False
                                            )
        
        list_frame.update()
        return test_flow_gen


    def predict_test_df(self, list_frame):      # 예측 함수
        list_frame.update()
        test_flow_gen = self.make_test_generator(list_frame)
        predict = self.new_model.predict_generator(test_flow_gen)
        print(test_flow_gen.class_indices)
        print(predict)
        thr_score = 0.85     # threshold score : 0.85
        if max(predict[0]) >= thr_score:        # softmax가 threshold score보다 높을 경우만 해당 물품 반환
            idx = np.argmax(predict[0])
            return self.product[idx]
                
        return False        # threshold score보다 낮을 경우 False 반환