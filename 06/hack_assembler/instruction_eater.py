"""This module is for taking already prepared symbolic commands
and interpreting them into machine language.
"""

from c_instruction import CInstruction
from a_instruction import AInstruction

class InstructionEater:
    """After whitespace has been removed from symbolic commands,
    this class takes instructions and returns them in binary format.
    """


    def __init__(self, asm_cmds, symb_tbl):
        self.symb_tbl = symb_tbl
        self.bin_command_list = []

        for i in enumerate(asm_cmds):
            if InstructionEater.is_a_command(i[1]):
                self.add_a_instruction(i[1])
            else:
                self.add_c_instruction(i[1])


    @staticmethod
    def is_a_command(a_cam_tst):
        """Checks if string begins with '@' character.
        """
        return a_cam_tst[0] == '@'

    def add_a_instruction(self, symb_cmd):
        """Appends binary A Instruction to binary commands list.
        """
        new_inst = AInstruction(symb_cmd, self.symb_tbl)
        self.bin_command_list.append(new_inst.translate())
        self.update_symbol_table(new_inst.symbol_table)

    def update_symbol_table(self, new_table):
        """Retrieve latest symbol table after each a command is
        translated.
        """
        self.symb_tbl = new_table

    def add_c_instruction(self, symb_cmd):
        """Add binary instruction following the rules of
        a C-Command."""
        new_inst = CInstruction(symb_cmd)
        self.bin_command_list.append(new_inst.translate())
