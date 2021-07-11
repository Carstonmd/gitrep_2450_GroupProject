class virtualMachine:

    def __init__(self):
        self.memory = [100]
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
    def Dump():
        print("Dump the memory!!")
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


        #ADDED A CHANGE FOR TEST GIT