import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Read in the agent-level data from CSV
agent_data = pd.read_csv('base_case_agent_level_data.csv')

# Considering the last 1075 rows for the last timestep
agent_data_last_step = agent_data.iloc[-1075:]

# Group agents by the number of times they've been stopped
search_total_counts = agent_data_last_step['search_total'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
search_total_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Number of Stops')
plt.ylabel('Number of Agents')
plt.title('Grouping agents by frequency of Stops)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Extract data from the last run
df_last_run = agent_data_last_step

# Group by the 'searched' column and count occurrences
search_counts = df_last_run['searched'].value_counts()

# Plot
plt.figure(figsize=(8, 6))
search_counts.plot(kind='bar', color=['red', 'green'])
plt.title('Agents grouped by Searched vs Not-Searched')
plt.xlabel('Search Status')
plt.ylabel('Number of Agents')
plt.xticks(ticks=[0, 1], labels=['Searched', 'Not Searched'], rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()