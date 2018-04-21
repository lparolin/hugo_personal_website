"""Specs for the functions contained in generate_other_language_files.py .

These specs can be run with nose2.
"""

# from pyfakefs import fake_filesystem_unittest
# from fake_filesystem_unittest import TestCase
from pyfakefs.fake_filesystem_unittest import TestCase

FILE_PATH = "/foo/bar/tests"
N_FILES_TO_CREATE = 5


class TestFileDuplication(TestCase):
    """Test that all files are found and that the right number of copies are
    created."""

    def setUpClass(self):
        """Prepare fake filesystem."""
        self.setUpPyfakefs()

        self.file_names = [FILE_PATH + str(n_file) + ".txt" for n_file in
                           range(N_FILES_TO_CREATE)]
        for i_file in self.file_names:
            self.fs.create_file(i_file, contents='test')
            print("Creating file: {}".format(i_file))

    def test_get_file_name(self):
        """All files found by get_file_name must be in the file systems and all
        files in the file systems must be found."""
        file_found = get_file_name(FILE_PATH)

        # check all required files are found
        for i_file in self.file_names:
            assert(i_file in file_found)

        # check that all files that are found are also required
        for i_file in file_found:
            assert(i_file in self.file_names)



#
# class FakeFyleSystem(object):
#    @classmethod
#    def setUp(cls):
#
#
# def test_get_file_list_in_folder():
#     """Return a list of files contained in a given folder."""
#     assert (True)
