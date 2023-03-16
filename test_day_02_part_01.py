import unittest
from day_02_part_01 import process_intcode_program


class TestProcessIntcodeProgram(unittest.TestCase):
    def test_process_intcode_program(self):
        intcode_program = [1,0,0,0,99]
        expected_output = [2,0,0,0,99]
        self.assertEqual(process_intcode_program(intcode_program), expected_output)

        intcode_program = [2,3,0,3,99]
        expected_output = [2,3,0,6,99]
        self.assertEqual(process_intcode_program(intcode_program), expected_output)

        intcode_program = [2,4,4,5,99,0]
        expected_output = [2,4,4,5,99,9801]
        self.assertEqual(process_intcode_program(intcode_program), expected_output)

        intcode_program = [1,1,1,4,99,5,6,0,99]
        expected_output = [30,1,1,4,2,5,6,0,99]
        self.assertEqual(process_intcode_program(intcode_program), expected_output)

