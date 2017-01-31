"""
# Practice: Rain

The city of Portland has rain gauges that keep track of rainfall.
[A website](http://or.water.usgs.gov/non-usgs/bes/) has text data tables the history of all the daily measurements at these gauges.

It looks like:

```
            Daily  Hourly data -->
   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

```

The amounts are in hundredths of inches or are a `-` if the sensor was broken.

Print out a summary of the data:

* The specific date with the most rain.
* The year with the most rain.

You will have to slice out the header lines from all the lines you read.
Remember, the header has a totally different format.
You can split a string by whitespace into a list of strings using `str.split()`.
You will also have to slice out the date and daily total from each of those lists of strings.
If there are any days with `-` for data, explicitly drop them from your dataset.

Avoid using un-named "pairs" outside of dictionaries.
If you need to group together individual instances of a date and a rainfall amount, use a named tuple.

"""


def open_file(filename):
    with open(filename) as requested_file:
        text = requested_file.read()
        return text


def data_collection():

    raw_data = open_file('./sample.rain')[290::]

    data = raw_data.split('\n')[11:]

    data_list = list()

    for line_sum in data:
        try:
            data_list.append(list((line_sum[0:11], int(line_sum[14:17]))))
        except ValueError:
            continue

    return data_list


def helper(data_list):
    return data_list[1]


def rain(data_list):
    highest_rain_date = max(data_list, key=helper)

    years_dict = dict()

    for day in data_list:

        total = day[1]
        year = day[0].split('-')[-1]
        try:
            years_dict[year].append(total)
        except KeyError:
            years_dict[year] = [total]

    years_dict = {year: sum(daily_totals) for year, daily_totals in years_dict.items()}

    highest_rain_year = max(years_dict.items(), key=lambda t: t[1])

    return highest_rain_date, highest_rain_year


def run_program():
    data_list = data_collection()
    day, year = rain(data_list) #unpacks highest_rain_date to day and highest_rain_year to year
    print(f'The specific date with the most rain is {day[0]} with {day[1]} hundredths of an inch of rain.')
    print(f'The year with the most rain is {year[0]}, with {year[1]} hundredths of an inch of rain.')

if __name__ == "__main__":
    run_program()