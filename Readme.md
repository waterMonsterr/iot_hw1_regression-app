# Interactive Linear Regression Visualizer

This is a simple web application built with Streamlit that allows users to interactively visualize linear regression.

## Description

The application generates a set of data points based on a linear equation `y = ax + b + noise`, where `a`, `b`, and the noise variance are configurable by the user. It then fits a linear regression model to the data, plots the data points and the regression line, and identifies the top 5 outliers.

## Features

-   Interactive sliders to control the data generation parameters:
    -   Number of data points
    -   True coefficient `a`
    -   True intercept `b`
    -   Noise variance
-   Visualizes the generated data and the fitted linear regression line.
-   Identifies and highlights the top 5 outliers.
-   Displays the calculated coefficients of the linear regression model.
-   Shows a table of the top 5 outliers with their coordinates and residuals.

## Installation

1.  Clone the repository or download the source code.
2.  Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will open a new tab in your web browser with the application running.
