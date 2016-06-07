"""
>>> import data_generator
>>> dg = data_generator.DataGenerator('data.txt')
>>> dg.pre_check() #doctest: +ELLIPSIS
[True, '...']
>>> dg1 = data_generator.DataGenerator('test.txt')
>>> dg1.pre_check() #doctest: +ELLIPSIS
[False, 'The format of Income(aa) of line 23 is not correct.', '...']
>>> import bar_generator
>>> bg = bar_generator.BarGenerator('20160316090613')
>>> bg.display_by_sales()
>>> bg.display_by_income()
>>> bg.display_income_sales()
>>> import pie_generator
>>> pg = pie_generator.PieGenerator('20160316090613')
>>> pg.display_by_income()
>>> pg.display_by_sales()
>>> from bar_creator import BarCreator
>>> bg2 = BarCreator.make_product('20160316090613')
>>> bg2.display_by_sales()
>>> from pie_creator import PieCreator
>>> pg2 = PieCreator.make_product('20160316090613')
>>> pg2.display_by_income()
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
