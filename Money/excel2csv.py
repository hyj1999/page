# pip install pandas

import pandas as pd

def main(path = ''):
    data = pd.read_excel('money.xlsx', sheet_name=None, index_col=0)
    for sheet in data.keys():
        data[sheet].to_csv(path + '%s.csv' % sheet, encoding='utf-8')
    with open(path + "sheet_name.txt", 'w', encoding='utf-8') as f:
        f.write("sheet_name = ")
        f.write("[")
        f.write(", ".join(['"' + sheet_name + '"' for sheet_name in data.keys()]))
        f.write("];")

if __name__ == '__main__':
    main()
