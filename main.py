import os
from BdsBlob import BdsBlob


'''AZURE_STORAGE_CONNECTION_STRING'''
'''AZURE_STORAGE_CONNECTION_BDS'''
'''AZURE_STORAGE_CONNECT_STRING'''


def main():
    connect_str = os.getenv('AZURE_STORAGE_CONNECT_STRING')
    bds = BdsBlob(connect_str, container_name_="trotsenkodaniil")
    bds.task()
    bds.get_containers()


if __name__ == "__main__":
    main()
