def assembler_interpreter(program):
	# return a dictionary with the registers
   
    pc =0 # Program Counter
    register_table = {}
    lable_table = {}

    # Break up program into array of instructions
    def parse_lines(program):
        lines = []
        return lines
        pass

    # Locate all labels in program, and store label/address associations in label table
    def label_program(program_lines):
        pass

    # Break up instruction into key components as strings
    def parse_characters(instruction):
        instruction_type = ""
        val1 = ""
        val2 = ""
        stage =0
        sign2 = 1
        checkForSpaces = False # flag used to determine if spaces are important
        for c in instruction:
            if(not checkForSpaces and c == ' '): continue
            if(stage ==0): # parse instruction type
                if(c == ' ') :
                     stage = 1
                     checkForSpaces = False
                elif(c == ':'): instruction_type = ""
                else : 
                    instruction_type += c
                    checkForSpaces = True

            elif(stage ==1): # parse first arg
                if(c == ','): pass
                elif(c == ' '): 
                    stage = 2
                    checkForSpaces = False
                else:
                     val1 += c
                     checkForSpaces = True
            elif(stage ==2): # parse second arg
                if(c == ' '): break
                elif(c == '-'): sign2 = -1
                else: val2 += c
        return(instruction_type, val1, val2, sign2 )


    while(pc < len(program)) :
        instr, arg1, arg2, sign2 = parse(program[pc])
        if(instr == "mov"):
            if(arg2.isdigit()): 
                register_table[arg1] = int(arg2)*sign2
            elif(arg2.isalpha()):
                register_table[arg1] = register_table[arg2]
            pc += 1
        elif(instr == "inc"):
            register_table[arg1] = register_table[arg1] + 1
            pc +=1
        elif(instr == "dec"):
            register_table[arg1] = register_table[arg1] - 1
            pc +=1
        elif(instr == "jnz"):
            if(arg1.isdigit() and int(arg1) != 0):
                 pc += int(arg2)*sign2
            elif(arg1.isalpha() and int(register_table[arg1]) != 0): 
                pc += int(arg2)*sign2
            else : 
                pc +=1
    return(register_table)
