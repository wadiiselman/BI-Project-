import pandas as pd


df1 = pd.read_json('MOCK_DATA-3.json')
df2 = pd.read_json('MOCK_DATA-4-1.json')
df3 = pd.read_json('MOCK_DATA-5.json')
df4 = pd.read_json('freshman-2020.json').rename(columns={'branch_taken': 'specialization'})
df5 = pd.read_json('freshman-2021.json').rename(columns={'branch_taken': 'specialization'})
df6 = pd.read_json('freshman-2022.json').rename(columns={'branch_taken': 'specialization'})
df7 = pd.read_json('sophomore-2020.json').rename(columns={'branch_taken': 'specialization'})
df8 = pd.read_json('sophomore-2021.json').rename(columns={'branch_taken': 'specialization'})
df9 = pd.read_json('sophomore-2022.json').rename(columns={'branch_taken': 'specialization'})

df1['current_level'] = 'Major'
df2['current_level'] = 'Major'
df3['current_level'] = 'Major'

df1 = df1[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df2 = df2[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df3 = df3[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df4 = df4[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df5 = df5[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df6 = df6[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df7 = df7[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df8 = df8[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]
df9 = df9[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'date_added', 'study_hours', 'GPA']]


merged_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=0)

merged_df = merged_df.dropna()

merged_df['Day'] = merged_df['date_added'].apply(lambda x: x.split('/')[0])
merged_df['Month'] = merged_df['date_added'].apply(lambda x: x.split('/')[1])
merged_df['Year'] = merged_df['date_added'].apply(lambda x: x.split('/')[2])

merged_df = merged_df.drop(columns=['date_added'])

merged_df = merged_df[['id', 'first_name', 'last_name', 'gender', 'age', 'specialization','current_level', 'Day', 'Month', 'Year', 'study_hours', 'GPA']]

merged_df.to_csv('ALL DATA.csv')