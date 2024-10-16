import os
from time import sleep
from random import randrange

class Helper:
    def create_directory(self, name_directory=''):
        """
        Creates a directory with the specified name if it does not already exist.

        Parameters:
        name_directory (str): The name of the directory to be created. Defaults to an empty string.
        """
        try:
            # Check if the directory does not already exist
            if not os.path.exists(name_directory):
                # Create the directory
                os.mkdir(name_directory)
        except OSError:
            # Handle the case where the directory creation fails (e.g., due to permissions issues)
            ...

    def crate_file(self,filename='',mode='w', data=''):
        with open(file=filename, mode=mode,newline='') as file:
            file.write(data + '\n')

    def remove_duplicate(self,default='', sorted_filename=''):
        with open(file=default, mode='r+') as file:
            source = file.read()
            for i in set(source.split()):
                # print(i)
                with open(file=sorted_filename, mode='a', newline='') as file:
                    file.write(i + '\n')

    def create_file_from_list(self, filename, data_list):
        """
        Create a file from a list of strings.

        Parameters:
        filename (str): The name of the file to be created.
        data_list (list of str): The list of strings to write to the file.
        """
        try:
            with open(file=filename, mode='w',newline='') as file:
                for item in data_list:
                    file.write(f"{item}\n")
            print(f"File '{filename}' created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")



    def random_pause_code(self, start=0, stop=0):
        sleep(randrange(start, stop + 1))

