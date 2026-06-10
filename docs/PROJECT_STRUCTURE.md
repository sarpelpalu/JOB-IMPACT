# Project Structure Documentation

## Overview

The JOB-IMPACT repository is organized to support professional data analysis and machine learning workflows.

## Directory Structure

```
JOB-IMPACT/
│
├── README.md                              # Main project documentation
├── LICENSE                                # MIT License
├── CONTRIBUTING.md                        # Contribution guidelines
├── requirements.txt                       # Python dependencies
├── .gitignore                            # Git ignore rules
│
├── notebooks/
│   └── AI Impact on job.ipynb            # Main analysis notebook
│
├── data/
│   ├── ai_job_impact.csv                 # Primary dataset (~197 KB)
│   ├── comprehensive_model_results.csv   # Model performance metrics
│   └── model_comparison_results.csv      # Model comparison summary
│
├── src/                                   # Source code utilities
│   ├── __init__.py                       # Package initialization
│   ├── config.py                         # Configuration constants
│   ├── logger.py                         # Logging configuration
│   ├── data_utils.py                     # Data loading and preprocessing
│   ├── viz_utils.py                      # Visualization utilities
│   └── ml_utils.py                       # Machine learning utilities
│
├── outputs/                               # Generated outputs (created at runtime)
│   ├── figures/                          # Generated visualizations
│   ├── results/                          # Analysis results
│   └── models/                           # Trained models
│
├── logs/                                  # Application logs (created at runtime)
│   └── job_impact.log                    # Main log file
│
├── .github/
│   └── workflows/
│       └── notebook-validation.yml       # GitHub Actions CI/CD workflow
│
└── docs/                                  # Additional documentation
    └── config.md                         # Configuration guidelines
```

## Key Components

### 📓 Notebooks (`notebooks/`)
- **AI Impact on job.ipynb**: Main analysis notebook containing:
  - Data exploration and visualization
  - Statistical analysis
  - Machine learning models
  - Results and conclusions

### 📊 Data (`data/`)
- **ai_job_impact.csv**: Main dataset with job and AI impact metrics
- **comprehensive_model_results.csv**: Detailed model evaluation metrics
- **model_comparison_results.csv**: Summary comparison of different models

### 🛠️ Source Code (`src/`)
- **config.py**: Project-wide configuration and constants
- **logger.py**: Centralized logging setup
- **data_utils.py**: Dataset loading, cleaning, and preprocessing
- **viz_utils.py**: Advanced visualization functions
- **ml_utils.py**: Machine learning model training and evaluation
- **__init__.py**: Package initialization and exports

### 📈 Outputs (`outputs/`)
Generated during analysis:
- `figures/`: Charts, graphs, and visualizations
- `results/`: Analysis results and summaries
- `models/`: Trained model files

### 📝 Documentation
- **README.md**: Project overview and quick start guide
- **CONTRIBUTING.md**: Contribution guidelines
- **LICENSE**: MIT License
- **docs/config.md**: Configuration documentation

## Usage Examples

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook

# Open and run notebooks/AI Impact on job.ipynb
```

### Using Utilities

```python
# Import utilities
from src import load_csv, plot_distribution, ModelEvaluator

# Load data
df = load_csv('ai_job_impact.csv')

# Visualize
plot_distribution(df, 'column_name')

# Train models
evaluator = ModelEvaluator()
# ... train and evaluate models
```

## Best Practices

1. **Data Processing**: Use `src/data_utils.py` functions
2. **Visualization**: Use `src/viz_utils.py` for consistent styling
3. **ML Models**: Use `src/ml_utils.py` for training and evaluation
4. **Configuration**: Use `src/config.py` for constants
5. **Logging**: Use `src/logger.py` for logging messages

## Development Workflow

1. Create feature branch from `main`
2. Make changes to notebooks or utilities
3. Test locally before committing
4. Submit pull request with clear description
5. Address review comments
6. Merge to `main` when approved

## File Naming Conventions

- **Python files**: `snake_case.py`
- **Notebooks**: `descriptive_name.ipynb`
- **Data files**: `lowercase_with_underscores.csv`
- **Branches**: `feature/feature-name` or `bugfix/issue-name`

## Configuration Management

Global configuration is centralized in `src/config.py`:
- Model parameters (random state, test size, etc.)
- Visualization settings (figure size, style, palette)
- Data processing parameters
- Paths and directories

Override defaults by:
1. Modifying `src/config.py`
2. Setting environment variables
3. Passing parameters to functions

## Contribution Workflow

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Setting up development environment
- Code standards and style
- Testing procedures
- Pull request process
- Code review expectations

---

Last Updated: June 10, 2026
