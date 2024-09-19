# MyPyTest

A lite version of PyTest to develop understanding of PyTest and Python.

## Results Class

A singleton to store results with fns to add_result, get_results, get_results_totals.

## Utils.py

fns to colorise display of result in console.

## summary.py and header.py

In testrunner.py, these two files provide header and summary reports.

## read_mypytest.py and mypytest.ini

A config parser to get arguments from mypytest.ini.

## discovery.py 

gets values from mypytest.ini using the config parser from read_mypytest.py to find test directory, filename pattern, class namepattern and test pattern.