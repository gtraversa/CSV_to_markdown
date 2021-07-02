import csv
from os import path as Path

def converter(path):
    maxlen = 12000
    try:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            chars_count = 0
            s = '|'
            sp = '/'
            path = path.replace('.csv','')+'_converted.txt'
            if Path.exists(path):
                return False, 'The file already exists!\nDelete it or rename it to procede.'
            with open(path , 'a') as conv:
                for row in csv_reader:
                    if line_count <2:
                        w = row[0]+ '\n'
                        chars_count+=len(w)
                        if chars_count > maxlen:
                            return True, 'File exceeded max length of 12000 characters!\nConverted file is cut short.'
                        conv.write(w)
                    elif line_count == 2:
                        w = s.join(row)+ '\n'+'---------------|----------'+'\n'
                        chars_count+=len(w)
                        if chars_count > maxlen:
                            return True, 'File exceeded max length of 12000 characters!\nConverted file is cut short.'
                        conv.write(w)
                    else:
                        w = s.join(row)+ s+'\n'
                        chars_count+=len(w)
                        if chars_count > maxlen:
                            return True, 'File exceeded max length of 12000 characters!\nConverted file is cut short.'
                        conv.write(w)
                    line_count+= 1
        return True, f"File converted!\nNumber of characters: {chars_count} \nSaved as: {path.split('/')[-1]}\nAt location: {sp.join(path.split('/')[0:-1])}"
    except Exception as e:
        return False,f'Error encountered: {e}'