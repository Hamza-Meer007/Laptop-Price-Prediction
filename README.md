
<h1>Laptop Price Prediction Model</h1>

<h2>Overview</h2>

This project aims to predict laptop prices based on various features such as CPU, Company, RAM, Screen Resolution, Memory, Weight, and OS. The model uses a combination of numerical and categorical data to predict the price of a laptop.

<h2>Technologies Used</h2>

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

<h2>Data</h2>

The dataset used for this project contains 1303 rows and 12 columns. The features used are:

- CPU
- Brand
- RAM
- Screen Resolution
- Memory
- Weight
- OS
- Gpu
- Price
- Type Name

<h2>Methodology</h2>

1. *Data Loading and Understanding*: Loaded the dataset and explored the data to understand the distribution of each feature.
2. *Data Preprocessing*: Preprocessed the data by handling missing values, encoding categorical variables, and scaling numerical features.
3. *Feature Engineering*: Created new features such as ppi (pixels per inch), SSD, HDD to improve the model's performance.
4. *Exploratory Data Analysis (EDA)*: Performed EDA to visualize the relationships between features and the target variable (price).
5. *Model Training*: Trained multiple models using different approaches (e.g., linear regression, decision trees, random forest, xgb) and evaluated their performance using metrics such as mean squared error (MSE) and R-squared.
6. *Model Selection*: Selected the best-performing model based on the evaluation metrics and saved it in a pickle file.

<h2>Model Performance</h2>

The best-performing model achieved an MSE of 0.16134395316549877 and an R-squared value of 0.8835012269174494.

<h2>Deployment</h2>

The trained model is saved in a pickle file and can be loaded and used for prediction.

<h2>Future Work</h2>

- Collect more data to improve the model's performance
- Experiment with other machine learning algorithms
- Deploy the model as a web application

<h2>Contact</h2>

If you have any questions or suggestions, please feel free to contact me at hamzameer4152@gmail.com.
