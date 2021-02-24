
"""
*********IMPORTANT************

INSTALL ON CMD(python3):
pip install colormap
pip install pillow

WE DON´T HAVE A REGISTRER PAGE
USE to test:
Username: Murillo
Password: 123456

"""

from tkinter import*
from tkinter import messagebox

import PIL
from PIL import ImageTk
from PIL import Image
 
          
class Login_System:
    
        
    def __init__(self, root):
               
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1280x810+0+0")

        # Imagens
              
        self.bg_icon   = ImageTk.PhotoImage(PIL.Image.open(r"LoginSystem\images/background.png"))
        self.user_icon = ImageTk.PhotoImage(PIL.Image.open(r"LoginSystem\images/username-icon.png"))     
        self.pass_icon = ImageTk.PhotoImage(PIL.Image.open(r"LoginSystem\images/password-icon.png"))
        self.logo_icon = ImageTk.PhotoImage(PIL.Image.open(r"LoginSystem\images/logo-icon.png"))
        
        self.uname=StringVar()
        self.pass_=StringVar()
  
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="Login System",font=("Helvetica",40,"bold"),bg='#005f80' ,fg='#f5f9ff',bd=10)
        title.place(x=0,y=0,relwidth=1)
        
        Login_Frame=Frame(self.root,bg=('#f5f9ff'),height=51 , width=51)
        Login_Frame.place(x=400,y=150)
        
        self.uname.set("")
        self.pass_.set("")
        
        logolbl=Label(Login_Frame,image=self.logo_icon,compound=CENTER,borderwidth=0,bg='#f5f9ff').grid(row=0,columnspan=3,pady=20)
       
        
        userlbl=Label(Login_Frame,text="Usuário",image=self.user_icon,compound=LEFT,borderwidth=0,font=("Helvetica",20,"bold"),bg='#f5f9ff').grid(row=1,column=0,padx=20,pady=5)
        textuser=Entry(Login_Frame,bd=2,relief=GROOVE,textvariable=self.uname,font=("",15),bg='#f5f9ff').grid(row=1,column=1,padx=5)
        
        passlbl=Label(Login_Frame,text="Senha  ",image=self.pass_icon,compound=LEFT,font=("Helvetica",20,"bold"),bg='#f5f9ff').grid(row=2,column=0,padx=0,pady=5)
        textpass=Entry(Login_Frame,bd=3,relief=GROOVE,textvariable=self.pass_,font=("",15),bg='#f5f9ff').grid(row=2,column=1,padx=5)
        
        def login():
            if self.uname.get()=="" or self.pass_.get()=="":
                messagebox.showerror("Error","Preencha todos os campos!")
            elif self.uname.get()=="Murillo" and self.pass_.get()=="123456":
                messagebox.showinfo("Sucesso",f"Bem-vindo {self.uname.get()}")
            else:
                messagebox.showerror("Error","Usuario ou senha invalido!")
                
        btn_log=Button(Login_Frame, text="Login",width=15, font=("Helvetica",15,"bold"),bg='#f5f9ff',command=login).grid(row=3,columnspan=3,pady=15)
        

    
            
root = Tk()
obj = Login_System(root)
root.mainloop()
