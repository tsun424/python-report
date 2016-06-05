import plotly
import plotly.graph_objs as go
import a_plot_generator


class BarGenerator(a_plot_generator.APlotGenerator):

    def __init__(self, serial_no=''):
        a_plot_generator.APlotGenerator.__init__(self, serial_no)

    def prepare_sales_figure(self, label_list, value_list):
        fig = {"data": [go.Bar(x=label_list, y=value_list, name='Sales')],
               "layout": go.Layout(title="Sales data by bar chart")}
        return fig, 'sales_bar.html'

    def prepare_income_figure(self, label_list, value_list):
        fig = {"data": [go.Bar(x=label_list, y=value_list, name='Income')],
               "layout": go.Layout(title="Income data by bar chart")}
        return fig, "income_bar.html"

    def display_income_sales(self):
        x_list = []
        y_list = []
        for k, v in self.sales_data.items():
            x_list.append(k)
            y_list.append(v)
        sales_plot = go.Bar(x=x_list, y=y_list, name='Sales')
        x_list = []
        y_list = []
        for k, v in self.income_data.items():
            x_list.append(k)
            y_list.append(v)
        income_plot = go.Bar(x=x_list, y=y_list, name='Income')
        data = [sales_plot, income_plot]
        layout = go.Layout(barmode='group',
                           title="Sales and Income data by bar chart")
        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename="sales_income_bar.html")

if __name__ == "__main__":
    bar = BarGenerator('20160314233501')
    bar.display_by_sales()
    bar.display_by_income()
    bar.display_income_sales()
