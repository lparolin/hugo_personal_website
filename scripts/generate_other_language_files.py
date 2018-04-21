"""Generates files for other langauges in the selected folders."""

import os
import sys
import logging
import shutil

FILES_TO_SKIP = ("_index.md",)

# see https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('generated_files_details.log')
file_handler.setLevel(logging.DEBUG)

std_error_handler = logging.StreamHandler(sys.stderr)
std_error_handler.setLevel(logging.INFO)

file_handler.setFormatter(formatter)
std_error_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(std_error_handler)


def get_file_list_in_folder(folder_path):
    """Return a list of files contained in a given folder."""
    file_list = [file_to_add for file_to_add in os.listdir(folder_path) if
                 is_to_be_added(os.path.join(folder_path, file_to_add))]
    if not file_list:
        logger.warning("No files found.")
    else:
        logger.info("File found: %s", ",".join(file_list))
    return file_list


def is_to_be_added(file_to_be_checked):
    """Return true if the file at file_to_be_checked should be added to the
    list of observed files. False otherwise."""
    file_path, file_name = os.path.split(file_to_be_checked)
    base_name, extension = os.path.splitext(file_name)
    is_file_to_be_added = file_name not in FILES_TO_SKIP and \
        os.path.isfile(file_to_be_checked) and \
        extension == ".md"

    if not is_file_to_be_added:
        logger.debug("File %s not added", file_to_be_checked)
    if is_file_to_be_added:
        logger.debug("File %s marked as to be added", file_to_be_checked)
    return is_file_to_be_added

def replicate_file(file_src, token_list):
    """Replicate a given file and append a token to its name."""

    file_path, file_name = os.path.split(file_src)
    base_name, extension = os.path.splitext(file_name)
    logger.debug("src_path: %s, src_base_name: %s, src_extension: %s",
                 file_path, base_name, extension)
    created_files = []
    for i_token in token_list:
        new_file_name = base_name + i_token + extension
        logger.info("Creating new file: %s", new_file_name)
        file_dst = os.path.join(file_path, new_file_name)
        shutil.copyfile(file_src, file_dst)
        created_files.append(file_dst)

    return created_files


if __name__ == '__main__':
    # parameters = sys.argv
    # if len(parameters) is not 3:
    #     log.error("Wrong number of input paramters. Expected 3 got %d",
    #               len(parameters))
    #     sys.exit("""Wrong number of input paramters. Use the following syntax to execute the script:")
    #         python generate_other_language_files.py <path_fo_src_files> <language_token>
    #     """)

    # folder = parameters[1]
    # extension = parameters[2]
    folder = "../content/publication"
    language_token = ("_it", "_de")
    file_src = get_file_list_in_folder(folder)
    for i_file in file_src:
        replicate_file(i_file, language_token)
