#! /usr/bin/env python3
# From Nand to Tetris Pt. 1, ch6.
# Create program to convert symbolic assembly code into binary code.

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

if len(sys.argv) < 2:
    print('Usage: python3 hack_assembler.py [usr_file.asm] - assemble to machine language.')
    sys.exit()

# Step 1
# Declare symbol table w/ built-in symbols.
SYMBOL_TABLE = {'RO':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5,
                'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10, 'R11':11,
                'R12':12, 'R13':13, 'R14':14, 'R15':15, 'SCREEN':16384, 'KBD':24576,
                'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4}

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
                SYMBOL_TABLE[line.strip('()')] = LINE_COUNTER + 1
            else:
                COMMANDS_LIST.append(line)
            # Increment after operations on current line of habeen completed.
            LINE_COUNTER += 1

# TODO: Fill out methods below

# Methods to identify different properties of lines.
def is_ignorable(ig_line):
    """If line is a comment or contains only whitespace"""

def clean_up_line(cl_line):
    """Remove whitespace & comments from line leaving only useful commands behind"""

def is_position_symbol(symb_line):
    """Checks to see if command is a symbol that needs to
    be recorded as a position in the command list."""
    symbol_syntax = re.compile(r'\([A-Z]+\)')
    if symbol_syntax.search(symb_line):
        return True
    else:
        return False
