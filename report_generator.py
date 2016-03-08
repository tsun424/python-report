from os.path import getsize


class ReportGenerator:

    def __init__(self, file_path):
        self.file_path = file_path      # the file path
        self.file_size = 0.0            # file size
        try:
            self.file_size = (getsize(self.file_path)/1024/1024)
        except FileNotFoundError:
            print("The file "+self.file_path+" doesn't exist")
            raise
        self.passed_lines_list = []     # lines which have passed the check

    def pre_check(self):
        if self.file_size > 10:
            print("The file size exceed 10 MB, cannot handle")
            return False
        lines_list = []
        result_list = []    # result list, first element is Boolean to indicate pass(True) or not(False)
        try:
            with open(self.file_path) as f:
                lines_list = f.readlines()
        except IOError:
            print("Could not open the file: "+self.file_path)
        # error messages
        column_error = "The format of line {line_number} is not correct, "
        column_error += "6 columns which are separated by one space in one line"
        for i in range(len(lines_list)):
            column_list = lines_list[i].split()
            if len(column_list) != 6:
                print(column_error.format(line_number=(i+1)))
