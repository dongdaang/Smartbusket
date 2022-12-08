from tkinter import *
import tkinter.font
import smartbusket_opencv
import smartbusket_object_detection
import time
from datetime import datetime

class Smartbusket_gui:
    def __init__(self):                         # 프로그램 시작과 동시에 실행
        before = datetime.now()
        self.root = Tk()                        # GUI 틀 생성
        self.root.title('Smartbusket')
        self.root.geometry('800x480')
        self.root.resizable(False, False)
        self.root.configure(bg='#BCEAD5')
        
        self.title_frame = Frame(self.root)     # 프로그램 제목 프레임
        self.title_frame.pack(padx=5, pady=5)
        self.title_frame.configure(bg='#BCEAD5')
        
        title_font = tkinter.font.Font(family='맑은 고딕', size=45)
        title = Label(self.title_frame, text='스마트 장바구니', font=title_font, height=4)      # 프로그램 제목
        title.pack(fill='x', padx=5, pady=5)
        title.configure(bg='#BCEAD5')
        
        self.btn_frame = Frame(self.root)       # 시작 버튼 프레임
        self.btn_frame.pack(padx=5, pady=5)
        self.btn_frame.configure(bg='#BCEAD5')
        
        start_btn = Button(self.btn_frame, bg='#DEF5E5', text='쇼핑 시작', command=self.program_start, width=10, height=2)    # 시작 버튼, 버튼 클릭 시 self.program_start 실행
        start_btn.pack(padx=5, pady=5)
        
        self.product_price = {'BEER' : 2100, 'COCACOLA' : 1600, 'CORNCHIP' : 1500, 'HARIBO' : 2000, 
                              'PEPSI' : 1700, 'SOJU' : 1800}       # 물품 가격 데이터
        self.product_count = {'BEER' : 0, 'COCACOLA' : 0, 'CORNCHIP' : 0, 'HARIBO' : 0, 
                              'PEPSI' : 0, 'SOJU' : 0}                 # 물품 갯수 데이터
        self.detection = smartbusket_object_detection.object_detection()                      # 객체 인식 모델 및 초기 데이터 생성
        
        after = datetime.now()
        print(f'로딩 시간 : {after - before}초')
        self.root.mainloop()
        
    
    def start_display(self):        # 프로그램 시작 화면 실행 함수
        self.list_frame.destroy()
        self.btn_price_frame.destroy()
        
        self.title_frame = Frame(self.root)
        self.title_frame.configure(bg='#BCEAD5')
        self.title_frame.pack(padx=5, pady=5)
        
        title_font = tkinter.font.Font(family='맑은 고딕', size=30)
        title = Label(self.title_frame, text='잠시만 기다려 주십시오.', font=title_font, height=6)
        title.configure(bg='#BCEAD5')
        title.pack(fill='x', padx=5, pady=5)
        title.update()
        for _ in range(4):
            time.sleep(0.7)
            title.config(text='잠시만 기다려 주십시오.')
            title.update()
            time.sleep(0.7)
            title.config(text='잠시만 기다려 주십시오..')
            title.update()
            time.sleep(0.7)
            title.config(text='잠시만 기다려 주십시오...')
            title.update()
        self.detection = smartbusket_object_detection.object_detection()
        title.config(text='스마트 장바구니')
        
        self.btn_frame = Frame(self.root)
        self.btn_frame.configure(bg='#BCEAD5')
        self.btn_frame.pack(padx=5, pady=5)
        
        start_btn = Button(self.btn_frame, text='시작', command=self.program_start, width=10, height=2)
        start_btn.pack(padx=5, pady=5)
        
        self.product_price = {'BEER' : 2100, 'COCACOLA' : 1600, 'CORNCHIP' : 1500, 'HARIBO' : 2000,
                              'PEPSI' : 1700, 'SOJU' : 1800}
        self.product_count = {'BEER' : 0, 'COCACOLA' : 0, 'CORNCHIP' : 0, 'HARIBO' : 0,
                              'PEPSI' : 0, 'SOJU' : 0}
        
    
    def program_start(self):            # 프로그램 메인 함수
        self.title_frame.destroy()
        self.btn_frame.destroy()
        
        self.camera_on = True
        
        # --------------------------물품 목록 창-----------------------------------
        self.list_frame = Frame(self.root)
        self.list_frame.pack(fill='x', padx=5, pady=5)
        self.list_frame.configure(bg='#BCEAD5')
        
        self.list_name_font = tkinter.font.Font(family='맑은 고딕', size=20)
        self.list_name = Label(self.list_frame, text='물품 목록', font=self.list_name_font)
        self.list_name.pack(fill='x', padx=5, pady=5)
        self.list_name.configure(bg='#BCEAD5')
        
        product_listbox_scrollbar = Scrollbar(self.list_frame)
        product_listbox_scrollbar.pack(side='right', fill='y')
        
        product_font = tkinter.font.Font(family='맑은 고딕', size=18)
        self.listbox_name = Listbox(self.list_frame, bg='#DEF5E5', selectmode='extended', width=18, height=8, font=product_font, yscrollcommand=product_listbox_scrollbar.set)
        self.listbox_name.pack(side='left', padx=0)
        
        self.listbox_price = Listbox(self.list_frame, bg='#DEF5E5', selectmode='extended', width=18, height=8, font=product_font, yscrollcommand=product_listbox_scrollbar.set)
        self.listbox_price.pack(side='left', padx=0)
        
        self.listbox_cnt = Listbox(self.list_frame, bg='#DEF5E5', selectmode='extended', width=18, height=8, font=product_font, yscrollcommand=product_listbox_scrollbar.set)
        self.listbox_cnt.pack(side='left', padx=0)
        # --------------------------------------------------------------------------
        
        # ------------------------버튼, 가격 표시줄----------------------------------
        self.btn_price_frame = Frame(self.root)
        self.btn_price_frame.pack(fill='x', padx=5, pady=5)
        self.btn_price_frame.configure(bg='#BCEAD5')
        
        self.end_btn = Button(self.btn_price_frame, bg='#DEF5E5', text='쇼핑 종료', command=self.program_end, width=7, height=2) # 쇼핑 종료 버튼, 버튼 클릭 시 self.program_end 실행
        self.end_btn.pack(side='right', padx=5, pady=5)
        
        self.delete_product_btn = Button(self.btn_price_frame, bg='#DEF5E5', text='물품 삭제', command=self.delete_product, width=7, height=2) # 물품 삭제 버튼, 버튼 클릭 시 self.delete_product 실행
        self.delete_product_btn.pack(side='right', padx=20, pady=3)
        
        price_font = tkinter.font.Font(family='맑은 고딕', size=20)
        price_label = Label(self.btn_price_frame, text='총 가격', width=7, font=price_font)
        price_label.pack(side='left', padx=(150, 5), pady=5)
        price_label.configure(bg='#BCEAD5')
        
        self.price_entry = Entry(self.btn_price_frame, state='normal', font=price_font)
        self.price_entry.configure(bg='#BCEAD5')
        self.price_entry.delete(0, END)
        self.price_entry.insert(0, 0)
        self.price_entry.config(state='readonly')
        self.price_entry.pack(side='left', padx=5, pady=5)
        # ----------------------------------------------------------------------------
        
        self.take_pic()     # 사진 캡쳐 함수 실행
        
    
    def success(self, total, product, cnt): # 디버깅용 함수
        total += 1
        if product:
            if product == 'BEER':
                cnt['BEER'] += 1
            elif product == 'COCACOLA':
                cnt['COCACOLA'] += 1
            elif product == 'CORNCHIP':
                cnt['CORNCHIP'] += 1
            elif product == 'HARIBO':
                cnt['HARIBO'] += 1
            elif product == 'PEPSI':
                cnt['PEPSI'] += 1
            else:
                cnt['SOJU'] += 1
        
        return total, cnt
        
    
    def take_pic(self):     # 사진 캡쳐 시작
        self.list_frame.update()    # 물품 목록 창 업데이트
        total = 0
        cnt = {'BEER' : 0, 'COCACOLA' : 0, 'CORNCHIP' : 0, 'HARIBO' : 0,
                              'PEPSI' : 0, 'SOJU' : 0}
        while self.camera_on:
            camera = smartbusket_opencv.Camera()    # 카메라 연동
            camera.turn_on_video()                  # 화면 캡쳐
            before = datetime.now()
            product = self.detection.predict_test_df(self.list_frame)     # 객체 인식, product = 해당 물체
            after = datetime.now()
            if product:
                self.add_product(product)       # 물체 존재 하면 self.add_product(물품 추가) 함수 실행
            self.list_frame.update()
            total, cnt = self.success(total, product, cnt)
            print(f'전체 사진 수 : {total}\n{cnt}')
            print(f'분류 시간 : {after - before}초')
            time.sleep(0.5)
                
        
    def add_product(self, product):         # 물품 추가 함수
        if self.product_count[product] == 0:
            self.product_count[product] += 1
            self.listbox_name.insert(END, product)
            self.listbox_price.insert(END, self.product_price[product])
            self.listbox_cnt.insert(END, self.product_count[product])
        else:
            self.product_count[product] += 1
            for i in range(self.listbox_name.size()):
                if self.listbox_name.get(i, i + 1)[0] == product:
                    self.listbox_price.delete(i, i)
                    self.listbox_cnt.delete(i, i)
                    self.listbox_price.insert(i, self.product_price[product] * self.product_count[product])
                    self.listbox_cnt.insert(i, self.product_count[product])
        
        self.put_total_price()      # 총 가격 입력 함수
    
    
    def delete_product(self):       # 물품 삭제 함수
        idx = self.listbox_name.curselection()[0]
        name = self.listbox_name.get(idx)
        price = self.listbox_price.get(idx)
        cnt = self.listbox_cnt.get(idx)

        if name == 'BEER' :
            self.product_count['BEER'] -= 1
        elif name == 'COCACOLA' :
            self.product_count['COCACOLA'] -= 1
        elif name == 'CORNCHIP' :
            self.product_count['CORNCHIP'] -= 1
        elif name == 'HARIBO' :
            self.product_count['HARIBO'] -= 1
        elif name == 'PEPSI' :
            self.product_count['PEPSI'] -= 1
        elif name == 'SOJU' :
            self.product_count['SOJU'] -= 1
            
        if int(cnt) == 1:
            self.listbox_name.delete(idx, idx)
            self.listbox_price.delete(idx, idx)
            self.listbox_cnt.delete(idx, idx)
        else:
            self.listbox_name.delete(idx, idx)
            self.listbox_price.delete(idx, idx)
            self.listbox_cnt.delete(idx, idx)
            
            self.listbox_name.insert(idx, name)
            self.listbox_price.insert(idx, int(price - (price / cnt)))
            self.listbox_cnt.insert(idx, cnt - 1)
        
        self.put_total_price()
        

    def put_total_price(self):      # 총 가격 입력 함수
        total_price = self.calculate_price()
        
        self.price_entry.config(state='normal')
        self.price_entry.delete(0, END)
        self.price_entry.insert(0, total_price)
        self.price_entry.config(state='readonly')
    
    
    def calculate_price(self):      # 총 가격 계산 함수
        total_beer_price = self.product_price['BEER'] * self.product_count['BEER']
        total_cocacola_price = self.product_price['COCACOLA'] * self.product_count['COCACOLA']
        total_cornchip_price = self.product_price['CORNCHIP'] * self.product_count['CORNCHIP']
        total_haribo_price = self.product_price['HARIBO'] * self.product_count['HARIBO']
        total_pepsi_price = self.product_price['PEPSI'] * self.product_count['PEPSI']
        total_soju_price = self.product_price['SOJU'] * self.product_count['SOJU']
        
        total_price = total_beer_price + total_cocacola_price + total_cornchip_price + total_haribo_price + \
             total_pepsi_price +  total_soju_price
        
        return total_price
    
    
    def program_end(self):          # 쇼핑 종료 화면 출력
        self.list_name.config(text='감사합니다.\n고객님의 구매내역입니다.')
        self.end_btn.config(text='처음으로', command=self.start_display)
        self.delete_product_btn.destroy()
        self.camera_on = False


start = Smartbusket_gui()