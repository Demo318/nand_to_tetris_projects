"""hack_assembler.py takes a .asm file and returns a .hack file
of binary machine language.
"""

import sys
from file_interpreter import FileInterpreter
from instruction_eater import InstructionEater

if len(sys.argv) < 2:
    print('Usage: python3 hack_assembler.py [usr_file.asm] - assemble to machine language.')
    sys.exit()

ASM_INSTS = FileInterpreter(sys.argv[1])

print(ASM_INSTS.collected_commands())

BIN_CMDS = InstructionEater(ASM_INSTS.collected_commands(), ASM_INSTS.collected_symbols())

print(BIN_CMDS.bin_command_list)
