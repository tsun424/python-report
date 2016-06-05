import cmd
import data_generator
import shelve
import pie_creator
import sys
from bar_creator import BarCreator
from pie_creator import PieCreator


class ReportCmd(cmd.Cmd):
    """
    report line-oriented command class
    commands: report, recheck, ls, show, quit
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>>"

    def do_report(self, file_path=''):
        """
        import data from a text file, generate according format of reports
        then show it in a broswer
        command format:
        report xxx.txt  xxx.txt is the file absolute path, for example,
                        E:/data.txt
        report          if there is no file path, will request customer to
                        input later or use default file 'data.txt'
        :param file_path: the text file location
        :return: None
        """
        if not file_path:
            msg = "The file is not given, default file 'data.txt' will be " \
                  "used if you input Enter,\n otherwise, please input " \
                  "the file name which you want to handle: "
            file_path = input(msg)
            if not file_path:
                file_path = 'data.txt'
        report = data_generator.DataGenerator(file_path)
        result_list = report.pre_check()
        if result_list[0]:
            print("Congratulations!!!!",
                  ' Report has been generated successfully.')
            serial_number = result_list[-1]
            self.__show_report(serial_number)
        else:
            print("The format of file doesn't meet criteria, details: ")
            for result_str in result_list[1:-1]:
                print(result_str)
            if_continue = input("continue to generate the report or "
                                "exit? Please enter yes(y) or no(n):")
            if if_continue in ['', 'yes', 'y']:
                self.__show_report(result_list[-1])
            elif if_continue in ['no', 'n']:
                sys.exit()

    @staticmethod
    def do_precheck(file_path=''):
        """
        only precheck a text file if all lines meet criteria,
        won't show a report in broswer
        command format:
        precheck xxx.txt  xxx.txt is the file absolute path
        precheck          if there is no file path,
                          will request customer to input later

        :param file_path: the text file absolute location
        :return: None
        """
        if not file_path:
            file_path = input("Please input the file path: ")
        report = data_generator.DataGenerator(file_path)
        result_list = report.pre_check()
        if result_list[0]:
            print("Congratulations!!!!",
                  ' The serial number is: ', result_list[-1])
        else:
            print("Sorry, the format of file doesn't meet criteria, details: ")
            for result_str in result_list[1:-1]:
                print(result_str)

    @staticmethod
    def do_ls(db_name='db.shelve'):
        """
        list all available serial numbers in shelve, which are ordered by time
        :param db_name: a string to show the shelve name
        :return: None
        """
        if db_name == '':
            db_name = 'db.shelve'
        serial_nos = []
        db = shelve.open(db_name)
        for item in db:
            serial_nos.append(int(item))
        serial_nos.sort()
        print(*serial_nos, sep="\n")
        db.close()

    @staticmethod
    def do_quit(message='Exit...'):
        """
        Quit from my CMD
        :param message: a message output during exit
        :return: True
        """
        print('Exit...')
        return True

    def do_show(self, serial_number=''):
        """
        request user to input one serial number
        and show a related report in broswer. A serial number
        is a key of data in shelve, which is a timestamp as well
        command format:
        show serial_number
        show         if a serial_number will be requested if it is not set
        :param serial_number: a string which is the key of data in shelve
        :return: None
        """
        if serial_number == '':
            serial_number = input("Please input a serial number: ")
        self.__show_report(serial_number)

    @staticmethod
    def __show_report(serial_number):
        """
        show report menu and request user to choose which report is to be
        generated and shown
        :param: serial_number: a string which is the key of data in shelve
        :return:
        """
        bar = BarCreator.make_product(serial_number)
        pie = PieCreator.make_product(serial_number)
        msg = "Please choose report number:\n press 1: sales by bar chart\n " \
              "press 2: sales by pie chart\n press 3: income by bar chart\n " \
              "press 4: income by pie chart\n " \
              "press 5: income and sales by bar chart\n"
        report_number = input(msg)
        if report_number == "1":
            bar.display_by_sales()
        elif report_number == "2":
            pie.display_by_sales()
        elif report_number == "3":
            bar.display_by_income()
        elif report_number == "4":
            pie.display_by_income()
        elif report_number == "5":
            bar.display_income_sales()


if __name__ == '__main__':
    quitter = ReportCmd()
    quitter.cmdloop()
