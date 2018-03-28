from tkinter import *

window =Tk()

l1=Label(window, text="화씨")
l2=Label(window, text="섭씨")

l1.pack()	#pack() : 버튼을 최대한 압출하여 윈도우에 표시
l2.pack()

e1=Entry(window)	#사용자로부터 입력 받으려면
e2=Entry(window)

e1.pack()
e2.pack()

b1=Button(window,text="화씨->섭씨")
b2=Button(window,text="섭씨->화씨")

b1.pack()
b2.pack()

window.mainloop() #윈도우에서 발생하는 여러 가지 이벤트를 처리하는 함수

