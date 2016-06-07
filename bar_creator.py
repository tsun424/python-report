from a_plot_creator import APlotCreator
from bar_generator import BarGenerator


class BarCreator(APlotCreator):

    @staticmethod
    def make_product(serial_number):
        return BarGenerator(serial_number)
