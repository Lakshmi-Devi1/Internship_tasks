import streamlit as st
import pandas as pd

# Step 1: Read the input data from file
input_file = r'C:\Users\lakshmi devi\Desktop\gowtham\4K Video\rawdata.xlsx'  # Adjust the file path as per your actual file location
df = pd.read_excel(input_file)

# Step 2: Convert 'time' column to datetime format (try inferring format)
df['time'] = pd.to_datetime(df['time'], errors='coerce')

# Step 3: Group by 'date' and calculate metrics
datewise_summary = df.groupby('date').agg({
    'activity': lambda x: (x == 'picked').sum(),
    'position': lambda x: (x.str.lower() == 'inside').sum(),
    'time': lambda x: x.max() - x.min()
}).rename(columns={
    'activity': 'pick_activities',
    'position': 'place_activities',
    'time': 'inside_duration'
}).reset_index()

datewise_summary['outside_duration'] = ''  # Initialize outside_duration column as empty

# Step 4: Format the output
output_format = datewise_summary[['date', 'pick_activities', 'place_activities', 'inside_duration', 'outside_duration']]

# Step 5: Display on Streamlit page
st.title('Datewise Activity Summary')
st.dataframe(output_format)  # Display the formatted output as a DataFrame in Streamlit

# Optionally, you can also save the output as a CSV file from Streamlit
# st.download_button('Download CSV', output_format.to_csv(), 'activity_summary.csv', 'text/csv')

