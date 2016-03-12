import cmd
import report_generator
import shelve


class ReportCmd(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>>"

    @staticmethod
    def do_report(file_path=''):
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
        report = report_generator.ReportGenerator(file_path)
        result_list = report.pre_check()
        if result_list[0]:
            print("Congratulations!!!!",' Result: \n')
            db1 = shelve.open('db.shelve')
            print(db1[result_list[-1]])
        else:
            print(result_list)

    @staticmethod
    def do_quit(message=''):
        """
        Quit from my CMD

        :param message: message output during exit
        :return: True
        """
        print("Exit.", message)
        return True


if __name__ == '__main__':
    quitter = ReportCmd()
    quitter.cmdloop()