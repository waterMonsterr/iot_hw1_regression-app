import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Set up the page configuration for the Streamlit app
st.set_page_config(page_title="Interactive Linear Regression Visualizer", layout="wide")

# --- User Interface (Sidebar) ---
st.sidebar.header("Configuration")
st.sidebar.write("Adjust the parameters below to generate new data and retrain the model.")

# Sliders for user to control the data generation
n_points = st.sidebar.slider("Number of data points (n)", 100, 1000, 500)
coefficient_a = st.sidebar.slider("True Coefficient 'a'", -10.0, 10.0, 2.0, 0.1)
intercept_b = st.sidebar.slider("True Intercept 'b'", -10.0, 10.0, 5.0, 0.1)
noise_variance = st.sidebar.slider("Noise Variance (var)", 0.0, 1000.0, 100.0, 10.0)

# --- Main Page Content ---
st.title("HW1-1: Interactive Linear Regression Visualizer")

# 1. Data Generation
# Set a seed for reproducibility
np.random.seed(42) 
# Generate random x values
x = np.random.rand(n_points) * 20 - 10 # Generate x in a range [-10, 10]
# Calculate y based on the linear equation y = ax + b + noise
y_true = coefficient_a * x + intercept_b
# Generate normally distributed noise
# np.random.normal takes standard deviation (sqrt of variance)
noise = np.random.normal(0, np.sqrt(noise_variance), n_points)
y = y_true + noise

# Create a DataFrame for easier handling
df = pd.DataFrame({'x': x, 'y': y})

# Main content area split into two columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Linear Regression Visualization")
    
    # 2. Linear Regression Modeling
    # Reshape x to be a 2D array for scikit-learn
    X_train = x.reshape(-1, 1)
    
    # Create and fit the model
    model = LinearRegression()
    model.fit(X_train, y)
    
    # Get predictions to plot the regression line
    y_pred = model.predict(X_train)
    
    # 3. Outlier Identification
    # Calculate residuals (absolute difference between actual and predicted y)
    df['residuals'] = np.abs(y - y_pred)
    # Find the top 5 points with the largest residuals
    outliers = df.nlargest(5, 'residuals')

    # 4. Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Scatter plot of the generated data
    ax.scatter(df['x'], df['y'], label='Generated Data', alpha=0.7)
    
    # Sort values for a clean line plot
    df_sorted = df.sort_values(by='x')
    y_pred_sorted = model.predict(df_sorted['x'].values.reshape(-1, 1))
    
    # Plot the regression line in red
    ax.plot(df_sorted['x'], y_pred_sorted, color='red', label='Linear Regression Line', linewidth=2)

    # Highlight and label the top 5 outliers
    ax.scatter(outliers['x'], outliers['y'], color='orange', s=100, edgecolors='black', zorder=5, label='Top 5 Outliers')
    for i, row in outliers.iterrows():
        ax.annotate(f"  ({row['x']:.1f}, {row['y']:.1f})", (row['x'], row['y']), textcoords="offset points", xytext=(0,5), ha='center')

    # Chart formatting
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Generated Data and Fitted Regression Line")
    ax.legend()
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Display the plot in Streamlit
    st.pyplot(fig)

with col2:
    # 5. Displaying Results
    st.subheader("Model Results")
    st.write(f"**Model's Calculated Coefficient (a):** `{model.coef_[0]:.2f}`")
    st.write(f"**Model's Calculated Intercept (b):** `{model.intercept_:.2f}`")
    
    st.markdown("---") # Visual separator
    
    st.subheader("Top 5 Outliers")
    st.write("These are the 5 points furthest from the regression line.")
    # Display the outliers dataframe, formatted for better readability
    st.dataframe(outliers[['x', 'y', 'residuals']].style.format({
        "x": "{:.2f}",
        "y": "{:.2f}",
        "residuals": "{:.2f}"
    }))