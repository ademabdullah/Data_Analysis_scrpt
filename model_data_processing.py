import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#data being processed now is the 2 patrol data

df = pd.read_csv('2_patrols_model_level_data.csv')

columns_to_exclude = ['count_jailed_Citizens', 'Count_Active_Citizens', 'count_agents_on_grid', 'stop_and_search_success_rate', 'stop_and_search_total' ]
correlation_matrix = df.drop(columns=columns_to_exclude).corr()
# # code for creating correlation dataframe
# # plt.matshow(correlation_matrix.corr())
# # plt.show()
#
# print(correlation_matrix.corr())
# # Display the styled correlation matrix


# # Plotting the heatmap
# plt.figure(figsize=(12, 10))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
# plt.title("Correlation Matrix")
# plt.show()
# plt.savefig("correlation matrix")
# #
# description = df[['stop_and_search_rate', 'active_criminal_rate_on_grid']].describe()
# print(description)
# description = df[['stop_and_search_rate', 'Rate_of_Violence']].describe()
# print(description)
# #
#
#
# # see ChatGPT convo for more reference for these
#
#
# # # Scatter Plot: Stop and Search Rate vs. Knife Crime Rate
# #plt.figure(figsize=(10,6))
# plt.scatter(df['stop_and_search_rate'], df['active_criminal_rate_on_grid'], color='blue')
# plt.title('Scatter Plot: Stop and Search Rate vs. Knife Crime Rate')
# plt.xlabel('Stop and Search Rate')
# plt.ylabel('Knife Crime Rate')
# plt.grid(True)
# plt.show()
# #
# # #
# #
# # Creating the correlation between columns in the DataFrame
# correlation_matrix = df.corr()
# Print the correlation between 'stop and search rate' and 'knife crime rate'
# print("Correlation between 'stop and search rate' and 'knife crime rate':", correlation_matrix.loc['stop_and_search_rate', 'active_criminal_rate_on_grid'])
# #
# #
# # Scatter Plot: Knife Crime rate vs. Stop and Search Rate
#plt.figure(figsize=(10,6))
# plt.scatter(df['active_criminal_rate_on_grid'], df['stop_and_search_rate'], color='red')
# plt.title('Scatter Plot: Knife Crime Rate vs. Stop and Search Rate')
# plt.xlabel('active criminal rate')
# plt.ylabel('Stop and Search Rate')
# plt.grid(True)
# plt.show()


#Scatter Plot: Prison Rates vs. crime rates
#plt.figure(figsize=(10,6))
# Scatter plot
# plt.figure(figsize=(10,6))
# plt.scatter(df['Rate_of_Violence'], df['percentage_in_prison'], color='blue', label='Data Points')
# plt.title('Scatter Plot: Rate of Violence vs. Percentage in Prison')
# plt.xlabel('Rate of Violence')
# plt.ylabel('Percentage in Prison')
# plt.grid(True)
#
# # Line of best fit
# m, b = np.polyfit(df['Rate_of_Violence'], df['percentage_in_prison'], 1)  # m = slope, b = intercept
# plt.plot(df['Rate_of_Violence'], m * df['Rate_of_Violence'] + b, color='red', label='Line of Best Fit')
#
# plt.legend()
# plt.show()


# #
# # List of columns for which you want the summary
columns_of_interest = ['active_criminal_rate_on_grid', 'stop_and_search_rate']
#
# # Get the basic statistics
summary = df[columns_of_interest].describe()
#
# # Compute range for each column
summary.loc['range', :] = summary.loc['max', :] - summary.loc['min', :]

print(summary)

# Save the summary to a new CSV file
summary.to_csv('summary_statistics.csv')
#
# # Create a sequence of steps based on the number of rows in the dataframe
steps = np.arange(1, len(df) + 1)
# #
# # Plotting
# plt.figure(figsize=(15, 8))

#Time series of Stop and Search and knife crime

# Plot each series
plt.plot(steps, df['active_criminal_rate_on_grid'], label='Knife Crime Rate', color='blue')
# plt.plot(steps, df['percentage_in_prison'], label='Percentage in Prison', color='green')
plt.plot(steps, df['stop_and_search_rate'], label='Stop and Search Rate', color='red')
# plt.plot(steps, df['Rate_of_Violence'], label='Rate of Violence', color='orange')

# Setting labels, title, legend, and grid
plt.xlabel('Steps')
plt.ylabel('Rate')
plt.title('Time Series of Knife Crime Rate vs Stop and Search Rate')
plt.legend()
plt.grid(True)
plt.figure(figsize=(15, 8))
plt.tight_layout()
plt.show()
plt.savefig("Knife Crime Rate vs Stop  when police patrols are 2")

# # Plot each series
# plt.plot(steps, df['active_criminal_rate_on_grid'], label='Knife Crime Rate', color='blue')
# # plt.plot(steps, df['percentage_in_prison'], label='Percentage in Prison', color='green')
# #plt.plot(steps, df['stop_and_search_rate'], label='Stop and Search Rate', color='red')
# # plt.plot(steps, df['Rate_of_Violence'], label='Rate of Violence', color='orange')


# # Setting labels, title, legend, and grid
# plt.xlabel('Steps')
# plt.ylabel('Rate')
# plt.title('Time Series of Knife Crime Rate')
# plt.legend()
# plt.grid(True)
# plt.figure(figsize=(15, 8))
# plt.tight_layout()
# plt.show()
# plt.savefig("Knife Crime Rate over time")



# # Plot each series
# plt.plot(steps, df['active_criminal_rate_on_grid'], label='Knife Crime Rate', color='blue')
# plt.plot(steps, df['stop_and_search_rate'], label='Stop and Search Rate', color='red')
# # plt.plot(steps, df['percentage_in_prison'], label='Percentage in Prison', color='green')
# # plt.plot(steps, df['Rate_of_Violence'], label='Rate of Violence', color='orange')

# # Setting labels, title, legend, and grid
# plt.xlabel('Steps')
# plt.ylabel('Rate')
# plt.title('Time Series of Knife Crime Rate vs Stop and Search Rate.')
# plt.legend()
# plt.grid(True)
#
# plt.tight_layout()
# plt.show()
# plt.savefig("Time Series of Knife Crime Rate vs Stop and Search Rate.")