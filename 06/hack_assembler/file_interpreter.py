"""Module for initial contac with .asm file.
"""

import re

class FileInterpreter:
    """
    This module takes a .asm file and strips out comments & whitespace.
    Assembly command is placed into a list self.commands_list.
    """

    starting_symbol_table = {'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5,
                             'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10, 'R11':11,
                             'R12':12, 'R13':13, 'R14':14, 'R15':15, 'SCREEN':16384, 'KBD':24576,
                             'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4}

    def __init__(self, file_name):
        self.commands_list = []
        self.symbol_table = FileInterpreter.new_symb_table()

        with open(file_name, 'r') as asm_file:
            line_counter = 0
            for line in asm_file:
                if FileInterpreter.is_ignorable(line):
                    continue
                else:
                    line = FileInterpreter.clean_up_line(line)
                    if FileInterpreter.is_position_symbol(line):
                        self.symbol_table[line.strip('()')] = line_counter
                    else:
                        self.commands_list.append(line)
                        # Increment after operations on current line of have been completed.
                        line_counter += 1


    def collected_commands(self):
        """Returns full list of commands.
        """
        return self.commands_list

    def collected_symbols(self):
        """Returns dict of symbols.
        """
        return self.symbol_table

    @staticmethod
    def is_ignorable(passed_inst):
        """If line is a comment or contains only whitespace
        """
        ig_regex = re.compile(r'^\s*//.*$|^\s*$')
        if ig_regex.match(passed_inst):
            return True
        else:
            return False

    @staticmethod
    def clean_up_line(line):
        """Remove whitespace & comments from line leaving only useful commands behind.
        """
        line = re.sub(r'\s', '', re.sub(r'//.*', '', line))
        return line

    @staticmethod
    def is_position_symbol(symb_line):
        """Checks to see if command is a symbol that needs to
        be recorded as a position in the command list.
        """
        symbol_syntax = re.compile(r'^\(.+\)$')
        if symbol_syntax.search(symb_line):
            return True
        else:
            return False
    @classmethod
    def new_symb_table(cls):
        """Return the class symbol table so that
        an instance may have a copy to manipulate.
        """
        return cls.starting_symbol_table
