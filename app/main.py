# app/main.py
from data_handler import load_and_preprocess_data
from visualizations import *  # Import everything from visualizations.py

def run_project():
    # Path to your CSV file
    file_path = "HDFS_2k.log_structured.csv"
    
    # Step 1: Load and preprocess data
    df = load_and_preprocess_data(file_path)
    
    # Step 2: Visualize EventTemplate Frequency by Day of the Week
    plt.figure(figsize=(12,6))
    sns.countplot(x='DayOfWeek', hue='EventTemplate', data=df, palette='Set2')
    plt.title('EventTemplate Frequency by Day of the Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Frequency of Event Templates')
    plt.show()

    # Step 3: Visualize the Distribution of Anomaly Levels Across Days of the Week
    plt.figure(figsize=(12, 6))
    sns.countplot(x='DayOfWeek', hue='Level', data=df, palette='Set3', order=range(7))
    plt.title('Distribution of Anomaly Levels Across Days of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Count')
    plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.legend(title='Level', loc='upper right')
    plt.show()

# Run the project
if __name__ == "__main__":
    run_project()
