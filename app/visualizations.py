# app/visualizations.py
import seaborn as sns
import matplotlib.pyplot as plt
from data_handler import load_and_preprocess_data

# Load data
file_path = "HDFS_2k.log_structured.csv"
df = load_and_preprocess_data(file_path)

# Plot EventTemplate Frequency by Day of the Week
plt.figure(figsize=(12,6))
sns.countplot(x='DayOfWeek', hue='EventTemplate', data=df, palette='Set2')
plt.title('EventTemplate Frequency by Day of the Week')
plt.xlabel('Day of Week')
plt.ylabel('Frequency of Event Templates')
plt.show()

# Distribution of Anomaly Levels Across Days of the Week
plt.figure(figsize=(12, 6))
sns.countplot(x='DayOfWeek', hue='Level', data=df, palette='Set3', order=range(7))
plt.title('Distribution of Anomaly Levels Across Days of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.legend(title='Level', loc='upper right')
plt.show()
