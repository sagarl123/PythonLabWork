class CharacterDisplay(object):
    string =''
    def takeInput(self):
        self.string = input('please enter string: ')
    
    def displayOutput(self):
        output = ''
        for i in self.string:
            if(ord(i)>=65 and ord(i)<=90 or (ord(i)>=97 and ord(i)<122) or (ord(i)==32)):
                output += chr(ord(i))
        print(output)
     
a = CharacterDisplay()
a.takeInput()
a.displayOutput()