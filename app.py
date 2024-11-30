import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and data
pipe = pickle.load(open(r'D:\Data Science Pojects\Laptop Price Prediction\Model\model.pkl', 'rb'))
df = pickle.load(open(r'D:\Data Science Pojects\Laptop Price Prediction\Model\df.pkl', 'rb'))

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f4f9;
            font-family: 'Helvetica', sans-serif;
        }
        .main-container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stTitle {
            font-size: 2.5rem;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #3498db;
            color: white;
            font-size: 1.3rem;
            border-radius: 10px;
            padding: 0.8em;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2980b9;
            transform: scale(1.05);
        }
        .price-title {
            font-size: 2rem;
            color: #16a085;
            text-align: center;
            font-weight: bold;
            margin-top: 30px;
        }
        .stSelectbox, .stSlider, .stNumberInput {
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# App title
st.title("Laptop Price Predictor")

# Layout for inputs
company = st.selectbox('Select Brand', df['Company'].unique(), key='brand_select')
type = st.selectbox('Select Type of Laptop', df['TypeName'].unique(), key='type_select')
ram = st.selectbox('Select RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64], key='ram_select')
weight = st.number_input('Enter Weight of Laptop (in Kg)', min_value=0.1, max_value=10.0, step=0.1, key='weight_input')
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'], key='touchscreen_select')
ips = st.selectbox('IPS Display', ['No', 'Yes'], key='ips_select')
screen_size = st.slider('Select Screen Size (in inches)', 10.0, 18.0, 13.0, key='screen_size_slider')
resolution = st.selectbox('Select Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'], key='resolution_select')
cpu = st.selectbox('Select CPU Brand', df['Cpu Brand'].unique(), key='cpu_select')
hdd = st.selectbox('Select HDD (in GB)', [0, 128, 256, 512, 1024, 2048], key='hdd_select')
ssd = st.selectbox('Select SSD (in GB)', [0, 8, 128, 256, 512, 1024], key='ssd_select')
gpu = st.selectbox('Select GPU Brand', df['Gpu Brand'].unique(), key='gpu_select')
os = st.selectbox('Select Operating System', df['os'].unique(), key='os_select')

# Predict Button
if st.button('Predict Price', key='predict_button'):
    # Prepare the input data
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create the input query as a DataFrame with column names
    query_dict = {
        'Company': [company],
        'TypeName': [type],
        'Ram': [ram],
        'Weight': [weight],
        'os': [os],
        'TouchScreen': [touchscreen],
        'Ips': [ips],
        'ppi': [ppi],
        'Cpu Brand': [cpu],
        'Gpu Brand': [gpu],
        'SSD': [ssd],
        'HDD': [hdd]
    }
    
    query_df = pd.DataFrame(query_dict)
    
    # Get the column names from the original dataframe (the training set)
    query_df = query_df[df.columns.difference(['Price'])]  # Ensuring to match feature names
    
    # Predict the price using the model
    predicted_price = int(np.exp(pipe.predict(query_df)[0]))
    
    # Convert to Pakistani Rupees (1 INR ≈ 3.5 PKR)
    # predicted_price_pkr = predicted_price * 3.5
    
    st.markdown(f'<p class="price-title">The predicted price of this configuration is RS.{predicted_price} PKR</p>', unsafe_allow_html=True)

# End the container
st.markdown('</div>', unsafe_allow_html=True)
