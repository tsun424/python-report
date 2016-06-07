from a_plot_creator import APlotCreator
from pie_generator import PieGenerator


class PieCreator(APlotCreator):

    @staticmethod
    def make_product(serial_number):
        return PieGenerator(serial_number)
