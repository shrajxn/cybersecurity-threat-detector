import seaborn as sns
import matplotlib.pyplot as plt

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
