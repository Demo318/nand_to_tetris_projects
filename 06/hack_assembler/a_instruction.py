"""Module for interpreting A-Instructions.
"""

import re

class AInstruction:
    """Translating A-Instructions into binary.
    """

    var_mem_counter = 16

    def __init__(self, symbol_command, symbol_table):
        self.command = symbol_command[1:]
        self.symbol_table = symbol_table

    def translate(self):
        if self.cmd_is_not_digits():             # Confirm this is symbolic command
            if self.addy_not_in_symb_tbl():      # Confirm cmnd not already recorded.
                if self.cmd_is_ram():            # Confirm is a RAM symbolic cmd
                    self.assign_as_ram()         # Record into symb_table as RAM
                else:
                    self.assign_new_memory()     # Variable will need new place in memory.
            self.retrieve_num_frm_symbol_table() # Retrieve int address from symbol table.
        else:
            self.address_num = int(self.command) # Cmd is num. Save as the address.
        return self.binary_cmd()

    def cmd_is_not_digits(self):
        if re.match(r'\D+', self.command):
            return True
        return False

    def addy_not_in_symb_tbl(self):
        """Checks if tst_symb is in dict symb_table."""
        for k in enumerate(self.symbol_table):
            if k[1] == self.command:
                return False
        return True

    def cmd_is_ram(self):
        """Check if A-Command is RAM address.
        """
        if re.match(r'^RAM[/d+]', self.command):
            return True
        return False

    def assign_as_ram(self):
        self.symbol_table[self.command] = int(self.command[4:-2])

    def assign_new_memory(self):
        while AInstruction.is_mem_taken(self.symbol_table):
            AInstruction.var_mem_counter += 1
            if AInstruction.var_mem_counter >= 16384:
                print("Compilation Error: Variable Memory Assignment in SCREEN Range")
                print("Process Terminated")
                exit()
        self.symbol_table[self.command] = AInstruction.var_mem_counter

    @classmethod
    def is_mem_taken(cls, symb_tbl):
        """See if number has allready been assigned in memory."""
        for key, val in symb_tbl.items():
            if val == cls.var_mem_counter and not key == key.upper():
                return True
        return False

    def retrieve_num_frm_symbol_table(self):
        self.address_num = int(self.symbol_table[self.command])

    def binary_cmd(self):
        return str(bin(self.address_num)).lstrip('0b').rjust(16, '0')
