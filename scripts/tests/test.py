"""Specs for the functions contained in generate_other_language_files.py .

From the tests folder type python test.py
"""

# from pyfakefs import fake_filesystem_unittest
# from fake_filesystem_unittest import TestCase
#
#


import os
import sys
currentdir = os.path.dirname(os.path.abspath("."))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from pyfakefs.fake_filesystem_unittest import TestCase
from scripts.generate_other_language_files import get_file_list_in_folder
from scripts.generate_other_language_files import replicate_file
from scripts.generate_other_language_files import FILES_TO_SKIP

FILE_PATH = "/foo/bar/"
N_FILES_TO_CREATE = 5


def write_files(file_list, function_create_file):
    """Creates files using the supplied function."""
    for i_file in file_list:
        file_full_path = os.path.join(FILE_PATH, i_file)
        #print("Creating file: {}".format(file_full_path))
        function_create_file(file_full_path)

class TestFileDuplication(TestCase):
    """Test that all files are found and that the right number of copies are
    created."""

    def setUp(self):
        """Prepare fake filesystem."""
        self.setUpPyfakefs()

        self.file_names_to_find = ["file_test" + str(n_file) +
                                   ".md" for n_file in
                                   range(N_FILES_TO_CREATE)]
        self.file_names_to_skip = FILES_TO_SKIP
        write_files(self.file_names_to_find, self.fs.create_file)
        write_files(self.file_names_to_skip, self.fs.create_file)

    def test_files_found_are_required(self):
        """All files shall be in self.file_names_to_find."""
        file_found = get_file_list_in_folder(FILE_PATH)
        for i_file in file_found:
            assert(i_file in self.file_names_to_find)

    def test_all_required_files_are_found(self):
        """All files in self.file_names_to_find shall be found."""
        file_found = get_file_list_in_folder(FILE_PATH)
        for i_file in self.file_names_to_find:
            assert(i_file in file_found), \
                   "{} not in was not found".format(i_file)

    def test_skip_index_file(self):
        """The function shall skip a file named _index.md"""
        file_found = get_file_list_in_folder(FILE_PATH)

        # check none of the files is in self.file_names_to_skip
        for i_file in file_found:
            assert(i_file not in self.file_names_to_skip)

    def test_replicate_file(self):
        """The function shall replicate a given file and append a token to
        its name"""
        token_list = ("_1", "_2", "_3")
        original_file_list = [os.path.join(FILE_PATH, i_file)
                              for i_file in self.file_names_to_find]

        expected_file_list = [os.path.splitext(file_name)[0] + token +
                              os.path.splitext(file_name)[1]
                              for token in token_list
                              for file_name in original_file_list]
        print("Exepected file list: {}".format(",".join(expected_file_list)))

        replicated_file = []
        for i_file in original_file_list:
            new_file_created = replicate_file(i_file, token_list)
            replicated_file.extend(new_file_created)

        assert(set(replicated_file) == set(expected_file_list)), \
               "\n Expected: \n{}\n Obtained{}".format(",".join(expected_file_list), ",".join(replicated_file))

        # check files were actually created
        all_files_in_dir = [os.path.join(FILE_PATH, i_file)
                            for i_file in os.listdir(FILE_PATH)]
        for i_file in replicated_file:
            assert(i_file in all_files_in_dir), "{} was not created".format(i_file)


if __name__ == '__main__':
    unittest.main()
