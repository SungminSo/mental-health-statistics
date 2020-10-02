
# with open('chs19_all.txt', 'r', encoding='CP949') as f:
#     line_num = 1
#     line = f.readline()
#     while line:
#         print('%d %s' % (line_num, line))
#         line = f.readline()
#         line_num += 1
#     print(line_num)
#     f.close()

import pandas as pd

# file = pd.read_csv('chs19_all.txt', 'r', encoding='latin', delimiter='\t', low_memory=False)
# print(file.head(10))
# file.to_csv('chs19_all.csv', index=False)

# data = pd.read_csv('chs19_all.csv', 'r', encoding='latin', delimiter=',', low_memory=False)
# print(data.head())
# print(data.columns)
# print(data.shape)
# data_sample = data.loc[:, ['age', 'sex', 'signgu_code', 'fma_19z1', 'mea_14z1', 'mea_10z1', 'sma_01z1', 'sma_03z2', 'dra_01z1', 'mta_01z1', 'mta_02z1', 'mtb_01z1', 'qoc_07z1', 'qoc_01z1', 'hma_01z2', 'enb_02z1', 'enb_03z1', 'soa_01z1']]
# print(data_sample.head(10))
# data_sample.to_csv('chs19_all_sample.csv', index=False)

# data = pd.read_csv('chs19_all_sample.csv', 'r', encoding='latin', delimiter=',', low_memory=False)
# print(data.head())
#
# is_seoul = data['signgu_code'] <= 20000
# seoul_sample = data[is_seoul]
# seoul_sample.to_csv('chs19_seoul_sample.csv', index=False)

file = pd.read_csv('구별 공원면적 비율.txt', 'r', encoding='utf-8', delimiter='\t')
print(file.head())


