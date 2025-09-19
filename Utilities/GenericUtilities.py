import os
import psutil
import shutil
import subprocess
import socket


class GenericUtilities:
    """
    Funções para executar operações genéricas relacionadas ao sistema operacional ou ao ambiente, como abrir e encerrar processos, etc.
    """

    @classmethod
    def check_process_status(cls, process_name):
        """
        Para verificar se um processo já está em execução antes de iniciá-lo ou encerrá-lo.
        :param process_name: Nome do processo com extensão como WinAppDriver.exe
        :return: Verdadeiro se o processo estiver em execução, caso contrário, Falso.
        """
        for process in psutil.process_iter():
            if process.name() == process_name:
                return True
        return False

    @classmethod
    def terminate_process(cls, process_name):
        """
        Para encerrar um processo em execução.
        :param process_name: Nome do processo com extensão como WinAppDriver.exe
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
        Para ler o valor de uma variável de ambiente do sistema.
        :param var_name: Nome da variável de ambiente a ser lida.
        :return: valor da variável de ambiente definida no sistema.
        """
        var_value = os.environ.get(var_name)
        if var_value is None:
            print(f"Environment variable {var_name} not found.")
        return var_value


    @classmethod
    def find_available_port(cls, start_port, num_ports_to_check):
        """
        Encontre uma porta disponível no intervalo de portas fornecido no localhost.
        :param start_port: número da porta para iniciar a busca, exemplo: 7900
        :param num_ports_to_check: número de portas a serem verificadas, 10, 20 etc.
        :return: [int] número da porta disponível.
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
        Copia arquivos de um diretório de origem para um diretório de destino.
        Se o arquivo existir no diretório de destino, ele será substituído pelo arquivo de origem.
        :param source_dir: Caminho completo do diretório de origem.
        :param destination_dir: Caminho completo do diretório de destino.
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
