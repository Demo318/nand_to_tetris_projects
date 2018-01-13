"""hack_assembler.py takes a .asm file and returns a .hack file
of binary machine language.
"""

import sys
from file_interpreter import FileInterpreter
from instruction_eater import InstructionEater
from file_maker import HackFileMaker

if len(sys.argv) < 2:
    print('Usage: python3 hack_assembler.py [usr_file.asm] - assemble to machine language.')
    sys.exit()

ASM_INSTS = FileInterpreter(sys.argv[1])

BIN_CMDS = InstructionEater(ASM_INSTS.collected_commands(), ASM_INSTS.collected_symbols())

NEW_FILE = HackFileMaker(sys.argv[1])

NEW_FILE.make_file(BIN_CMDS.bin_command_list)

exit()
