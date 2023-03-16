def process_intcode_program(intcode_program):
    index = 0
    opcode = intcode_program[index]
    while opcode != 99:
        if opcode == 1:
            # addition operation
            input1_index = intcode_program[index+1]
            input2_index = intcode_program[index+2]
            output_index = intcode_program[index+3]
            intcode_program[output_index] = intcode_program[input1_index] + intcode_program[input2_index]
        elif opcode == 2:
            # multiplication operation
            input1_index = intcode_program[index+1]
            input2_index = intcode_program[index+2]
            output_index = intcode_program[index+3]
            intcode_program[output_index] = intcode_program[input1_index] * intcode_program[input2_index]
        index += 4
        opcode = intcode_program[index]
    return intcode_program
