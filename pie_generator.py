import a_plot_generator


class PieGenerator(a_plot_generator.APlotGenerator):

    def display_by_sales(self):
        super(PieGenerator, self).display_by_sales('pie', 'Sales data in pie chart', 'sales_pie')

    def display_by_income(self):
        super(PieGenerator, self).display_by_income('pie', 'Income data in pie chart', 'income_pie')

if __name__ == "__main__":
    pie = PieGenerator('20160314233501')
    pie.display_by_sales()
    pie.display_by_income()
