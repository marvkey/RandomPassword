from tkinter import *
from PassWordGenrate import PasswordGenerator
import tkinter as tk
import pyperclip as pc
class SetGui:
    Window:Tk
    def __init__(self,GuiWindow= Tk()):
        self.Window =GuiWindow
    
    EnableLowerCase =BooleanVar()
    EnableCapitalCase=BooleanVar()
    EnableSpecialCharacter = BooleanVar()

    bEnableLowerCase:bool =False
    bEnableCapitalCase:bool =False
    bEnableSpecialCharacter:bool =False
    TextInput:Entry
    tkPassword:StringVar ="none"
    Password:str ="none"
    thepassword:tk.Label
    def lowercase(self):
        if( self.bEnableLowerCase ==False):
            self.bEnableLowerCase =True
        else:
            self.bEnableLowerCase =False

    def CaptialCaseLetter(self):
        if(self.bEnableCapitalCase==False):
            self.bEnableCapitalCase =True
        else:
            self.bEnableCapitalCase=False

    def SpecialCharacter(self):
        if(self.bEnableSpecialCharacter ==False):
            self.bEnableSpecialCharacter =True
        else:
            self.bEnableSpecialCharacter =False

    def Generatepassword(self):
        if not  self.TextInput.get(): 
            return 
        PasswordGenrate =PasswordGenerator(self.bEnableLowerCase,self.bEnableCapitalCase,self.bEnableSpecialCharacter,int( self.TextInput.get()))
        self.Password = PasswordGenrate.GeneratePassword()
        self.tkPassword =self.Password
        self.thepassword.config(text = self.Password) 

    def Copy(self):
        pc.copy(self.Password)
    def Mainloop(self):
        input  = tk.Label(self.Window,text ="Size of password").grid(row =0)

        self.TextInput =Entry(self.Window)
        self.TextInput.grid(row =0,column =1)
        number = self.TextInput.get()

        btn=Button(self.Window,text="generate", fg ="blue",command=self.Generatepassword)
        temp = tk.Label(self.Window,text ="Password = ")
        self.thepassword =tk.Label(self.Window,text = self.Password)

        LowerCaseLetter =Checkbutton(self.Window,text="Enable Lower case letters",variable=self.EnableLowerCase,command=self.lowercase)
        CaptialCaseLetter1 =Checkbutton(self.Window,text="Enable captial case letters",variable=self.EnableCapitalCase,command=self.CaptialCaseLetter)
        SpecialCharacter =Checkbutton(self.Window,text="Enable special characters",variable=self.EnableSpecialCharacter,command = self.SpecialCharacter)
        copyButton =Button(self.Window,text="Copy",command = self.Copy)
        LowerCaseLetter.place(x=0,y=30)
        CaptialCaseLetter1.place(x=0,y=60)
        SpecialCharacter.place(x=0,y=90)

        copyButton.place(x=40,y=120)
        btn.place(x=80,y=150)
        temp.place(x=40,y=180)

        self.thepassword.place(x=100,y=180)

        self.Window.title('password Generator')
        self.Window.geometry("300x200+10+20")
        self.Window.mainloop()