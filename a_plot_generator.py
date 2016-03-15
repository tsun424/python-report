import shelve
from collections import OrderedDict


class APlotGenerator:

    def __init__(self, serial_number=''):
        db = shelve.open("db.shelve")
        try:
            self.db_data = db[serial_number]
        except KeyError:
            print("There is no such serial number("+serial_number+") in shelve, please input a correct serial number")
            raise
        self.sales_data = OrderedDict([("0-99", 0), ("100-199", 0), ("200-299", 0), ("300-399", 0), ("400-499", 0), ("500-599", 0), ("600-699", 0), ("700-799", 0)])
        self.sales_data["800-899"] = 0
        self.sales_data["900-999"] = 0
        self.income_data = OrderedDict([("0-99", 0), ("100-199", 0), ("200-299", 0), ("300-399", 0), ("400-499", 0), ("500-599", 0), ("600-699", 0), ("700-799", 0)])
        self.income_data["800-899"] = 0
        self.income_data["900-999"] = 0
        db.close()
        self.generate_sales()
        self.generate_income()

    def generate_sales(self):
        for line in self.db_data:
            sale = int(line.split()[3])
            if 0 <= sale <= 99:
                self.sales_data["0-99"] += 1
            elif 100 <= sale <= 199:
                self.sales_data["100-199"] += 1
            elif 200 <= sale <= 299:
                self.sales_data["200-299"] += 1
            elif 300 <= sale <= 399:
                self.sales_data["300-399"] += 1
            elif 400 <= sale <= 499:
                self.sales_data["400-499"] += 1
            elif 500 <= sale <= 599:
                self.sales_data["500-599"] += 1
            elif 600 <= sale <= 699:
                self.sales_data["600-699"] += 1
            elif 700 <= sale <= 799:
                self.sales_data["700-799"] += 1
            elif 800 <= sale <= 899:
                self.sales_data["800-899"] += 1
            elif 900 <= sale <= 999:
                self.sales_data["900-999"] += 1

    def generate_income(self):
        for line in self.db_data:
            income = int(line.split()[5])
            if 0 <= income <= 99:
                self.income_data["0-99"] += 1
            elif 100 <= income <= 199:
                self.income_data["100-199"] += 1
            elif 200 <= income <= 299:
                self.income_data["200-299"] += 1
            elif 300 <= income <= 399:
                self.income_data["300-399"] += 1
            elif 400 <= income <= 499:
                self.income_data["400-499"] += 1
            elif 500 <= income <= 599:
                self.income_data["500-599"] += 1
            elif 600 <= income <= 699:
                self.income_data["600-699"] += 1
            elif 700 <= income <= 799:
                self.income_data["700-799"] += 1
            elif 800 <= income <= 899:
                self.income_data["800-899"] += 1
            elif 900 <= income <= 999:
                self.income_data["900-999"] += 1

    def display_by_sales(self):
        pass

    def display_by_income(self):
        pass