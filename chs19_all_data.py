import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('chs19_seoul_sample.csv', 'r', encoding='latin', delimiter=',', low_memory=False)
# print(data.describe())

# 거동이 불편한 사람 제외
is_qoc_01z1 = data['qoc_01z1'] == 1

# 흡연자 제외
is_sma_01z1 = data['sma_01z1'] == 3

tmp_data = data[is_qoc_01z1 & is_sma_01z1]

park_rate_data = pd.read_csv('구별 공원면적 비율.txt', 'r', encoding='utf-8', delimiter='\t')

merged_data = pd.merge(tmp_data, park_rate_data, how='inner', left_on='signgu_code', right_on='구분')
# print(merged_data.loc[:, ['signgu_code', 'mta_01z1', 'mta_02z1', 'mtb_01z1', '구분', '공원율(%)']].head())

print(merged_data.head())
# print(merged_data.mean())

print(merged_data.groupby('signgu_code').mean())

# 구 전체면적 대비 공원면적
print('주관적 스트레스 기준:', merged_data['mta_01z1'].corr(merged_data['공원율(%)']))
print('스트레스 인한 정신상담 여부:', merged_data['mta_02z1'].corr(merged_data['공원율(%)']))
print('우울감 경험 여부:', merged_data['mtb_01z1'].corr(merged_data['공원율(%)']))
print('행복감 지수:', merged_data['qoc_07z1'].corr(merged_data['공원율(%)']))
#
# print(merged_data[''])

