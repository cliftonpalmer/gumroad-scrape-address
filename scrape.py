import sys
import csv

address = """{Buyer Name}
{Street Address}
{City}, {State} {Zip Code}
"""

reader = csv.DictReader(sys.stdin)
for row in reader:
    print address.format(**row)
