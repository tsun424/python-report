import cmd
import data_generator
import shelve


class ReportCmd(cmd.Cmd):
    """
    report command class
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>>"

    def do_report(self, file_path=''):
        """
        import date from a text file and generate according format of reports
        command format:
        report xxx  xxx is the file absolute path
        report      if there is no file path, will request customer to input later

        :param file_path: the text file location
        :return:
        """
        if not file_path:
            file_path = input("Please input the file path: ")
        report = data_generator.DataGenerator(file_path)
        result_list = report.pre_check()
        if result_list[0]:
            print("Congratulations!!!!", ' Result: \n')
            db1 = shelve.open('db.shelve')
            print(db1[result_list[-1]])
        else:
            print("The format of file doesn't meet criteria, details: ")
            for result_str in result_list[1:-1]:
                print(result_str)
            if_continue = input("continue to generate the report or exit? Please enter yes(y) or no(n):")
            if if_continue in ['', 'yes', 'y']:
                db1 = shelve.open('db.shelve')
                print(db1[result_list[-1]])
                db1.close()
            else:
                self.do_quit()

    @staticmethod
    def do_precheck(file_path=''):
        """
        precheck the text file only
        command format:
        precheck xxx  xxx is the file absolute path
        precheck      if there is no file path, will request customer to input later

        :param file_path: the text file location
        :return:
        """
        if not file_path:
            file_path = input("Please input the file path: ")
        report = data_generator.DataGenerator(file_path)
        result_list = report.pre_check()
        if result_list[0]:
            print("Congratulations!!!!", ' The serial number is: ', result_list[-1])
        else:
            print("Sorry, the format of file doesn't meet criteria, details: ")
            for result_str in result_list[1:-1]:
                print(result_str)

    @staticmethod
    def do_quit(message='Exit...'):
        """
        Quit from my CMD

        :param message: message output during exit
        :return: True
        """
        print(message)
        return True


if __name__ == '__main__':
    quitter = ReportCmd()
    quitter.cmdloop()
