class CharacterEvenDisplay(object):
    string = ''
    
    def takeInput(self):
        self.string = input('please enter string: ')
    
    def displayOutput(self):
        output = ''
        for i in range(len(self.string)):
            if(i!=0 and i%2 ==0):
                print(self.string[i], end="")
              
       

a = CharacterEvenDisplay()
a.takeInput()
a.displayOutput()
        