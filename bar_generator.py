import pygal
import webbrowser
import a_plot_generator


class BarGenerator(a_plot_generator.APlotGenerator):

    def display_by_sales(self):
        bar_chart = pygal.Bar()                                     # Then create a bar graph object
        bar_chart.title = "Display by sales"
        bar_chart.x_labels = self.sales_data.keys()
        bar_chart.add('Sales', self.sales_data.values())            # Add some values
        bar_chart.render_to_file('sales_bar_chart.svg')             # Save the svg to a file
        webbrowser.open_new('sales_bar_chart.svg')

if __name__ == "__main__":
    bar = BarGenerator('20160314233501')
    bar.display_by_sales()
