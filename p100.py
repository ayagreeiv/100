class ATM:
    
    def _init_(self,name,cashleft,cashtook):
        self.name = name
        self.cashleft = cashleft
        self.cashtook = cashtook

    def setCashleft(self,cashleft):
        self.cashleft = cashleft

nick = ATM("Nick",9876,100)
jeff = ATM("jeff",1856,100)
albert = ATM("albert",1534,100)
mark = ATM("mark",4856,100)
print(nick.cashleft)
