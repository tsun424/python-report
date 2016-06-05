from a_plot_factory import APlotFactory
from bar_generator import BarGenerator
from pie_generator import PieGenerator


class PlotFactory(APlotFactory):

    @staticmethod
    def create_bar(serial_number):
        return BarGenerator(serial_number)

    @staticmethod
    def create_pie(serial_number):
        return PieGenerator(serial_number)
