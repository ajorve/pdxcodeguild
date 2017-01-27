"""
DateTime Practice

Take 2 dates and find the time that has passed between them.

"""

from datetime import datetime



def date_time():
    the_date = '2012/09/18 23:40:00'
    another_date = '2013/09/12 2:00:32'

    the_date = datetime.strptime(the_date, '%Y/%m/%d %H:%M:%S')
    another_date = datetime.strptime(another_date, '%Y/%m/%d %H:%M:%S')

    delta = str(the_date - another_date)

    print(delta)

date_time()