from azure.storage.filedatalake import DataLakeServiceClient, FileSystemClient, DataLakeDirectoryClient
import logging
import os


def logging_name_function(func):
    def wrap(*args, **kwargs):
        logging.info(f"{func.__name__} has been started")
        func(*args)
        logging.info(f"{func.__name__} has been finished")
    return wrap


class DataLakeG2:
    file_system_client: FileSystemClient
    current_directory: DataLakeDirectoryClient
    directory: DataLakeDirectoryClient
    dict_of_directory: dict
    dict_inh: dict

    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO,
                        filename='DataLakeG2.log',
                        filemode='w')

    def __init__(self, connection_string=os.getenv("AZURE_DT_2"),
                 container_name_="container03",
                 file_name_='IndianFoodDatasetCSV.csv'):
        account_name = os.getenv('STORAGE_ACCOUNT_NAME', "")
        account_key = os.getenv('STORAGE_ACCOUNT_KEY', "")

        # set up the service client with the credentials from the environment variables
        self.service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https",
            account_name
        ), credential=account_key)
        self.file_system_name = container_name_
        self.file_name = file_name_
        self.dict_inh = {}
        self.dict_of_directory = {}

    @logging_name_function
    def create_file_system(self):
        """
            Create file system(Container)
        """
        try:
            self.file_system_client = self.service_client.create_file_system(file_system=self.file_system_name)
            logging.info("Create_file_system - DONE")
        except Exception as ex:
            logging.error("Exception occurred in create_file_system", exc_info=True)
            self.file_system_client = self.service_client.get_file_system_client(file_system=self.file_system_name)

    @logging_name_function
    def create_directory(self, name_directory):
        try:
            directory = self.file_system_client.create_directory(name_directory)
            self.dict_of_directory[name_directory] = directory
            self.dict_inh[name_directory] = []
        except Exception as ex:
            logging.error("Exception occurred in create_directory", exc_info=True)

    @logging_name_function
    def create_subdirectory(self, name_directory, name_subdirectory):
        try:
            self.dict_of_directory[name_subdirectory] = self.dict_of_directory[name_directory].\
                create_sub_directory(name_subdirectory)
            logging.info('get_sub_directory client DONE')
            self.dict_inh[name_directory].append(name_subdirectory)
            self.dict_inh[name_subdirectory] = []
        except Exception as ex:
            logging.error("Exception occurred in create_subdirectory", exc_info=True)


def main():
    dt = DataLakeG2()
    dt.create_file_system()
    dt.create_directory("folder01")
    dt.create_subdirectory('folder01', 'folder02')
    dt.create_subdirectory('folder02', 'folder03')


if __name__ == "__main__":
    main()