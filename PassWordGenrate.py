import random
# all array are the same size
LowerCaseLetter = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
CapitalCaseLetter = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
SpecialCharacters =("!","@","#","$","%","^","&","*","(",")","_","+","?","|","~",".","/","}","{","[","]","-",":",";","<",">")

class PasswordGenerator:
    EnableLowerCase:bool=False
    EnableCapitalCase:bool =False
    EnableSpecialCharacters:bool= False
    Password:str=""
    SizePassword:int =8
    def __init__(self,LowerCaseLetter:bool=True,CapitalCaseLetter:bool=True,SpecialCharacter:bool=True,NumberofLetter:int =8):
        self.EnableLowerCase =LowerCaseLetter
        self.EnableCapitalCase = CapitalCaseLetter
        self.EnableSpecialCharacters = SpecialCharacter
        self.SizePassword = NumberofLetter

    def GenerateLowerCase(self,Element):
        if(self.EnableLowerCase == True):
            return str(LowerCaseLetter[Element])
    
    def GenerateCapitalCase(self,Element):
        if(self.EnableCapitalCase == True):
            return str(CapitalCaseLetter[Element])
    
    def GenerateSpecialCharacter(self,Element):
        if(self.EnableSpecialCharacters == True):
            return str(SpecialCharacters[Element])

    def GeneratePassword(self):
        NumberIteration:int =0
        while(NumberIteration != self.SizePassword):
            ValueAccesNumber =random.randint(0,len(LowerCaseLetter)-1)
            ArrayToChooseNumber =random.randint(1,3)
            if(self.EnableLowerCase == False and self.EnableCapitalCase == False and self.EnableSpecialCharacters == False):
                break
            if(ArrayToChooseNumber ==1  and self.EnableLowerCase == True):
                self.Password+=str(self.GenerateLowerCase(ValueAccesNumber))
                NumberIteration+=1
            elif(ArrayToChooseNumber ==2  and self.EnableCapitalCase == True):
                self.Password+=str(self.GenerateCapitalCase(ValueAccesNumber))
                NumberIteration+=1
            elif(ArrayToChooseNumber ==3 and self.EnableSpecialCharacters == True):
                self.Password+=self.GenerateSpecialCharacter(ValueAccesNumber)
                NumberIteration+=1


        return self.Password    