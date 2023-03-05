# pip install pandas

import pandas as pd
import base64
import os

def main(path = ''):
    data = pd.read_excel('money.xlsx', sheet_name=None, index_col=0)
    for sheet in data.keys():
        data[sheet].to_csv(path + '%s.csv' % sheet, encoding='utf-8')
    with open(path + "sheet_name.txt", 'w', encoding='utf-8') as f:
        f.write("sheet_name = ")
        f.write("[")
        f.write(", ".join(['"' + sheet_name + '"' for sheet_name in data.keys()]))
        f.write("];")
    os.remove('money.xlsx')


def base64_encode_string(s):
    """
    将字符串进行Base64编码
    """
    s_bytes = s.encode('UTF-8')  # 将字符串转换为字节串
    base64_bytes = base64.b64encode(s_bytes)  # 进行Base64编码
    base64_string = base64_bytes.decode('UTF-8')  # 将字节串转换为字符串
    return base64_string.strip()  # 去除换行符并返回编码后的字符串


def main_base64(path = ''):
    data = pd.read_excel('money.xlsx', sheet_name=None, index_col=0)
    for sheet in data.keys():
        data[sheet].to_csv(path + '%s.csv' % sheet, encoding='utf-8')
        with open(path + '%s.csv' % sheet, encoding='utf-8') as file:
            text = file.read()
            text_base64 = base64_encode_string(text)
            file.close()
        with open(path + '%s.csv' % sheet, 'w', encoding='utf-8') as file:
            file.write(text_base64)
            file.close()
    with open(path + "sheet_name.txt", 'w', encoding='utf-8') as f:
        f.write("sheet_name = ")
        f.write("[")
        f.write(", ".join(['"' + sheet_name + '"' for sheet_name in data.keys()]))
        f.write("];")
    os.remove('money.xlsx')

if __name__ == '__main__':
    main()
