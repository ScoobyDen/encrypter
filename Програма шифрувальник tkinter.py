from tkinter import *

def goDecode():
    if (rBtn.get() == 0 or rBtn.get() == 1):
        goCode()
    else:
        tOutput.delete(1.0, END)
        tIn = tInput.get(1.0, END)
        tIn = tIn[0:len(tIn) - 1]
        tOut = ""
        if (rBtn.get() == 2):
            for i in range(len(tIn)):
                tout += chr(ord(tIn[i]) - 1)
        elif (rBtn.get() == 3):
            p = 0
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - p)
                p = (p + 1) % 33
        tOutput.insert(1.0, tOut)

def goCode():
    tOutput.delete(1.0, END)
    tIn = tInput.get(1.0, END)
    #Убираємо перенос строки
    tIn = tIn[0:len(tIn) - 1]
    tOut = ""
    if (rBtn.get() == 0):
        for i in range(len(tIn) - 1, -1, -1):
            tOut += tIn[i]
    elif (rBtn.get() == 1):
        for i in range(0, len(tIn) - 1, 2):
            tOut += tIn[i + 1] + tIn[i]
    elif (rBtn.get() == 2):
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + 1)
    elif (rBtn.get() == 3):
        p = 0
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + p)
            p = (p + 1) % 33
    tOutput.insert(1.0, tOut)

def clearText():
    tInput.delete(1.0, END)
    tOutput.delete(1.0, END)

def resToDef():
    tInput.delete(1.0, END)
    txt = tOutput.get(1.0, END)
    txt = txt[0:len(txt) - 1]
    tInput.insert(1.0, txt)

def pasteFromClipboard():
    try:
        tInput.insert(END, root.clipboard_get())
    except:
        tInput.insert(END, "\nПОМИЛКА: Буфер пустий")

def copyToClipboard():
    root.clipboard_clear();
    root.clipboard_append(tOutput.get(1.0, END))

def setMenuPos(event):
    menuInput.pos(event.x_root, event.y_root)

#Ініціалізація вікна
root = Tk()
root.resizable(False, False)
root.title("Шифрувальник")

#Налаштування геометрії вікна
WIDTH = 800
HEIGHT = 320
POS_X = root.winfo_screenmmwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

#Текстові відмітки
textInput = Label(text="Введіть початковий текст: ")
textInput.place(x=2, y=1)
textOutput = Label(text="Резултат:")
textOutput.place(x=2, y=157)

#текстові поля
tInput = Text(width=70, height=8, wrap=WORD)
tInput.place(x=5, y=20)
tInput.insert(1.0, """Екземпляри Checkbutton також можуть бути візуально оформлені 
в группу, але кожен флаг незалежен від інших. Кожен може бути 
в стані  "встановление" або "знятий", незалежно від стану інших флагів. 
Іншими словами, в группі Checkbutton можна зробити множинний 
вибір, в группі Radiobuuton - ні.""")

scrollInput = Scrollbar(command=tInput.yview, width=20)
scrollInput.place(x=570, y=20, height=132)
tInput['yscrollcommand'] = scrollInput.set

tOutput = Text(width=70, height=8, wrap=WORD)
tOutput.place(x=5, y=180)

scrollOutput = Scrollbar(command=tOutput.yview, width=20)
scrollOutput.place(x=570, y=180, height=132)
tOutput['yscrollcommand'] = scrollOutput.set

#Меню на першу кнопку
menuInput = Menu(tearoff=False)
menuInput.add_command(label='Копіювати результат', command=copyToClipboard)
menuInput.add_command(label='Встивити первісний текст', command=pasteFromClipboard)
menuInput.add_command(label='Результат -> Первісний', command=resToDef)
menuInput.add_command(label='Очистити текст', command=clearText)
tInput.bind('<Button-3>', setMenuPos)

btnCode = Button(text='Шифрувати', width=25, command=goCode)
btnCode.place(x=600, y=20)

btnDecode = Button(text='Дешифрувати', width=25, command=goDecode)
btnDecode.place(x=600, y=50)

# Радіокнопки
textAlgo = Label(text='Алгоритм:')
textAlgo.place(x=600, y=100)
rBtn = IntVar()
rBtn.set(0)
algo01 = Radiobutton(text="Інвертувати", variable=rBtn, value=0)
algo02 = Radiobutton(text="Заміна з сусідньої", variable=rBtn, value=1)
algo03 = Radiobutton(text="+1", variable=rBtn, value=2)
algo04 = Radiobutton(text="+позиція (до33)", variable=rBtn, value=3)
algo01.place(x=600, y=120)
algo02.place(x=600, y=140)
algo03.place(x=600, y=160)
algo04.place(x=600, y=180)

root.mainloop()

