#! /usr/bin/env python3
# From Nand to Tetris Pt. 1, ch6.
"""Create program to convert symbolic assembly code into binary code."""

# Step 1: First Pass
# Open file.
# Go through & identify symbol positions (i.e. (LOOP), (END), etc.)
# Create a symbol table to keep track of built-in symbols as well as
# symbols declared by the code.


# Step 2: Second Pass
# Convert all symbolic code into binary assembly code.
# Catch all variables and record them to the symbol table,
# staring memory at n = 16 and counting up from there.


# Step 3: Write to File
# Should use the same file name with .hack as the ending.
# Assembly code only, no comments or whitespace.

import sys
import re
import os

if len(sys.argv) < 2:
    print('Usage: python3 hack_assembler.py [usr_file.asm] - assemble to machine language.')
    sys.exit()

# Step 1
# Declare symbol table w/ built-in symbols.
SYMBOL_TABLE = {'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5,
                'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10, 'R11':11,
                'R12':12, 'R13':13, 'R14':14, 'R15':15, 'SCREEN':16384, 'KBD':24576,
                'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4}

# Methods to identify different properties of lines.
def is_ignorable(ig_line):
    """If line is a comment or contains only whitespace"""
    ig_regex = re.compile(r'^\s*//.*$|^\s*$')
    if ig_regex.match(ig_line):
        return True
    else:
        return False

def clean_up_line(cl_line):
    """Remove whitespace & comments from line leaving only useful commands behind"""
    cl_line = re.sub(r'\s', '', re.sub(r'//.*', '', cl_line))
    return cl_line


def is_position_symbol(symb_line):
    """Checks to see if command is a symbol that needs to
    be recorded as a position in the command list."""
    symbol_syntax = re.compile(r'^\(.+\)$')
    if symbol_syntax.search(symb_line):
        return True
    else:
        return False

# Open file through command-line args.
# Read into list, removing whitespace and comments.
COMMANDS_LIST = []
with open(sys.argv[1], 'r') as asm_file:
    # To record which line is being dealt with.
    LINE_COUNTER = 0
    for line in asm_file:
        if is_ignorable(line):
            continue
        else:
            line = clean_up_line(line)
            if is_position_symbol(line):
                SYMBOL_TABLE[line.strip('()')] = LINE_COUNTER
            else:
                COMMANDS_LIST.append(line)
                # Increment after operations on current line of habeen completed.
                LINE_COUNTER += 1

# Step 2: Second Pass
# Convert all symbolic code into binary assembly code.
# Catch all variables and record them to the symbol table,
# staring memory at n = 16 and counting up from there.

def is_a_command(a_cam_tst):
    """Checks if string begins with '@' character."""
    return a_cam_tst[0] == '@'

def is_in_symb_table(symb_table, tst_symb):
    """Checks if tst_symb is in dict symb_table."""
    for k in enumerate(symb_table):
        if k[1] == tst_symb:
            return True
    return False

def mem_taken(mem_num, symb_table):
    """See if number has allready been assigned in memory."""
    for key, val in symb_table.items():
        if val == mem_num and not key == key.upper():
            return True
    return False

COMP_TABLE = {'0':'0101010', '1':'0111111', '-1':'0111010',
              'D':'0001100', 'A':'0110000', 'M':'1110000',
              '!D':'0001101', '!A':'0110001', '!M':'1110001',
              '-D':'0001111', '-A':'0110011', '-M':'1110011',
              'D+1':'0011111', 'A+1':'0110111', 'M+1':'1110111',
              'D-1':'0001110', 'A-1':'0110010', 'M-1':'1110010',
              'D+A':'0000010', 'D+M':'1000010', 'D-A':'0010011',
              'D-M':'1010011', 'A-D':'0000111', 'M-D':'1000111',
              'D&A':'0000000', 'D&M':'1000000', 'D|A':'0010101',
              'D|M':'1010101'}

DEST_TABLE = {'M':'001', 'D':'010', 'MD':'011', 'A':'100',
              'AM':'101', 'AD':'110', 'AMD':'111', 'None':'000'}

JUMP_TABLE = {'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100',
              'JNE':'101', 'JLE':'110', 'JMP':'111', 'None':'000'}

VAR_MEM_COUNTER = 16
BIN_COMMAND_LIST = []
C_COMM_REGEX = re.compile(r'(^[A|M|D]+)?(=)?([A|M|D|!|\-|+|0|1|&|\|]+)(;)?(\w{3})?')
for i, symbol_command in enumerate(COMMANDS_LIST):
    instruction_command = '0'
    # Is this A-Command instruction?
    if is_a_command(symbol_command):
        address = symbol_command[1:]
        # Is this just a string of digits?
        if re.match(r'\D+', address):
            # Is this symbol already in the table?
            if not is_in_symb_table(SYMBOL_TABLE, address):
                # Is this a RAM address?
                if re.match(r'^RAM[/d+]', address):
                    SYMBOL_TABLE[address] = int(address[4:-2])
                # This is a new symbol that isn't a RAM address.
                else:
                    #Loop to enusre new variable assignment hasn't already been taken.
                    while mem_taken(VAR_MEM_COUNTER, SYMBOL_TABLE):
                        VAR_MEM_COUNTER += 1
                        if VAR_MEM_COUNTER >= 16384:
                            print("Compilation Error: Variable Memory Assignment in SCREEN Range")
                            print("Process Terminated")
                            exit()
                    SYMBOL_TABLE[address] = VAR_MEM_COUNTER
            address_num = SYMBOL_TABLE[address]
        else:
            address_num = address
        # Construct final binary command.
        bin_address = str(bin(int(address_num))).lstrip('0b').rjust(15, '0')
        full_command = instruction_command + bin_address

    # Is C-Command instruction
    else:
        c_comm_split = C_COMM_REGEX.search(symbol_command)
        full_command = ('111' +
                        COMP_TABLE[str(c_comm_split.group(3))] +
                        DEST_TABLE[str(c_comm_split.group(1))] +
                        JUMP_TABLE[str(c_comm_split.group(5))])

    BIN_COMMAND_LIST.append(full_command + "\n")

# Step 3: Create new .hack file
DESTINATION_FILE_NAME = str(re.compile(r'(.+)(\.\w+)').search(sys.argv[1]).group(1)) + '.hack'
# DESTINATION_FILE_NAME = ORIGIN_FILE_NAME.groups(1) + '.hack'
if os.path.exists(DESTINATION_FILE_NAME):
    os.remove(DESTINATION_FILE_NAME)
DESTINATION_FILE = open(str(DESTINATION_FILE_NAME), "w+")
DESTINATION_FILE.writelines(BIN_COMMAND_LIST)

print('File written to: ' + os.path.abspath(DESTINATION_FILE_NAME))
