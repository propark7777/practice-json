import requests
import json
from tkinter import *
import time
import tkinter.messagebox as msgbox
import upbit_method

root = Tk()
root.title("알리미")
root.geometry("1200x800")

row_index = 0
column_index =0
# ticker_list = ["QKC","SOL","BTC"]
volum_list_now =[] #5분봉 현재 거래량 
volum_list_before =[] #5분봉 이전 5분 거래량
volum_list_hour = [] #5분봉 1시간 누적 거래량
volum_hour = 0
volum_list_avg = [] #5분봉 1시간 평균 거래량
volum_ticker_now = []
tickers_krw = upbit_method.get_tickers_kwr()

running = True # 버튼 실행 함수 시작/정지
print(tickers_krw)


for ticker in tickers_krw:
    
    url = "https://api.upbit.com/v1/candles/minutes/5?market=KRW-{}&count=13".format(ticker)

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers)
    jsonObject = response.text
    
    info = json.loads(jsonObject)
    
    volum_list_now.append(info[0]["candle_acc_trade_volume"])
    volum_list_before.append(info[1]["candle_acc_trade_volume"])
    for k in range(1,13):
        volum_hour += info[k]["candle_acc_trade_volume"]
    volum_avg = volum_hour/12
    volum_list_hour.append(volum_hour)
    volum_list_avg.append(volum_avg)
    volum_hour = 0

for i in range(0,3):
    for j in range(0,3):
        if j == 0 :
            print(tickers_krw)
            label_ticker = Label(root, text=tickers_krw[i] , borderwidth= 3, relief= "solid", width= 10, height= 2)
            label_ticker.grid(row= i, column= j)
        elif j ==1 :
            label_volum_now = Label(root, text=volum_list_now[i] , borderwidth= 3, relief= "solid", width= 30, height= 2)
            label_volum_now.grid(row= i, column= j)
        elif j ==2 :
            label_volum_avg = Label(root, text=volum_list_avg[i] , borderwidth= 3, relief= "solid", width= 30, height= 2)
            label_volum_avg.grid(row= i, column= j)

def start_vol_check():
    volum_ticker_now = []
    volum_ticker_avg = []
    
    for ticker in tickers_krw:
        
        url = "https://api.upbit.com/v1/candles/minutes/5?market=KRW-{}&count=13".format(ticker)

        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)
        jsonObject = response.text
        
        info = json.loads(jsonObject)
        
        volum_list_now =[] #5분봉 현재 거래량 
        volum_list_before =[] #5분봉 이전 5분 거래량
        volum_list_hour = [] #5분봉 1시간 누적 거래량
        volum_hour = 0
        volum_list_avg = [] #5분봉 1시간 평균 거래량
        inner_list_now = []
        inner_list_avg = []
        
        inner_list_now.append(ticker)
        inner_list_now.append(info[0]["candle_acc_trade_volume"])
        volum_ticker_now.append(inner_list_now)
        
        volum_list_now.append(info[0]["candle_acc_trade_volume"])
        volum_list_before.append(info[1]["candle_acc_trade_volume"])
            
        for k in range(1,13):
            volum_hour += info[k]["candle_acc_trade_volume"]
        volum_avg = volum_hour/12
        volum_list_hour.append(volum_hour)
        volum_list_avg.append(volum_avg)
        volum_hour = 0
        
        inner_list_avg.append(ticker)
        inner_list_avg.append(volum_list_avg[0])
        volum_ticker_avg.append(inner_list_avg)
        
        # print("*******************")
        # print(ticker,volum_list_now)
        # print(ticker,volum_list_avg)
        # print(ticker)
        # print(volum_ticker_now)
        # print(volum_ticker_avg)
        print(len(volum_ticker_now))
        # print(volum_ticker_avg[0][1])
        # print("-------------------")   
    for i in range(0,len(tickers_krw)):
        
        if len(volum_ticker_now) == len(tickers_krw) :
            if volum_ticker_avg[i][1] * 5  < volum_ticker_now[i][1] :
                label_alert0.config(text=volum_ticker_now[i][0]+"거래량 급등",bg="red") 
                msgbox.showinfo("",volum_ticker_now[i][0]+"거래량 급등")
                
        else:     
            label_alert0.config(text="체크중",bg="green")   
        
    global running
    if running == True:
        root.after(10, start_vol_check)    # 0.1초에 한번씩 start_vol_check() 호출
    else:    
        running = True
        
def stop_vol_check():
    global running
    running = False

button_start = Button(root,text="시작", command=start_vol_check ,width=5, height=2)
button_start.grid(row=4,column=0)

button_close = Button(root,text="닫기", command=stop_vol_check ,width=5, height=2)
button_close.grid(row=4,column=1)

label_alert0 = Label(root, text="알림", width=20, height=2)
label_alert0.grid(row=5,column=0)

label_alert1 = Label(root, text="알림", width=20, height=2)
label_alert1.grid(row=6,column=0)

label_alert2 = Label(root, text="알림", width=20, height=2)
label_alert2.grid(row=7,column=0)

root.mainloop()
