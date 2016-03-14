from os.path import getsize
import re
import shelve
import time


class DataGenerator:

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
            print("The file size is over 10 MB, cannot handle.")
            return False
        lines_list = []
        result_list = []    # result list, first element is Boolean to indicate pass(True) or not(False)
        passed_list = []
        # error messages
        column_errmsg = "The format of line {line_number} is not correct, "
        column_errmsg += "6 columns which are separated by one space in one line"
        columns = ["ID", "Gender", "Age", "Sales", "BMI", "Income"]
        errmsg = "The format of {column}({value}) of line {line_number} is not correct."
        try:
            with open(self.file_path) as f:
                lines_list = f.readlines()
        except IOError:
            print("Could not open the file: "+self.file_path)
            raise
        for i in range(len(lines_list)):
            column_list = lines_list[i].split()
            if len(column_list) != 6:
                if not result_list:
                    result_list.insert(0, False)
                result_list.append(column_errmsg.format(line_number=(i+1)))
                continue
            # check the format of ID
            if not re.match('^[A-Z][0-9]{3}$', column_list[0]):
                if not result_list:
                    result_list.insert(0, False)
                result_list.append(errmsg.format(column=columns[0], value=column_list[0], line_number=(i+1)))
            # check the format of Gender
            if not re.match('^(M|F)$', column_list[1]):
                if not result_list:
                    result_list.insert(0, False)
                result_list.append(errmsg.format(column=columns[1], value=column_list[1], line_number=(i+1)))
            # check the format of Age
            if not re.match('^[0-9]{2}$', column_list[2]):
                if not result_list:
                    result_list.insert(0, False)
                result_list.append(errmsg.format(column=columns[2], value=column_list[2], line_number=(i+1)))
            # check the format of Sales
            if not re.match('^[0-9]{3}$', column_list[3]):
                if not result_list:
                    result_list.insert(0, False)
                result_list.append(errmsg.format(column=columns[3], value=column_list[3], line_number=(i+1)))
            # check the format of BMI
            if not re.match('^(Normal|Overweight|Obesity|Underweight)$', column_list[4]):
                if not result_list:
                    result_list.insert(0, False)
                result_list.append(errmsg.format(column=columns[4], value=column_list[4], line_number=(i+1)))
            # check the format of Income
            if not re.match('^[0-9]{2,3}$', column_list[5]):
                if not result_list:
                    result_list.insert(0, False)
                result_list.append(errmsg.format(column=columns[5], value=column_list[5], line_number=(i+1)))
            if not result_list:
                passed_list.append(lines_list[i])
        if not result_list:
            result_list.insert(0, True)
        if passed_list:
            db = shelve.open('db.shelve', 'c')
            current_time = time.strftime("%Y%m%d%H%M%S")
            db[current_time] = passed_list
            result_list.append(current_time)
            db.close()
        return result_list

if __name__ == '__main__':
    r = ReportGenerator('test.txt')
    result = r.pre_check()
    if result[0]:
        print("Congratulations!!!!",' Result: \n')
        db1 = shelve.open('db.shelve')
        print(db1[result[-1]])
        db1.close()
    else:
        print(result)
