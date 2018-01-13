"""Module for creating a new .hack file"""

import os
import re

class HackFileMaker:
    """Class for creating new .hack file.
    """
    file_name_regex = re.compile(r'(.+)(\.\w+)')

    def __init__(self, file_name):
        self.dest_file_name = HackFileMaker.file_name_regex.search(file_name).group(1)
        self.dest_file_name = str(self.dest_file_name) + '.hack'

    def make_file(self, bin_commands):
        """Takes list of bin_commands, writes new file.
        """
        bin_commands = self.add_line_breaks(bin_commands)
        destination_file = open(str(self.dest_file_name), "w+")
        destination_file.writelines(bin_commands)
        destination_file.close()

        print('File written to: ' + os.path.abspath(self.dest_file_name))

    @staticmethod
    def add_line_breaks(this_list):
        """Add \\n to each item in list."""
        for i in enumerate(this_list):
            this_list[i[0]] = i[1] + "\n"
        return this_list
