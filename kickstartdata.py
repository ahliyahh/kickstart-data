import pandas as pd
file_path=r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\kickstarter_projects.csv"



df = pd.read_csv(file_path)

print(df.head())  


df = df.drop_duplicates()

df['Country'] = df['Country'].fillna('Unknown')
df['Pledged'] = df['Pledged'].fillna(0)

df['Deadline'] = pd.to_datetime(df['Deadline'], errors='coerce')

df = df.dropna(subset=['Name', 'Goal'])

print(df)