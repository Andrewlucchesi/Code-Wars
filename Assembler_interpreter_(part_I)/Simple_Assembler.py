def simple_assembler(program):
	# return a dictionary with the registers
   
    pc =0 # Program Counter
    register_table = {}

    # Break up instruction into key components as strings
    def parse(instruction):
        instruction_type = ""
        val1 = ""
        val2 = ""
        stage =0
        sign2 = 1
        for c in instruction:
            if(stage ==0): # parse instruction type
                if(c != ' ') : instruction_type += c
                else : 
                    stage = 1
            elif(stage ==1): # parse first arg
                if(c == ','): pass
                elif(c == ' '): stage = 2
                else: val1 += c
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
