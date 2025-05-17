import pandas as pd


def load_data(filepath, nrows=None):
    """Load Bitcoin dataset from CSV."""
    try:
        df = pd.read_csv(filepath, nrows=nrows)
        print(f"Data loaded successfully with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def validate_data(df):
    """Validate basic structure of Bitcoin minute-level dataset."""
    required_columns = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'datetime']
    missing_cols = [col for col in required_columns if col not in df.columns]

    if missing_cols:
        raise ValueError(f"Missing columns in dataset: {missing_cols}")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values (NaN).")

    if df.duplicated().any():
        raise ValueError("Dataset contains duplicated rows.")

    print("Data validation passed successfully.")
