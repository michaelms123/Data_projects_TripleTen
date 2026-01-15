import pandas as pd
import plotly.express as px 
import streamlit as st

vehicles_df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')
vehicles_df['manufacturer'] = vehicles_df['model'].apply(lambda x: x.split()[0])

#Data preprocessing 
#replacing missing values using 'fillna()'
vehicles_df.fillna({'model_year': 'Unknown'}, inplace=True)
vehicles_df.fillna({'paint_color': 'Unknown'}, inplace=True)
vehicles_df.fillna({'odometer': 'Unknown'}, inplace=True)
vehicles_df['is_4wd'].fillna('Unknown', inplace=True)
#replacing the missing values in 'cylinders' column with the median cylinders 
vehicles_df['cylinders'] = vehicles_df.groupby('model').cylinders.transform(lambda x: x.fillna(x.median()))

#Converting 'model_year' column to object datatype to mititgate errors in analysis 
vehicles_df['model_year'] = vehicles_df['model_year'].astype('Int64', errors='ignore')
#Converting 'price' and 'days_listed' to string 
vehicles_df['price'] = vehicles_df['price'].astype('Int64', errors='ignore')
vehicles_df['days_listed'] = vehicles_df['days_listed'].astype('Int64', errors='ignore')

st.header('Data Viewer')
vehicles_df

#Histogram for vehicle types by manufacturer
st.header('Vehicle Types by Manufacturer')
fig = px.histogram(vehicles_df, x='manufacturer', color='type', labels={'manufacturer': 'Vehicle Manufacturer', 'count': 'Vehicle Inventory'})
st.write(fig)


#Histogram of condition vs model year
st.header('Histogram of Condition vs. Model Year')
fig_2 = px.histogram(vehicles_df, x='model_year', color='condition', labels={'model_year': 'Model Year'})
st.write(fig_2)

st.header('Compare Price Distribution Between Manufacturers')
#Get a list of car manufacturers 
manufac_list = sorted(vehicles_df['manufacturer'].unique())
#Get user's inputs from dropdown menu
manufacturer_1 = st.selectbox(label='Select Manufacturer 1', options=manufac_list, index=manufac_list.index('chevrolet'))
#Repeat for 2nd dropdown menu
manufacturer_2 = st.selectbox(label='Select Manufacturer 2', options=manufac_list, index=manufac_list.index('hyundai'))
#Filter for the df 
mask_filter = (vehicles_df['manufacturer'] == manufacturer_1) | (vehicles_df['manufacturer'] == manufacturer_2)
filtered_df = vehicles_df[mask_filter]

#Added checkbox if a user wants to normalise the histogram 
normalise = st.checkbox('Normalise Histogram', value=True)
if normalise:
    histnorm = 'percent'
else: 
    histnorm = None 

#Creating the histogram 
fig_3 = px.histogram(filtered_df, x='price', nbins=30, color='manufacturer', histnorm=histnorm, barmode='overlay')
#displaying the figure 
st.write(fig_3)

#Creating a scatterplot that Model Year vs odometer reading 
st.header('Model Year vs. Odometer Reading')
fig_4 = px.scatter(vehicles_df, x='model_year', y='odometer', color='manufacturer', opacity=0.5, labels={'model_year': 'Model Year', 'odometer': 'Odometer Reading'})
st.plotly_chart(fig_4)

#Histogram showing distribution of price by condition 
st.header('Distribution of Price Based on Vehicle Condition')
fig_5 = px.histogram(vehicles_df, x='price', color='condition')
st.plotly_chart(fig_5, use_container_width=True)

#Histogram showing the distribution of price based on model year 
st.header('Distribution of Price Based on Model Year')
fig_6 = px.histogram(vehicles_df, x='model_year', y='price', color='manufacturer', labels={'model_year': 'Model Year', 'price': 'Price'})
st.plotly_chart(fig_6)


