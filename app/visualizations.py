import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_event_template_frequency(df):
    """
    Visualize the frequency of EventTemplates by Day of the Week.
    
    Args:
        df (pd.DataFrame): Preprocessed DataFrame.
    """
    plt.figure(figsize=(12, 6))
    sns.countplot(x='DayOfWeek', hue='EventTemplate', data=df, palette='Set2')
    plt.title('EventTemplate Frequency by Day of the Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Frequency of Event Templates')
    plt.legend(title='Event Template', loc='upper right')
    plt.show()

def plot_anomaly_level_distribution(df):
    """
    Visualize the distribution of anomaly levels across days of the week.
    
    Args:
        df (pd.DataFrame): Preprocessed DataFrame.
    """
    plt.figure(figsize=(12, 6))
    sns.countplot(x='DayOfWeek', hue='Level', data=df, palette='Set3', order=range(7))
    plt.title('Distribution of Anomaly Levels Across Days of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Count')
    plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.legend(title='Level', loc='upper right')
    plt.show()

def plot_anomalous_pie_chart(df):
    """
    Draws a pie chart for the 'Anomalous' column in the dataset.
    
    Args:
        df (pd.DataFrame): Preprocessed DataFrame.
    """
    # Count the occurrences of each class in the 'Anomalous' column
    anomalous_counts = df['Anomalous'].value_counts()
    anomalous_data = pd.DataFrame({
        'Anomalous': ['Normal (0)', 'Anomalous (1)'],
        'Count': anomalous_counts.values
    })
    
    # Plotting the pie chart with consistent aesthetics
    plt.figure(figsize=(12, 6))  # Same width as other plots
    colors = ['#4CAF50', '#F44336']  # Matching colors
    explode = [0, 0.1]  # Highlight anomalous
    
    plt.pie(
        anomalous_data['Count'],
        labels=anomalous_data['Anomalous'],
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        explode=explode
    )
    
    plt.title('Distribution of Normal and Anomalous Events', fontsize=14, weight='bold')
    plt.axis('equal')  
    plt.tight_layout()  
    plt.show()