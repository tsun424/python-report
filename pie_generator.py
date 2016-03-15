import plotly
import plotly.graph_objs as go
import a_plot_generator


class PieGenerator(a_plot_generator.APlotGenerator):

    def display_by_sales(self):
        label_list = []
        value_list = []
        for k, v in self.sales_data.items():
            label_list.append(k)
            value_list.append(v)
        fig = {'data': [{'labels': label_list,
                         'values': value_list,
                         'type': 'pie'}],
               'layout': {'title': 'Sales data in pie chart'}
               }
        plotly.offline.plot(fig, filename="sales_pie")

    def display_by_income(self):
        label_list = []
        value_list = []
        for k, v in self.income_data.items():
            label_list.append(k)
            value_list.append(v)
        fig = {'data': [{'labels': label_list,
                         'values': value_list,
                         'type': 'pie'}],
               'layout': {'title': 'Income data in pie chart'}
               }
        plotly.offline.plot(fig, filename="income_pie")

if __name__ == "__main__":
    pie = PieGenerator('20160314233501')
    pie.display_by_sales()
    pie.display_by_income()
