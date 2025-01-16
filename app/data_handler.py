import pandas as pd

def load_and_preprocess_data(file_path, save_path=None):
    """
    Load CSV data and preprocess it for analysis.
    
    Args:
        file_path (str): Path to the input CSV file.
        save_path (str, optional): Path to save the modified DataFrame. Defaults to None.
        
    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    data = pd.read_csv(file_path)
    
    df = pd.DataFrame(data)
    
    df['Hour'] = df['Time'].astype(str).str.zfill(6).str[:2].astype(int)
    
    df['Date'] = pd.to_datetime(df['Date'], format='%y%m%d')
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    
    event_frequency = df['EventId'].value_counts()
    df['EventFrequency'] = df['EventId'].map(event_frequency)

    # Create binary anomaly label: 1 = Anomalous (WARN), 0 = Normal (INFO)
    df['Anomalous'] = df['Level'].apply(lambda x: 1 if x == 'WARN' else 0)
    
    if save_path:
        df.to_csv(save_path, index=False)
        print(f"Modified dataset saved to {save_path}")
    
    return df
