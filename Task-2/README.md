# Gym Data Analytics Project

## Overview
This is a modular data analytics project built with Python. It demonstrates the fundamental steps of the data analysis pipeline: loading data, performing statistical calculations, and generating visual insights. The project analyzes a personal gym workout dataset (gym_data.csv) to uncover trends between muscle groups trained, workout duration, calories burned, and average heart rate.

## Project Structure
To maintain clean and organized code, the logic is separated into specific modules:

* main.py: The central execution script that connects all modules and runs the analysis sequentially.
* data_handler.py: Handles the file I/O operations, specifically loading the .csv file into a Pandas DataFrame.
* analyzer.py: Contains the mathematical logic for processing the data (e.g., calculating the average calories burned).
* plotter.py: The visualization engine utilizing Matplotlib to generate a Bar Chart, Scatter Plot, and a correlation Heatmap.
* gym_data.csv: The raw dataset containing the workout logs.

## Prerequisites
To run this project, you will need Python installed on your machine along with the following external libraries:
* Pandas (for data manipulation)
* Matplotlib (for data visualization)

You can install these dependencies via your terminal using:
pip install pandas matplotlib

## How to Run
1. Ensure gym_data.csv is located in the same directory as your Python scripts.
2. Open your terminal or command prompt.
3. Navigate to the project directory (e.g., cd path/to/Task-2).
4. Execute the main script:
python main.py

## Visualizations Generated
When the script runs, it will sequentially render three distinct visualizations:
1. Bar Chart: Compares the total calories burned against the specific muscle group trained.
2. Scatter Plot: Evaluates the relationship and potential correlation between the average heart rate and calories burned.
3. Heatmap: Displays a correlation matrix for all numerical data points (Duration, Calories, Heart Rate) to identify overarching trends.

---
Author: Ujjal 