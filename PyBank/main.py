import csv
import os
py_bank = os.path.join("../Resources", "pybank.csv")


with open(py_bank) as pybank_file:
    csv_reader = csv.reader(pybank_file)

