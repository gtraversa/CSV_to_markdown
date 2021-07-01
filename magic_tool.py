import csv
def converter(path):
    try:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            s = '|'
            path = path.replace(path.split('/')[-1],'')+'converted.txt'
            print(path)
            with open(path , 'a') as conv:
                for row in csv_reader:
                    if line_count <2:
                        conv.write(row[0]+ '\n')
                    elif line_count == 2:
                        conv.write(s.join(row)+ '\n')
                    else:
                        conv.write(s.join(row)+ s+'\n')
                    line_count+= 1
        return True, "File converted!"
    except Exception as e:
        return False,f'Error encountered: {e}'