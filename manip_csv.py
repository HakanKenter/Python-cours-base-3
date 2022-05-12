import argparse
import csv

parser = argparse.ArgumentParser(description="Exemple d'utilisation d'argument parser.")
parser.add_argument("-f", "--file", dest="filename", default="data/survey-financial.csv")

args = parser.parse_args()

# print(args)
f = open(args.filename, "r")
reader = csv.reader(f)

print(dir(reader))
# print(sizeof(reader))

for row in reader:
    for item in row:
        print(item)

f.close()
print("Done")