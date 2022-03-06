#python GUI Package
from tkinter import *
#MyWindow Class is defined
class MyWindow:
    #constructor
    def __init__(self, win):
        #label,textbox and button are created and placed at desired place.
        self.lbl1=Label(win, text='Enter the numbers')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t3=Entry()
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1=Button(win, text='Display Matrix', command=self.matrix)
        self.b2=Button(win, text='Array Flip',command=self.flip)
        self.b3=Button(win, text='Unique Elements',command=self.unique)
        self.b4 = Button(win, text='Possible Matrix', command=self.possible)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.b3.place(x=300, y=150)
        self.b4.place(x=100, y=100)
        self.lbl3.place(x=100, y=200)
        self.t3.place(width=200,height=100,x=200, y=200)
    #fuction is created to perform possible matrix operation.
    def possible(self):
        self.t3.delete(0,'end')
        num1 = self.t1.get()
        l = []
        c = ''
        for i in num1:
            if (i >= '0' and i <= '9'):
                c = c + i
            else:
                l.append(c)
                c = ''
        lenl = len(l)
        # if (lenl % 2 == 0):
        #     matrix = lenl * 0.25
        #     print(int(matrix))
        posmatrix=[4,9,16,25,36]
        if lenl in posmatrix:
            if lenl==4:
                self.t3.insert(END,'2x2')
            elif lenl==16:
                self.t3.insert(END, '4x4')
            elif lenl==36:
                self.t3.insert(END, '6x6')
            elif lenl==9:
                self.t3.insert(END, '3x3')
            elif lenl==25:
                self.t3.insert(END, '5x5')
        else:
            self.t3.insert(END, 'Enter only arrays of length 4,9,16,25,36')
    #fucntion is created to perform display matrix operation.
    def matrix(self):
        self.t3.delete(0, 'end')
        num1=self.t1.get()
        l=[]
        r=[]
        c=''
        l0=[]
        l1=[]
        l2=[]
        l3=[]
        for i in num1:
            if(i>='0' and i<='9'):
                c=c+i
            else:
                l.append(c)
                c=''
        lenl = len(l)
        if(lenl==4):
            # result="2x2"
            for i in range(0,2):
               l0.append(l[i])
               l1.append(l[i+2])
            r.append(l0)
            r.append(l1)
        elif(lenl==9):
            result = "3x3"
            for i in range(0,3):
               l0.append(l[i])
               l1.append(l[i+3])
               l2.append(l[i + 6])
            r.append(l0)
            r.append(l1)
            r.append(l2)
        elif(lenl==16):
            result="4x4"
            for i in range(0,4):
               l0.append(l[i])
               l1.append(l[i+3])
               l2.append(l[i + 6])
               l3.append(l[i + 9])
            r.append(l0)
            r.append(l1)
            r.append(l2)
            r.append(l3)
        self.t3.insert(END, str(r))

    # fucntion is created to perform array flip operation.
    def flip(self):
        self.t3.delete(0, 'end')
        num1 = self.t1.get()
        l = []
        c=''
        for i in num1:
            if (i >= '0' and i <= '9'):
                c = c + i
            else:
                l.append(c)
                c = ''
        l.reverse()
        self.t3.insert(END, str(l))

    # fucntion is created to perform unique elements operation.
    def unique(self):
        self.t3.delete(0, 'end')
        num1 = self.t1.get()
        l = []
        c = ''
        for i in num1:
            if (i >= '0' and i <= '9'):
                c = c + i
            else:
                l.append(c)
                c = ''
        for j in l:
            if(l.count(j)==1):
                self.t3.insert(END, j+" ")
#setup object by calling the Tk() function
window=Tk()
#calling the MyWindow class
mywin=MyWindow(window)
#Displaying the title and geometry of the GUI.
window.title('Array Manipulation')
window.geometry("500x400+10+10")
#event listening loop
window.mainloop()