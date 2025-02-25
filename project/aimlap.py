from tkinter import *
import random
from datetime import datetime

# 전역변수
win = None
num_t = 0
start = None
k = 1
btn = None
ent = None

def cc():
    global k, btn  # k를 전역 변수로 선언
    if k < num_t:
        k += 1
        btn.destroy()
        ran_btn()
    else:
        fin = datetime.now()
        dif_sec = (fin - start).total_seconds()
        btn.destroy()
        lab = Label(win, text="Clear " + str(dif_sec) + "초")
        lab.grid(column=0, row=1, columnspan=2, pady=20)

def ran_btn():
    global btn
    btn = Button(win, bg="red", text=str(k), command=cc)
    
    # 버튼이 창 안에서 랜덤 배치되도록 제한
    relx = random.uniform(0.1, 0.8)
    rely = random.uniform(0.1, 0.8)
    
    btn.place(relx=relx, rely=rely)

def btn_f():
    global num_t, start, k  # k를 초기화
    num_t = int(ent.get())
    k = 1  # 게임 시작 시 k 초기화
    
    # 기존 UI 요소 제거
    for wg in win.grid_slaves():
        wg.destroy()
    
    win.geometry("500x500")
    ran_btn()
    start = datetime.now()

def start_game():
    global win, ent  # tkinter 창과 입력 필드를 전역으로 설정

    win = Tk()
    win.title("AIM_GAME")
    win.geometry("550x150")
    win.option_add("*Font", "궁서 20")

    # Label
    lab = Label(win, text="표적 개수")
    lab.grid(column=0, row=0, padx=20, pady=20)

    # Entry
    ent = Entry(win)
    ent.grid(column=1, row=0, padx=20, pady=20)

    # 시작 버튼
    btn = Button(win, text="시작", command=btn_f)
    btn.grid(column=0, row=1, columnspan=2)

    win.mainloop()

if __name__ == "__main__":
    start_game()
