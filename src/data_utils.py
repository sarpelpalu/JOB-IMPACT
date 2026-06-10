"""
Data loading and preprocessing utilities for JOB-IMPACT analysis.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Dict, Any

# Data directory path
DATA_DIR = Path(__file__).parent.parent / "data"


def load_csv(filename: str) -> pd.DataFrame:
    """
    Load CSV file from data directory.
    
    Parameters
    ----------
    filename : str
        Name of the CSV file to load
        
    Returns
    -------
    pd.DataFrame
        Loaded dataframe
        
    Examples
    --------
    >>> df = load_csv('ai_job_impact.csv')
    >>> print(df.head())
    """
    filepath = DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Loaded {filename} - Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"✗ Error loading {filename}: {str(e)}")
        raise


def load_all_datasets() -> Dict[str, pd.DataFrame]:
    """
    Load all primary datasets.
    
    Returns
    -------
    dict
        Dictionary containing all loaded dataframes
    """
    datasets = {
        'main': load_csv('ai_job_impact.csv'),
        'comprehensive_results': load_csv('comprehensive_model_results.csv'),
        'model_comparison': load_csv('model_comparison_results.csv'),
    }
    return datasets


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
        
    Returns
    -------
    pd.DataFrame
        Cleaned dataframe
    """
    df_clean = df.copy()
    
    # Remove duplicates
    df_clean = df_clean.drop_duplicates()
    
    # Handle missing values (drop rows with all NaN, fill others)
    df_clean = df_clean.dropna(how='all')
    
    print(f"Data cleaning complete. New shape: {df_clean.shape}")
    return df_clean


def get_data_info(df: pd.DataFrame) -> None:
    """
    Print comprehensive information about the dataset.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    """
    print("\n" + "="*60)
    print("DATASET INFORMATION")
    print("="*60)
    print(f"Shape: {df.shape}")
    print(f"\nColumn Data Types:")
    print(df.dtypes)
    print(f"\nMissing Values:")
    print(df.isnull().sum())
    print(f"\nBasic Statistics:")
    print(df.describe())
    print("="*60 + "\n")


if __name__ == "__main__":
    # Example usage
    df = load_csv('ai_job_impact.csv')
    get_data_info(df)
