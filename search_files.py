import os,glob


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.geometry("900x900")
win.title("SEARCHING FILES")
win.config(bg='#CDB79E')

label1=Label(win, text="SEARCH FILES", font=("Arial",25,'bold'),bg='#CDB79E')
label1.grid(row=0,column=1,padx=20,pady=20)

label2=Label(win, text="Enter the path", font=("Arial",15,'bold'),bg='#CDB79E')
label2.grid(row=1,column=0,padx=20,pady=20)

def search(value):
    if entry1.get()=='':
        messagebox.showerror('Path', 'Please enter the path')
    else:
        path=entry1.get()
        os.chdir(path)
    

        if value=='text':
            text1.delete('1.0',END)
            for file in glob.glob("*.txt"):
                text1.insert(END,file)
                text1.insert(END,'\n')



        if value=='all':
            text1.delete('1.0',END)
            for file in glob.glob("*.*"):
                text1.insert(END,file)
                text1.insert(END,'\n')
            
            
        if value=='png':
            text1.delete('1.0',END)
            for file in glob.glob("*.png"):
                text1.insert(END,file)
                text1.insert(END,'\n')
        

        if value=='alpha':
            text1.delete('1.0',END)
            for file in glob.glob("[a-z]*.py"):
                text1.insert(END,file)
                text1.insert(END,'\n')
    
        if value=='number':
            text1.delete('1.0',END)
            for file in glob.glob("*[0-9].*"):
                text1.insert(END,file)
                text1.insert(END,'\n')
    
        if value=='test':
            text1.delete('1.0',END)
            for file in glob.glob("test?.py"):
                text1.insert(END,file)
                text1.insert(END,'\n')
    
        if value=='ade':
            text1.delete('1.0',END)
            for file in glob.glob("[!ade]*.py"):
                text1.insert(END,file)
                text1.insert(END,'\n')
    
entry1=Entry(win,width=40,font=("Arial",15,'bold'))
entry1.grid(row=1,column=1,padx=20,pady=20)

frame1=Frame(win)
frame1.grid(row=2,column=1,padx=20,pady=20)

text1=Text(frame1, height=20,width=50)


scroll=Scrollbar(frame1,orient=VERTICAL,command=text1.yview)

scroll.pack(side=RIGHT,fill=Y)

text1.config(yscrollcommand=scroll.set)
text1.pack()


btn_txt=Button(win,text="Text Files", font=("Arial",12,'bold'),bg='#8B7D6B',command=lambda:search('text'))
btn_txt.grid(row=3,column=0,padx=5,pady=5)

btn_all=Button(win,text="ALL Files", font=("Arial",12,'bold'),bg='#8B7D6B',command=lambda:search('all'))
btn_all.grid(row=3,column=1,padx=5,pady=5)

btn_png=Button(win,text="PNG Files", font=("Arial",12,'bold'),bg='#8B7D6B',command=lambda:search('png'))
btn_png.grid(row=3,column=2,pady=5)

btn_alpha=Button(win,text="Starting with Alphabets .py", font=("Arial",12,'bold'),bg='#8B7D6B',command=lambda:search('alpha'))
btn_alpha.grid(row=4,column=0,padx=5,pady=5)

btn_num=Button(win,text="Ending with numbers", font=("Arial",12,'bold'),bg='#8B7D6B',command=lambda:search('number'))
btn_num.grid(row=4,column=1,padx=5,pady=5)

btn_test=Button(win,text="Test?  .py", font=("Arial",12,'bold'),bg='#8B7D6B',command=lambda:search('test'))
btn_test.grid(row=4,column=2,pady=5)

btn_not=Button(win,text="Not start with a,d,e  .py", font=("Arial",12,'bold'),bg='#8B7D6B',command=lambda:search('ade'))
btn_not.grid(row=5,column=1,padx=5,pady=5)

win.mainloop()
