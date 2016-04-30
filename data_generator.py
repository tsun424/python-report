import re
import shelve
import time
import file_bean


class DataGenerator:

    def __init__(self, file_path):
        self.file_data = file_bean.FileBean(file_path)
        self.passed_lines_list = []     # lines which have passed the check
        self.result_list = []

    def pre_check(self):
        if self.file_data.file_size > 10:
            print("The file size is over 10 MB, cannot handle.")
            return False
        lines_list = []
        """
        result list, first element is Boolean to indicate
        pass(True) or not(False)
        """
        passed_list = []
        # error messages
        column_errmsg = "The format of line {line_number} is " \
                        "not correct, "
        column_errmsg += "6 columns are requested and they should be " \
                         "separated by one space in one line"
        columns = ["ID", "Gender", "Age", "Sales", "BMI", "Income"]
        errmsg = "The format of {column}({value}) of " \
                 "line {line_number} is not correct."
        try:
            with open(self.file_data.file_name) as f:
                lines_list = f.readlines()
        except IOError:
            print("Could not open the file: "+self.file_path)
            raise
        for i in range(len(lines_list)):
            passed_check = True
            column_list = lines_list[i].split()
            if len(column_list) == 0:
                continue
            if len(column_list) != 6:
                self.insert_result_list(column_errmsg.
                                        format(line_number=(i+1)))
                continue
            # check the format of ID
            if not re.match('^[A-Z][0-9]{3}$', column_list[0]):
                self.insert_result_list(errmsg.
                                        format(column=columns[0],
                                               value=column_list[0],
                                               line_number=(i+1)))
                passed_check = False
            # check the format of Gender
            if not re.match('^(M|F)$', column_list[1]):
                self.insert_result_list(errmsg.
                                        format(column=columns[1],
                                               value=column_list[1],
                                               line_number=(i+1)))
                passed_check = False
            # check the format of Age
            if not re.match('^[0-9]{2}$', column_list[2]):
                self.insert_result_list(errmsg.
                                        format(column=columns[2],
                                               value=column_list[2],
                                               line_number=(i+1)))
                passed_check = False
            # check the format of Sales
            if not re.match('^[0-9]{3}$', column_list[3]):
                self.insert_result_list(errmsg.
                                        format(column=columns[3],
                                               value=column_list[3],
                                               line_number=(i+1)))
                passed_check = False
            # check the format of BMI
            if not re.match('^(Normal|Overweight|Obesity|Underweight)$',
                            column_list[4]):
                self.insert_result_list(errmsg.
                                        format(column=columns[4],
                                               value=column_list[4],
                                               line_number=(i+1)))
                passed_check = False
            # check the format of Income
            if not re.match('^[0-9]{2,3}$', column_list[5]):
                self.insert_result_list(errmsg.
                                        format(column=columns[5],
                                               value=column_list[5],
                                               line_number=(i+1)))
                passed_check = False
            if passed_check:
                passed_list.append(lines_list[i])
        if not self.result_list:
            self.result_list.insert(0, True)
        if passed_list:
            self.insert_shelve(passed_list)
        return self.result_list

    def insert_result_list(self, error_msg):
        if not self.result_list:
            self.result_list.insert(0, False)
        self.result_list.append(error_msg)

    def insert_shelve(self, passed_list):
        db = shelve.open('db.shelve', 'c')
        current_time = time.strftime("%Y%m%d%H%M%S")
        db[current_time] = passed_list
        self.result_list.append(current_time)
        db.close()

if __name__ == '__main__':
    r = DataGenerator('data.txt')
    result = r.pre_check()
    if result[0]:
        print("Congratulations!!!!", ' Result: \n')
        db1 = shelve.open('db.shelve')
        print(db1[result[-1]])
        db1.close()
    else:
        print(result)
