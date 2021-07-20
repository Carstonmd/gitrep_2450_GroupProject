"""CS 2450 Scrumsters
Duncan DeNiro,
Carston Dastrup
Aaron Brown
Andrew Campbell
"""
import math


"""
opcodes:
                Name   Operator   Operand                   Description
                READ    10        Destination Mem add.      Reads a word into mem location
                WRITE   11        Source Mem add.           Write word from loc. to screen
                LOAD    20        Source Mem add.           load word at mem loc. to Accum.
                STORE   21        Dest. Mem add.            store word from Accum to mem loc.
                ADD     30        Src. Mem add.             add word from mem loc. to value in
                                                            Accum. - result stays in Accum.
                SUBTRACT 31       Src. Mem. add.            SUBTRACT word in mem loc. from word
                                                            in Accum. result stays in Accum.
                DIVIDE  32        Src. Mem. add             DIVIDE word in Accum. by word in
                                                            mem loc. result left in Accum.
                MULTIPLY 33       Src. Mem add              MULTIPLY word in mem loc. by
                                                            word in Accum. result left in Accum.
                BRANCH   40       Branch Mem. Add.          Branch to mem loc.
                BRANCHNEG 41      Branch Mem Add            Branch to Mem. loc if word in Accum.
                                                            is Negative.
                BRANCHZERO 42     Branch Mem. Add.          Branch to mem. loc if word in Accum.
                                                            is zero
                HALT       43     None                      Pause program
"""


class opCodes:
    #default constructor
    def __init__(self):
       pass
    
    def mem_add_locator(self,opcode):
        """extracts mem loc. from opcode and returns 2 digit integer"""
        op_str = str(opcode)
        if opcode is not None:
            mem_loc = op_str[2:]
            if mem_loc[0] == 0:
                mem_loc = op_str[3:]
            return int(mem_loc)
        else:
            quit()


    def read(self, mem_loc, memory_struct):
        """READ operation"""
        word = input("Enter an integer:")
        memory_struct[int(mem_loc)] = int(word)


    def write(self,src_add, memory_struct):
        """WRITE operation"""
        mem_loc = self.mem_add_locator(src_add)
        return print(f'WRITE from {mem_loc}: {memory_struct[mem_loc]}')


    def load(self, mem_loc, memory_struct, accumulator):
        """LOAD operation"""
        print("Loading from memory to accumuator: ")
        value_to_load = memory_struct[int(mem_loc)]
        accumulator = value_to_load#need to figure this out in meeting/teacher


    def store(self,dest_add, mem_struct, accum):
        """STORE operation"""
        value_to_store = accum
        mem_loc = self.mem_add_locator(dest_add)
        mem_struct[mem_loc] = value_to_store
        return print(f'STORE {value_to_store} from accumulator to memory loc.: {mem_loc}')


    def add(self,src_add, mem_struct):
        """ADD operation"""
        mem_loc = self.mem_add_locator(src_add)
        value_to_add = mem_struct[mem_loc]
        global accumulator
        accumulator += value_to_add
        return print(f'ADD {value_to_add} at mem loc. {mem_loc} to accumulator: {accumulator}')


    def subtract(self,src_add, mem_struct):
        """SUBTRACT operation"""
        mem_loc = self.mem_add_locator(src_add)
        value_to_sub = mem_struct[mem_loc]
        global accumulator
        accumulator -= value_to_sub
        return print(f'SUBTRACT {value_to_sub} at mem loc. {mem_loc} from accumulator: {accumulator}')


    def divide(self,src_add, mem_struct):
        """DIVIDE operation:
            may need to check numerator doesnt exceed size of denominator/accumulator value
            - what is expected behavior if result is float?
            - ceiling or floor operation?
        """
        mem_loc = self.mem_add_locator(src_add)
        value_denominator = mem_struct[mem_loc]
        global accumulator
        accumulator /= value_denominator

        return print(f'DIVIDE {value_denominator} at mem loc. {mem_loc} from accumulator: {int(accumulator)}')


    def multiply(self,src_add, mem_struct):
        """MULTIPLY operation"""
        mem_loc = self.mem_add_locator(src_add)
        value_to_multi = mem_struct[mem_loc]
        global accumulator
        accumulator *= value_to_multi
        return print(f'MULTIPLY {value_to_multi} at mem loc. {mem_loc} to accumulator: {int(accumulator)}')


    def branch(self,br_add, mem_struct):
        """BRANCH operation:
                - move instruction register to branch mem loc.
        """
        mem_loc = self.mem_add_locator(br_add)
        branch_to_add = mem_struct[mem_loc]
        return print(f'BRANCH to mem loc. {mem_loc} with value: {branch_to_add} ')


    def branch_neg(self,br_add, mem_struct):
        """BRANCHNEG operation:
                - if value in accumulator is negative: Branch to mem loc.
        """
        mem_loc = self.mem_add_locator(br_add)
        branch_to_add = mem_struct[mem_loc]
        global accumulator
        if accumulator < 0:
            return print(f'BRANCHNEG to mem loc. {mem_loc} with value: {branch_to_add}')


    def branch_zero(self,br_add, mem_struct):
        """BRANCHZERO operation:
                - if value in accumulator is zero: Branch to mem loc.
        """
        mem_loc = self.mem_add_locator(br_add)
        branch_to_add = mem_struct[mem_loc]
        global accumulator
        if accumulator == 0:
            return print(f'BRANCHZERO to mem loc. {mem_loc} with value: {branch_to_add}')


    def halt(self):
        quit()


