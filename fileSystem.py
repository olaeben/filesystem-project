import random
import string
from pathlib import Path
import logging


class Logger:
    """
    Handles logging configuration for the script.

    The logger is set up to output logs to both a
    file (`filesystem_loader.log`)and the console.
    The logging level is set to `INFO`, which
    captures all informational messages and above
    (including warnings, errors, and critical messages).
    """

    @staticmethod
    def configure_logging():
        """
        Configures the logging settings for the script.

        Sets up logging to output messages to a log file
        (`filesystem_loader.log`) and the console with a
        specific format that includes the timestamp, log level,
        and the log message.

        Returns:
            None
        """
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s '
                                   '- %(message)s',
                            handlers=[logging.FileHandler
                                      ('filesystem_loader.log'),
                                      logging.StreamHandler()])


class FileGenerator:
    """
    Generates random files with specified size and content.

    The `FileGenerator` class provides functionality to
    create files filled with random content. The size
    of the files can be customized by specifying minimum
    and maximum size limits.

    Attributes:
        min_size_kb (int): The minimum size of the
        generated files in kilobytes (default is 4 KB).
        max_size_kb (int): The maximum size of the generated
        files in kilobytes (default is 1024 KB).
    """
    def __init__(self, min_size_kb=4, max_size_kb=1024):
        """
        Initializes the FileGenerator with size constraints.

        Args:
            min_size_kb (int): The minimum size of the generated
            files in kilobytes (default is 4 KB).
            max_size_kb (int): The maximum size of the generated
            files in kilobytes (default is 1024 KB).

        Returns:
            None
        """
        self.min_size_kb = min_size_kb
        self.max_size_kb = max_size_kb

    def generate_random_content(self, size_kb):
        """
        Generates random text content for a file.

        This method generates a string of random alphanumeric
        characters to fill a file with a specified size.

        Args:
            size_kb (int): The size of the content to generate
            in kilobytes.

        Returns:
            str: A string containing random alphanumeric content
            of the specified size.
        """
        size_bytes = size_kb * 1024
        return ''.join(random.choices(string.ascii_letters
                                      + string.digits, k=size_bytes))

    def create_file(self, file_path):
        """
        Creates a file with random content at the specified path.

        This method generates a file at the given file path with
        a random content size between the specified minimum and
        maximum size limits.

        Args:
            file_path (str or Path): The path where the file will
            be created.

        Returns:
            None
        """
        size_kb = random.randint(self.min_size_kb, self.max_size_kb)
        content = self.generate_random_content(size_kb)
        with open(file_path, 'w') as file:
            file.write(content)
        logging.info(f"File created: {file_path} ({size_kb} KB)")


class FileSystemLoader:
    """
    Class to handle the creation of a simulated file system
    with a specified number of files and directories.
    The files are generated with random sizes and contents.

    Attributes:
        root_path (Path): The root directory where the file
        system will be created.
        num_files (int): The total number of files to be
        created across all directories.
        min_size (int): The minimum size (in bytes) for
        the generated files.
        max_size (int): The maximum size (in bytes) for
        the generated files.
    """

    def __init__(self, root_path, num_files=10_000):
        """
        Initializes the FileSystemLoader with the specified parameters.

        Args:
            root_path (str): The root directory path where the
            file system structure starts.
            num_files (int): The total number of files to be created.
            min_size (int): The minimum file size in bytes.
            max_size (int): The maximum file size in bytes.
        """
        self.root_path = Path(root_path)
        self.num_files = num_files
        self.file_generator = FileGenerator()

    def create_directories(self, current_path, level):
        """
        Recursively creates a directory tree with a specific structure.

        Args:
            path (Path): The current path where directories
            are being created.
            level (int): The current depth level of the
            directory tree.

        Returns:
            None
        """
        if level > 5:
            return
        for i in range(1, 11):
            dir_name = f"dir{level}_{i}"
            dir_path = current_path / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Directory created: {dir_path}")
            self.create_files_in_directory(dir_path)
            self.create_directories(dir_path, level + 1)

    def create_files_in_directory(self, directory):
        """
        Creates files with random content and sizes
        within a specified directory.

        Args:
            dir_path (Path): The path where files should be created.

        Returns:
            None
        """
        for i in range(self.num_files):
            file_name = f"file_{i + 1}.txt"
            file_path = directory / file_name
            self.file_generator.create_file(file_path)

    def load_filesystem(self):
        """
        Loads the entire file system by creating the
        required directories and files based on the
        initialized parameters.

        Returns:
            None
        """
        self.create_directories(self.root_path, 1)


if __name__ == "__main__":
    Logger.configure_logging()

    root_dir = "/Users/waleibitoye/Hitachi_Test"
    loader = FileSystemLoader(root_dir)
    loader.load_filesystem()
