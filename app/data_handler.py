# app/data_handler.py
import pandas as pd

def load_and_preprocess_data(file_path):
    """Load CSV data and preprocess it for analysis."""
    data = pd.read_csv(file_path)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Preprocessing: Extract hour from the 'Time' column
    df['Hour'] = df['Time'].astype(str).str.zfill(6).str[:2].astype(int)
    
    # Convert 'Date' column to datetime and extract Day of the Week
    df['Date'] = pd.to_datetime(df['Date'], format='%y%m%d')
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    
    # Calculate Event Frequency
    event_frequency = df['EventId'].value_counts()
    df['EventFrequency'] = df['EventId'].map(event_frequency)
    
    return df
