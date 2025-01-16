from data_handler import load_and_preprocess_data
from visualizations import plot_event_template_frequency, plot_anomaly_level_distribution

def run_project():
    file_path = "HDFS_2k.log_structured.csv"
    save_path = "HDFS_2k_modified.csv"
    
    df = load_and_preprocess_data(file_path, save_path=save_path)
    '''
    not needed because we are done with visualisation
    plot_event_template_frequency(df)
    
    
    plot_anomaly_level_distribution(df)
        '''


if __name__ == "__main__":
    run_project()
