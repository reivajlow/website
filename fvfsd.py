import csv
with open('C:/Users/javoe/OneDrive/Escritorio/datos') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
             print(row)