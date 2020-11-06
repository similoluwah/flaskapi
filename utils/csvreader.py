import csv

def readCSV(filepath):
    with open(filepath, encoding="utf8", errors='ignore' ) as csvfile:
        content = csv.reader(csvfile, delimiter=',')

        next(content)
        return [ {"phone_number" : int(float(row[0])), "run_time" : row[1].replace("/","-")} for row in content if not any(len(str(x))==0 for x in row)]