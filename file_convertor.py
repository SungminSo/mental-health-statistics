# import pandas as pd
#
# file = pd.read_fwf('chs19_all.txt')
# file.to_csv('chs19_all.csv')

with open('chs19_all.txt', 'r', encoding='UTF8') as f:
    line_num = 1
    line = f.readline()
    while line:
        print('%d %s' % (line_num, line))
        line = f.readline()
        line_num += 1
    print(line_num)
    f.close()
