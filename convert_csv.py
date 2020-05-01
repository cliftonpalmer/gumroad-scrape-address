import sys
import csv

stamps_fieldnames_dynamic = {
    'Order ID': 'Order Number',
    'Order Date': 'Purchase Date',
    'Order Value': 'Net Total ($)',
    'Ship To - Name': 'Buyer Name',
    'Ship To - Address 1': 'Street Address',
    'Ship To - State/Province': 'State',
    'Ship To - City': 'City',
    'Ship To - Postal Code': 'Zip Code',
    'Ship To - Country': 'Country',
    'Ship To - Email': 'Buyer Email',
    'Notes - Internal': 'Variants',
    }
stamps_fieldnames_static = {
    'Total Weight in Oz': '4',
    'Dimensions - Length': '11',
    'Dimensions - Width': '8.5',
    'Dimensions - Height': '0.5',
    }

stamps_fieldnames = stamps_fieldnames_dynamic.keys() + \
        stamps_fieldnames_static.keys()

reader = csv.DictReader(sys.stdin)
writer = csv.DictWriter(sys.stdout, fieldnames=stamps_fieldnames)

writer.writeheader()
for read_row in reader:
    write_row = stamps_fieldnames_static.copy() 
    for key in stamps_fieldnames_dynamic:
        gumroad_key = stamps_fieldnames_dynamic[key]
        write_row[key] = read_row[gumroad_key]
    writer.writerow(write_row)
