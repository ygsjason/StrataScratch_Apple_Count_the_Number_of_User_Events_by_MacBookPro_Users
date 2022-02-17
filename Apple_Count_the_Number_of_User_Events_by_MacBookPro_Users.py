# Import your libraries
import pandas as pd

# Start writing code
df1 = playbook_events.drop_duplicates()

# Filter out devices, then groupby event_name and count n of ids
df2 = df1[df1.device == 'macbook pro']
df2.groupby('event_name')['user_id'].count().reset_index(name = 'n_count').sort_values('n_count', ascending= [False])
