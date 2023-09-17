from tkinter import*
#define root
root=Tk()
root.title("Calculator")
#define class of buttons
class button:
    def __init__(self,text:str,func:str,row:int,column:int,width:int=8,colspan:int=1,rowspan:int=1,pady=1):
        self.text=text
        self.func=func
        self.pady=pady
        self.column=column
        self.row=row
        self.colspan=colspan
        self.width=width
        self.rowspan=rowspan
        self.funcs={"addition":self.add,
                    "subtraction":self.subtract,
                    "multiplication":self.multiply,
                    "division":self.divide,
                    "equal":self.equal,
                    "clear":self.clear,
                    "clc":self.clc
                    }
        self.deploy()
    def deploy(self):
        if self.func in [i for i in range(10)]:
            self.button=Button(root,text=self.text,width=self.width,command=lambda:self.num_button(self.func))
        else:
            self.dedicate=self.funcs[self.func]
            self.button=Button(root,text=self.text,width=self.width,pady=self.pady,command=self.dedicate)
        self.button.grid(column=self.column,row=self.row,rowspan=self.rowspan,columnspan=self.colspan)
    def clc(self):
        val=screen.get()
        self.clear()
        screen.insert(0,val[:-1])
    def add(self):
        val=screen.get()
        self.clear()
        screen.insert(0,val+'+')
        
    def subtract(self):
        val=screen.get()
        self.clear()
        screen.insert(0,val+'-')
       
    def divide(self):
        val=screen.get()
        self.clear()
        screen.insert(0,val+'/')
        
    def multiply(self):
        val=screen.get()
        self.clear()
        screen.insert(0,val+'*')
        
    def equal(self):
        op=screen.get()
        self.clear()
        screen.insert(0,eval(op))

    def clear(self):
        screen.delete(0,END)
    def num_button(self,i):
        previous=screen.get()
        self.clear()
        new=previous+f'{self.func}'
        screen.insert(0,new)
#define screen
screen=Entry(root,font=40,justify='center',width=28)
_1=button("1",1,5,2)
_2=button("2",2,5,1)
_3=button("3",3,5,0)
_4=button("4",4,4,2)
_5=button("5",5,4,1)
_6=button("6",6,4,0)
_7=button("7",7,3,2)
_8=button("8",8,3,1)
_9=button("9",9,3,0)
_0=button("0",0,6,1)
add=button("+","addition",2,1)
subtract=button("-","subtraction",2,2)
multiply=button("x","multiplication",2,3)
divide=button("÷","division",3,3)
clear=button("C","clear",2,0)
equal=button("=","equal",4,3,rowspan=2,pady=14)
back=button("<<","clc",6,0)
#packing
screen.grid(row=0,column=0,rowspan=2,columnspan=4,padx=10,pady=20,)
root.mainloop()