from typing import List, Tuple


def process_intcode_program(intcode: List[int]) -> int:
    instruction_pointer = 0

    while intcode[instruction_pointer] != 99:
        opcode = intcode[instruction_pointer]

        if opcode not in [1, 2]:
            raise ValueError(f"Invalid opcode {opcode} at position {instruction_pointer}")

        operand1 = intcode[intcode[instruction_pointer + 1]]
        operand2 = intcode[intcode[instruction_pointer + 2]]
        result_position = intcode[instruction_pointer + 3]

        if opcode == 1:
            intcode[result_position] = operand1 + operand2
        elif opcode == 2:
            intcode[result_position] = operand1 * operand2

        instruction_pointer += 4

    return intcode[0]


def find_noun_and_verb(intcode: List[int], target_output: int) -> Tuple[int, int]:
    for noun in range(100):
        for verb in range(100):
            test_intcode = list(intcode)
            test_intcode[1] = noun
            test_intcode[2] = verb

            try:
                output = process_intcode_program(test_intcode)
            except ValueError:
                continue

            if output == target_output:
                return noun, verb

    raise ValueError(f"Could not find noun and verb producing target output {target_output}")
