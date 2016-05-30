import a_plot_generator


class PieGenerator(a_plot_generator.APlotGenerator):

    def prepare_sales_figure(self, label_list, value_list):
        fig = {'data': [{'labels': label_list,
                        'values': value_list,
                         'type': 'pie'}],
               'layout': {'title': 'Sales data in pie chart'}}
        return fig, 'sales_pie'

    def prepare_income_figure(self, label_list, value_list):
        fig = {'data': [{'labels': label_list,
                        'values': value_list,
                         'type': 'pie'}],
               'layout': {'title': "Income data in pie chart"}}
        return fig, "income_pie"

if __name__ == "__main__":
    pie = PieGenerator('20160314233501')
    pie.display_by_sales()
    # pie.display_by_income()
