import dict
import pandas as pd

df = pd.DataFrame.from_dict(dict.students)

print(df[df['age']>20])


df.to_csv('students.csv', index=False)