import pandas as pd 

## single load of data
df = pd.read_csv('data/raw/SBU All Studies With PI And Primary Contact Info January 2025.csv')
df.columns
len(df)

# clean columns, remove all white space replace with _, and lowercase
df.columns = df.columns.str.replace(' ', '_').str.lower()

## create a slim version where we drop any rows where study_id contains _CR* or _MOD*
df_slim = df[~df.study_id.str.contains('_CR|_MOD')]
len(df_slim)

## value counts by pi_dept
value_counts = df_slim.pi_dept.value_counts()
value_counts.to_csv('data/output/pi_dept_value_counts.csv')

## value counts by pi_full_name
value_counts = df_slim.pi_full_name.value_counts()
value_counts = value_counts.reset_index()
value_counts = value_counts.merge(df_slim[['pi_full_name', 'pi_dept']], left_on='pi_full_name', right_on='pi_full_name')
value_counts = value_counts.drop_duplicates()
value_counts.to_csv('data/output/pi_full_name_value_counts_all.csv', index=False)

## value counts by pi_full_name where submission_type is 'Initial Study' and project_status is 'Approved'
value_counts = df_slim[(df_slim.submission_type == 'Initial Study') & (df_slim.project_status == 'Approved')].pi_full_name.value_counts()
value_counts = value_counts.reset_index()
value_counts = value_counts.merge(df_slim[['pi_full_name', 'pi_dept']], left_on='pi_full_name', right_on='pi_full_name')
value_counts = value_counts.drop_duplicates()
value_counts.to_csv('data/output/pi_full_name_value_counts_approved.csv', index=False)