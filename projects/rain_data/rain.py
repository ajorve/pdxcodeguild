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


import json
import requests
from datetime import datetime

