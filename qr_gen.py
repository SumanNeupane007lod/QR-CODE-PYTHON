from tkinter import *
from resizeimage import resizeimage
import qrcode
from tkinter import filedialog
from PIL import Image,ImageTk

class QGen:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False,False)

        self.var_Fname=StringVar()
        self.var_address=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.Save_Qr=StringVar()
        self.download_Path = StringVar()

        title=Label(self.root,text="QR Generator",font=("times new roman",40),bg='black',fg='white').place(x=0,y=0,relwidth=1)

        entryFrame=Frame(self.root,bd=2,relief=RIDGE,bg='black')
        entryFrame.place(x=50,y=100,width=500,height=380)
        
        title1=Label(entryFrame,text="Personal Information",font=("goudy old style",20),bg='black',fg='white').place(x=0,y=0,relwidth=1)
        
        lbl_code=Label(entryFrame,text="Full_Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(entryFrame,text="Address",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_dept=Label(entryFrame,text="E-mail",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_phno=Label(entryFrame,text="Phone",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        lbl_folder = Label(entryFrame, text="Pick Location : ", font=("times new roman", 15, 'bold'), bg='white').place(x=20,y=220)

        
        txt_code=Entry(entryFrame,textvariable=self.var_Fname,font=("times new roman",15),bg='white').place(x=200,y=60)
        txt_name=Entry(entryFrame,textvariable=self.var_address,font=("times new roman",15),bg='white').place(x=200,y=100)
        txt_dept=Entry(entryFrame,textvariable=self.var_email,font=("times new roman",15),bg='white').place(x=200,y=140)
        txt_phno=Entry(entryFrame,textvariable=self.var_phone,font=("times new roman",15),bg='white').place(x=200,y=180)
        txt_path = Entry(entryFrame, textvariable=self.download_Path, font=("times new roman", 15), bg='white').place(x=200,y=220,width=295)


        btn_gen=Button(entryFrame,text='Generate QR',command=self.gen,font=("times new roman",18,'bold'),bg='blue',fg='black').place(x=70,y=280,width=180,height=30)
        btn_clr=Button(entryFrame,text='Clear',command=self.clr,font=("times new roman",18,'bold'),bg='blue',fg='black').place(x=300,y=280,width=120,height=30)
        btn_dir = Button(entryFrame, text='Choose folder', command=self.Browse, font=("times new roman", 13, 'bold'),bg='blue',fg='white').place(x=300, y=250, width=180, height=20)

        self.msg=''
        self.lbl_msg=Label(entryFrame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)



        qrFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qrFrame.place(x=600,y=100,width=250,height=380)
        title2=Label(qrFrame,text="QR Code",font=("goudy old style",20),bg='black',fg='white').place(x=0,y=0,relwidth=1)

        self.qrc=Label(qrFrame,text='QR WILL BEEN SEEN HERE',font=('times new roman',8),bg='black',fg='white',bd=1,relief=RIDGE)
        self.qrc.place(x=35,y=100,width=180,height=180)

    def clr(self):
        self.var_Fname.set('') 
        self.var_address.set('') 
        self.var_email.set('') 
        self.var_phone.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qrc.config(image='')
        self.download_Path.set('')
    
    def Browse(self):
        download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        self.download_Path.set(download_Directory)

    def gen(self):
        if self.var_Fname.get()=='' or self.var_address.get()=='' or self.var_email.get()=='' or self.var_phone.get()=='':
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Full Name : {self.var_Fname.get()}\nAddress : {self.var_address.get()}\nEmail : {self.var_email.get()}\nPhone No : {self.var_phone.get()}")
            qr_code=qrcode.make(qr_data)
            
            qr_code=resizeimage.resize_cover(qr_code,[190,190])
            qr_code.save("QR/R_"+str(self.var_Fname.get())+'.png')

            self.img=ImageTk.PhotoImage(qr_code)
            self.qrc.config(image=self.img)
            
            self.msg="Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg,fg='black')


root=Tk()
o=QGen(root)
root.mainloop()