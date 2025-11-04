# Medical Data Visualizer

A Python project for visualizing and analyzing medical examination data using matplotlib, seaborn, and pandas. This project explores the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

## Project Overview

This project analyzes medical examination data to visualize relationships between various health indicators and cardiovascular disease. The dataset includes patient information such as body measurements, blood test results, and lifestyle factors.

## Features

- **Data Analysis**: Calculate BMI and categorize patients as overweight or normal weight
- **Data Normalization**: Convert cholesterol and glucose levels to binary good/bad indicators
- **Categorical Plots**: Visualize counts of health indicators for patients with and without cardiovascular disease
- **Correlation Heatmap**: Identify relationships between different health metrics

## Dataset Description

The dataset contains the following features:

| Feature | Variable Type | Variable | Value Type |
|---------|---------------|----------|------------|
| Age | Objective Feature | age | int (days) |
| Height | Objective Feature | height | int (cm) |
| Weight | Objective Feature | weight | float (kg) |
| Gender | Objective Feature | gender | categorical code |
| Systolic blood pressure | Examination Feature | ap_hi | int |
| Diastolic blood pressure | Examination Feature | ap_lo | int |
| Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | smoke | binary |
| Alcohol intake | Subjective Feature | alco | binary |
| Physical activity | Subjective Feature | active | binary |
| Presence or absence of cardiovascular disease | Target Variable | cardio | binary |

## Installation

1. Clone or download this project
2. Ensure you have Python 3.7+ installed
3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Required Packages

- pandas >= 1.3.0
- seaborn >= 0.11.0
- matplotlib >= 3.4.0
- numpy >= 1.20.0

## Usage

1. Place your `medical_examination.csv` file in the project directory
2. Run the main script:

```bash
python main.py
```

This will:
- Load and preprocess the medical data
- Generate categorical plots comparing health indicators
- Create a correlation heatmap of medical features
- Run unit tests to verify functionality

## Project Structure

```
medical-data-visualizer/
├── medical_data_visualizer.py  # Main implementation
├── main.py                     # Entry point for testing
├── test_module.py              # Unit tests
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

## Functions

### `draw_cat_plot()`
Creates a categorical plot showing counts of good and bad outcomes for:
- cholesterol
- glucose
- smoking
- alcohol intake
- physical activity
- overweight status

Separated by cardiovascular disease status (cardio=0 vs cardio=1).

### `draw_heat_map()`
Generates a correlation heatmap with:
- Data cleaned to remove invalid measurements
- Upper triangle masked for better readability
- Annotations showing correlation values

## Data Processing Steps

1. **BMI Calculation**: Weight (kg) / (Height (m))²
2. **Overweight Classification**: BMI > 25 = overweight (1), else normal (0)
3. **Normalization**:
   - Cholesterol/Glucose = 1 → 0 (good)
   - Cholesterol/Glucose > 1 → 1 (bad)
4. **Data Cleaning**:
   - Remove records where diastolic > systolic pressure
   - Remove height/weight outliers (outside 2.5-97.5 percentile)

## Testing

Run the unit tests to verify the implementation:

```bash
python main.py
```

Or run tests directly:

```bash
python -m unittest test_module.py
```

## Output

The project generates two main visualizations:

1. **Categorical Plot**: Bar charts comparing health indicator counts between patients with and without cardiovascular disease
2. **Heat Map**: Correlation matrix showing relationships between different health metrics

## License

This project is part of the freeCodeCamp Data Analysis with Python curriculum.

## Acknowledgments

- freeCodeCamp for the project specification
- Medical dataset providers