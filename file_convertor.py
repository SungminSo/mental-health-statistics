import pandas as pd

file = pd.read_csv('chs19_all.txt', 'r', encoding='latin', delimiter='\t', low_memory=False)
print(file.head(10))
file.to_csv('chs19_all.csv', index=False)

# with open('chs19_all.txt', 'r', encoding='CP949') as f:
#     line_num = 1
#     line = f.readline()
#     while line:
#         print('%d %s' % (line_num, line))
#         line = f.readline()
#         line_num += 1
#     print(line_num)
#     f.close()
