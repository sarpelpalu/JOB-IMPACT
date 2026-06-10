"""
Visualization utilities for JOB-IMPACT analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Optional, Tuple, List
import pandas as pd

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10


def set_plot_style(style: str = 'seaborn-v0_8-darkgrid', palette: str = 'husl') -> None:
    """
    Set global plotting style and theme.
    
    Parameters
    ----------
    style : str
        Matplotlib style name
    palette : str
        Color palette name
    """
    try:
        sns.set_style(style)
        sns.set_palette(palette)
    except:
        print(f"Style {style} not available, using default")


def plot_distribution(df: pd.DataFrame, column: str, title: Optional[str] = None,
                     bins: int = 30, figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Create a distribution plot for a column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name to plot
    title : str, optional
        Plot title
    bins : int
        Number of bins for histogram
    figsize : tuple
        Figure size
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Histogram
    axes[0].hist(df[column].dropna(), bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0].set_xlabel(column)
    axes[0].set_ylabel('Frequency')
    axes[0].set_title(f'{title or column} - Distribution')
    
    # Box plot
    axes[1].boxplot(df[column].dropna(), vert=True)
    axes[1].set_ylabel(column)
    axes[1].set_title(f'{title or column} - Box Plot')
    
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame, figsize: Tuple[int, int] = (12, 10),
                            cmap: str = 'coolwarm', annot: bool = True) -> None:
    """
    Create a correlation heatmap for numeric columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    figsize : tuple
        Figure size
    cmap : str
        Colormap name
    annot : bool
        Whether to annotate with correlation values
    """
    plt.figure(figsize=figsize)
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Create correlation matrix
    corr_matrix = numeric_df.corr()
    
    # Create heatmap
    sns.heatmap(corr_matrix, annot=annot, fmt='.2f', cmap=cmap,
                cbar_kws={'label': 'Correlation'}, linewidths=0.5)
    
    plt.title('Correlation Matrix Heatmap', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_categorical(df: pd.DataFrame, column: str, title: Optional[str] = None,
                    figsize: Tuple[int, int] = (12, 6), top_n: int = 10) -> None:
    """
    Create a bar plot for categorical data.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name (categorical)
    title : str, optional
        Plot title
    figsize : tuple
        Figure size
    top_n : int
        Number of top categories to show
    """
    plt.figure(figsize=figsize)
    
    # Get value counts
    counts = df[column].value_counts().head(top_n)
    
    # Create bar plot
    counts.plot(kind='barh', color='steelblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Count')
    plt.ylabel(column)
    plt.title(title or f'{column} - Top {top_n}', fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_scatter(df: pd.DataFrame, x: str, y: str, hue: Optional[str] = None,
                figsize: Tuple[int, int] = (12, 8)) -> None:
    """
    Create a scatter plot.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    x : str
        Column for x-axis
    y : str
        Column for y-axis
    hue : str, optional
        Column for color coding
    figsize : tuple
        Figure size
    """
    plt.figure(figsize=figsize)
    
    if hue:
        for group in df[hue].unique():
            mask = df[hue] == group
            plt.scatter(df[mask][x], df[mask][y], label=group, alpha=0.6, s=100)
        plt.legend()
    else:
        plt.scatter(df[x], df[y], alpha=0.6, s=100, color='steelblue')
    
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{y} vs {x}', fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_multiple_distributions(df: pd.DataFrame, columns: List[str],
                               figsize: Tuple[int, int] = (15, 10)) -> None:
    """
    Create multiple distribution plots in a grid.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    columns : list
        Columns to plot
    figsize : tuple
        Figure size
    """
    n_cols = 2
    n_rows = (len(columns) + 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.flatten()
    
    for idx, col in enumerate(columns):
        if col in df.columns:
            axes[idx].hist(df[col].dropna(), bins=20, color='steelblue', edgecolor='black', alpha=0.7)
            axes[idx].set_title(col, fontweight='bold')
            axes[idx].set_xlabel('Value')
            axes[idx].set_ylabel('Frequency')
    
    # Hide unused subplots
    for idx in range(len(columns), len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("Visualization utilities loaded successfully")
