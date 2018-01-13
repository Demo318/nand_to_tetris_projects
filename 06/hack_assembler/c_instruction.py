"""This module contains one class for handling a C instruction.
"""

import re

class CInstruction:
    """Rules for reading and translating C Instructions.
    """

    comp_table = {'0':'0101010', '1':'0111111', '-1':'0111010',
                  'D':'0001100', 'A':'0110000', 'M':'1110000',
                  '!D':'0001101', '!A':'0110001', '!M':'1110001',
                  '-D':'0001111', '-A':'0110011', '-M':'1110011',
                  'D+1':'0011111', 'A+1':'0110111', 'M+1':'1110111',
                  'D-1':'0001110', 'A-1':'0110010', 'M-1':'1110010',
                  'D+A':'0000010', 'D+M':'1000010', 'D-A':'0010011',
                  'D-M':'1010011', 'A-D':'0000111', 'M-D':'1000111',
                  'D&A':'0000000', 'D&M':'1000000', 'D|A':'0010101',
                  'D|M':'1010101'}

    dest_table = {'M':'001', 'D':'010', 'MD':'011', 'A':'100',
                  'AM':'101', 'AD':'110', 'AMD':'111', 'None':'000'}

    jump_table = {'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100',
                  'JNE':'101', 'JLE':'110', 'JMP':'111', 'None':'000'}

    c_inst_regex = re.compile(r'(^[A|M|D]+)?(=)?([A|M|D|!|\-|+|0|1|&|\|]+)(;)?(\w{3})?')

    def __init__(self, instruction):
        self.instruction = instruction

    def translate(self):
        """Uses class tables comp_table, dest_table, and jump_table to
        interpret symbolic commands and replace with binary instruction code.
        """
        c_comm_split = CInstruction.c_inst_regex.search(self.instruction)
        bin_c_inst = ('111' +
                      CInstruction.comp_table[str(c_comm_split.group(3))] +
                      CInstruction.dest_table[str(c_comm_split.group(1))] +
                      CInstruction.jump_table[str(c_comm_split.group(5))])
        return bin_c_inst
