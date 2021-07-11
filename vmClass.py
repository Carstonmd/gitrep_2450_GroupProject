class virtualMachine:

    def __init__(self):
        self.memory = [[]]*100# memory is a list of lists declared here
        for i in range(100):
            self.memory[i] = [0,0,0,0,0]
        self.operand = 0
        self.exitCode = -99999
        self.opCode = 0

        self.InstructCounter = 0
        self.InstructRegister = 0
        self.Accumulator = 0
        self.LineNum = 0
        self.LoadDialog = ""

    #This is where our function definitions are

    #logError does not return anything but will post an error log to console, I believe.
    def LogError(message):
        print("Returns nothing")
    

    #Dump is a memory dump I think
    def Dump(self):
        print("\nREGISTERS:          ")
        print("Accumulator:          ")# todo
        print("InstrucctionCounter:  ")# todo
        print("InstructionRegister:  ")# todo
        print("OperationCode:        ")# todo
        print("Operand:              ")# todo
        #Below is getting the format of the array displayed
        multiple = 0
        counter = 10
        print("\nMEMORY:")
        print("    00     01     02     03     04     05     06     07     08     09",end="")
        for index in self.memory:
            if counter % 10 == 0:
                print("\n"+str(multiple) + "0 ", end =" ")
                multiple += 1
                counter = 0
            counter +=1    
            for value in range(5):
                word = str(index[value])
                print(word, end ="")
            print(" ",end=" ")


    #Calls the prompt to the console. This likely will be called on load.
    #this may return a string?
    def Prompt():
        print("PROMPT EM")
    #this will return a string
    def LinePrompt():
        print("Somehow Different")
    #this will validate input from users
    def validate(user_input):
        print("Validate here")

#main method if we want it not in a seperate class
def main():
    vm = virtualMachine()
    vm.Dump() # to access a certain memory location use vm.memory[i][j] 
    
    


#running main
if __name__ == "__main__":
    main()
