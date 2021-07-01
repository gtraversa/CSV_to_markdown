
import csv
with open('Markdown.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    s = '|'
    with open('converted.txt', 'a') as conv:
        for row in csv_reader:
            if line_count <2:
                conv.write(row[0]+ '\n')
            elif line_count == 2:
                conv.write(s.join(row)+ '\n')
            else:
                conv.write(s.join(row)+ s+'\n')
            line_count+= 1