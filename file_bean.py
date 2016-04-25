from os.path import getsize


class FileBean:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_size = 0.0
        try:
            self.file_size = (getsize(self.file_name)/1024/1024)
        except FileNotFoundError:
            print("The file "+self.file_name+" doesn't exist")
            raise
