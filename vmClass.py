class virtualMachine:
    memory = [100]
    operand = 0
    exitCode = -99999
    opCode = 0

    InstructCounter = 0
    InstructRegister = 0
    Accumulator = 0
    LineNum = 0
    LoadDialog = ""

    #This is where our function definitions are

    #logError does not return anything but will post an error log to console, I believe.
    def LogError(message):
        print("Returns nothing")
    
    #Dump is a memory dump I think
    def Dump():
        print("Dump the memory!!")
    #Calls the prompt to the console. This likely will be called on load.
    #this may return a string?
    def Prompt():
        print("PROMPT EM")
    #this will return a string
    def LinePrompt():
        print("Somehow Different")
    #This calls the validate function
    def Validate():
        print("Return a string")
    
