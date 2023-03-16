def find_noun_and_verb(intcode, desired_output):
    for noun in range(100):
        for verb in range(100):
            # create a copy of the intcode to modify
            program = intcode[:]
            program[1] = noun
            program[2] = verb

            # run the program
            instruction_pointer = 0
            while program[instruction_pointer] != 99:
                opcode = program[instruction_pointer]
                operand1 = program[program[instruction_pointer + 1]]
                operand2 = program[program[instruction_pointer + 2]]
                result_address = program[instruction_pointer + 3]

                if opcode == 1:
                    program[result_address] = operand1 + operand2
                elif opcode == 2:
                    program[result_address] = operand1 * operand2
                else:
                    raise ValueError(f"Invalid opcode {opcode} at position {instruction_pointer}")

                instruction_pointer += 4

            # check if the desired output was produced
            if program[0] == desired_output:
                return noun, verb

    # if no input values produce the desired output, raise an error
    raise ValueError("Desired output not found")

