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
        if os.path.exists(self.dest_file_name):
            os.remove(self.dest_file_name)
        destination_file = open(str(self.dest_file_name), "w+")
        destination_file.writelines(bin_commands)
        destination_file.close()

        print('File written to: ' + os.path.abspath(self.dest_file_name))