class virtualMachine:
    #default constructor
    def __init__(self):
        self.memory = [None]*100# list of size 100 filled with zero's
        for i in range(100):
            self.memory[i] = 0
        self.operand = 0
        self.exitCode = -99999
        self.opCode = 0
        self.storedOpCodes = []#list of input opcodes
        self.storedMemory = []#list of input memory loccation
        self.validate_pass = True

        self.InstructCounter = 0
        self.InstructRegister = 0
        self.Accumulator = 0
        self.LineNum = 0
        self.LoadDialog = ""

    #This is where our function definitions are

    #logError does not return anything but will post an error log to console, I believe.
    def LogError(self,message):
        print("Returns nothing")
    

    #Dump, display all whats stored in memory
    def Dump(self):
        print("\nREGISTERS:          ")
        print("Accumulator:          " + str(self.Accumulator))
        print("InstrucctionCounter:  " + str(self.InstructCounter))
        print("InstructionRegister:  " + str(self.InstructRegister))
        print("OperationCode:        " + str(self.opCode))
        print("Operand:              " + str(self.operand))
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
            print(f"{index:05d}",end="")#displaying with leading zeros
            print(" ",end=" ")


    #Calls the prompt to the console. This likely will be called on load.
    #this may return a string?
    def prompt(self):
        print("""
            
            _   ___   _____ ___ __  __ 
            | | | \ \ / / __|_ _|  \/  |
            | |_| |\ V /\__ \| || |\/| |
            \___/  \_/ |___/___|_|  |_|
                Welcome to UVSim
        This program interprets and runs programs written in the BasicML language.
        Usage: The program is entered line by line. Once your program has been entered enter -99999 to run the application.
        You will be prompted with each line number sequentially followed by ? where you can input your BasicML for that line.
            """)

    #this will return a string
    def LinePrompt(self):
        #LineNum  requires some class name/required variable to iterate.
        return input("{:02d}?".format(self.LineNum)) 

    #this will validate input from users
    def validate(self,user_input):
        # Opcodes
        opcodes = [10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]
        # exitcode
        exit_code = str(-99999)

        # check for entry
        if user_input is None:
            self.validate_pass = False
            return print(f'No input detected'), self.validate_pass
            return print(f'No input detected')

        # check for none integer input
        if user_input.isalpha():
            self.validate_pass = False
            return print(f'{user_input} please enter integers only'), self.validate_pass
            return print(f'{user_input} please enter integers only')

        # convert input to string
        input_to_string = str(user_input)
        if input_to_string == exit_code:
            return print(f'exit code')
        # check for input less than 4
        if len(input_to_string) <= 4:
            if len(input_to_string) < 4:
                self.validate_pass = False
                return print(f'{input_to_string} has too few digits')
            if input_to_string[0] == '-':
                self.validate_pass = False
                return print(f'{input_to_string} has too few digits')
        # check to make sure input is either length 5 if signed or 4 if unsigned
        if len(input_to_string) >= 5 and input_to_string != exit_code:
            if len(input_to_string) > 5:
                self.validate_pass = False
                return print(f'{input_to_string} has too many digits')
            if len(input_to_string) == 5 and input_to_string[0] != '-':
                self.validate_pass = False
                return print(f'{input_to_string} must be 4 digits only')
        # check if input is a negative value
        if input_to_string[0] == '-':
            if input_to_string != exit_code:
                # slice opcode as substring
                input_to_string = input_to_string[1:]
                operator = input_to_string[0:2]
                # check opcode
                if int(operator) not in opcodes:
                    self.validate_pass = False
                    return print(f'{user_input} incorrect operator entered')
        input_operator = input_to_string[0:2]
        if int(input_operator) not in opcodes:
            self.validate_pass = False
            return print(f'{user_input} incorrect operator entered')

    def validate_memory(self,curr_mem_len):
        if curr_mem_len > len(self.memory):
            print(f'Memory Exceeded')


    def validate_instruct_counter(self,curr_counter_value):
        if curr_counter_value > len(self.memory):
            print(f'Too many entries have been made')
    #running a while loop getting the first instruction inputs seperating them in their own lists
    def execute(self):
        print("*** Please enter your program one instruction ***\n*** ( or data word ) at a time into the input ***\n*** text field. I will display the location ***\n*** number and a question mark (?). You then ***\n*** type the word for that location. Enter ***\n*** -99999 to stop entering your program. ***")
        incoming = None
        inc = 0

        while incoming != "-99999":
            if inc < 10:
                print("0" + str(inc) + " ? ",end="")
            else:
                print(str(inc) + " ? ",end="")
            
            incoming = input()
            self.validate(incoming)
            if self.validate_pass == False:
                self.validate_pass = True
                continue
            inc += 1
            if incoming != "-99999":
                self.InstructCounter +=1
            self.storedMemory.append(incoming[2:])#memory list
            self.storedOpCodes.append(incoming[:2])#opcode list
    def loadingStarting(self):
        print("*** Program loading completed ***\n*** Program execution begins ***")
        op = opCodes()
        count = 0
        for i in self.storedOpCodes:
            if i == "10":# Read
                word = input("Enter an integer:")
                self.memory[int(self.memory[count])] = int(word)
            if i == "11":# Write
                print(f'WRITE from {self.storedMemory[count]}: {self.memory[int(self.storedMemory[count])]}')
            if i == "20":#load
                print("Loading from memory to accumulator: ")
                value_to_load = self.memory[int(self.storedMemory[count])]
                self.Accumulator = value_to_load
            if i == "21":#Store
                value_to_store = self.Accumulator
                self.memory[int(self.memory[count])] = value_to_store
                print(f'STORE {value_to_store} from accumulator to memory loc.: {self.storedMemory[count]}')
            if i == "30":# Add
                pass
            if i == "31":#Sbtract
                pass
            if i == "32": #Divide
                pass
            if i == "33":#Multiply
                pass
            if i == "40":# branch
                pass
            if i == "41":#branching
                pass
            if i == "42":#branchzero
                pass
            if i == "43":#halt
                quit()
            count +=1
        
                    
    #main method if we want it not in a seperate class
def main():
    vm = virtualMachine()
    vm.prompt()
    vm.execute() 
    vm.loadingStarting()
    vm.Dump()

if __name__ == "__main__":
    main()