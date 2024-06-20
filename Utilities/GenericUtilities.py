import os
import psutil
import shutil
import subprocess
import socket


class GenericUtilities:
    """
    - Functions to perform generic OS or environment related operations like open and terminate process etc.
    """

    @classmethod
    def check_process_status(cls, process_name):
        """
        - To check whether a process is already running before starting or terminating it.
        :param process_name: Name of the process with extension like WinAppDriver.exe
        :return: True if process is running else False.
        """
        for process in psutil.process_iter():
            if process.name() == process_name:
                return True
        return False

    @classmethod
    def terminate_process(cls, process_name):
        """
        - To terminate a running process.
        :param process_name: Name of the process with extension like WinAppDriver.exe
        :return:
        """
        if cls.check_process_status(process_name):
            try:
                subprocess.run(f'taskkill /F /IM {process_name}', check=True, shell=True)
            except subprocess.CalledProcessError as e:
                print(f"Error terminating process: {e}")
        else:
            print(f"{process_name} is not running.")

    @classmethod
    def read_environ_variable(cls, var_name):
        """
        - To read value of an environment variable from the system.
        :param var_name: Name of the environment variable to read.
        :return: value of the environment variable defined in the system.
        """
        var_value = os.environ.get(var_name)
        if var_value is None:
            print(f"Environment variable {var_name} not found.")
        return var_value

    @classmethod
    def directory_clean_up(cls, dir_path):
        """
        - Delete directory and it's content including sub-folders.
        :param dir_path: Directory full path.
        :return:
        """
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path, ignore_errors=True)
            print(f"Directory: {dir_path} cleaned.")
        else:
            print(f"Directory: {dir_path} not found.")

    @classmethod
    def find_available_port(cls, start_port, num_ports_to_check):
        """
        - Find an available port from the given range of ports on localhost.
        :param start_port: port number to start searching from, example: 7900
        :param num_ports_to_check: number of ports to check, 10, 20 etc.
        :return: [int] available port number.
        """
        for port in range(start_port, start_port + num_ports_to_check):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                try:
                    s.bind(('localhost', port))
                    return port
                except OSError:
                    continue
        raise RuntimeError("Unable to find an available port")

    @classmethod
    def copy_files(cls, source_dir, destination_dir):
        """
        - Copies files from a source to destination directory.
            If file exist in destination directory, it will be overridden by file from source.
        :param source_dir: Full path of source directory.
        :param destination_dir: Full path of destination directory.
        :return:
        """
        if os.path.isdir(source_dir) and os.path.isdir(destination_dir):
            files = os.listdir(source_dir)

            for file in files:
                source_file = os.path.join(source_dir, file)
                destination_file = os.path.join(destination_dir, file)

                if os.path.isfile(destination_file):
                    os.remove(destination_file)

                shutil.copy(source_file, destination_file)
        else:
            print(f"directory{source_dir} or {destination_dir} doesn't exist.")
