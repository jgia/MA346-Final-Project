import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title( 'MA346 Final Project Giaquinto & Consiglio' )
happiness_and_economic_freedom = pd.read_csv("happiness_and_economic_freedom.csv")

st.write("The goal of this project is to determine how the different variables that make up the Index of Economic Freedom by the Heritage Foundation \
        compare with the subjective life satisfaction scores of each country found in the World Happiness Report. The vast majority of our analysis \
        is not included in this dashboard, and can be found in this report: \
        https://deepnote.com/@john-giaquinto-685f/MA346-Final-Project-Giaquinto-and-Consiglio-a8eb658e-6f64-4544-bf57-cd04444e7be6.")
st.write("This dashboard explores life satisfaction across world regisions, as well as provides scatter plots for two economic variabes that are \
        positively correlated with life satisfaction, two economic variables that are negatively correlated with life satisfaction, and one \
        economic variable that has almost no correlation with life satisfaction. The positively correlated variables are business freedom and \
        GDP per capita. The negatively correlated variables are tarrif rate and government spending. The variable with very little correlation \
        is FDI inflow. The exact correlation coefficients can be found in the report.")


st.text("Select regions to include in the Life Satisfaction by Region bar chart")

#Check boxes for selecting region
Americas = st.checkbox('Americas', value=True)
Asia_Pacific = st.checkbox('Asia-Pacific', value=True)
Europe = st.checkbox('Europe', value=True)
Middle_East_and_North_Africa = st.checkbox('Middle East and North Africa', value=True)
Sub_Saharan_Africa = st.checkbox('Sub-Saharan Africa', value=True)

#If region is selected, add it to the selected_regions list
selected_regions = []

if Americas:
     selected_regions.append('Americas')
if Asia_Pacific:
     selected_regions.append('Asia-Pacific')
if Europe:
     selected_regions.append('Europe')
if Middle_East_and_North_Africa:
     selected_regions.append('Middle East and North Africa')
if Sub_Saharan_Africa:
     selected_regions.append('Sub-Saharan Africa')

#We only want to look at rows of the dataframe where the region is in the selected_regions list
selected_regions_subset = happiness_and_economic_freedom[happiness_and_economic_freedom['Region'].isin(selected_regions)]

#We will use groupby to find the mean life satisfaction for each region
fig , ax = plt.subplots()
ax.bar(selected_regions_subset[['LifeSatisfaction','Region']].groupby('Region').mean().index.to_list(), selected_regions_subset[['LifeSatisfaction','Region']].groupby('Region').mean()["LifeSatisfaction"].to_list())
ax.tick_params('x', labelrotation=20)
ax.set_xlabel('Region')
ax.set_ylabel('Life Satisfaction  (Out of 10)')
ax.set_title('Life Satisfaction by Region')
st.pyplot(fig)

#Business freedom is a score between 0 and 100
values = st.slider( 'Select a Business Freedom Range', 0,100, (0,100))
business_freedom_subset = happiness_and_economic_freedom[happiness_and_economic_freedom["Business Freedom"]>values[0]]
business_freedom_subset = business_freedom_subset[business_freedom_subset["Business Freedom"]<values[1]]

fig , ax = plt.subplots()
ax.scatter(business_freedom_subset['Business Freedom'], business_freedom_subset['LifeSatisfaction'])
ax.set_xlabel('Business Freedom (Out of 100 Points)')
ax.set_ylabel('Life Satisfaction (Out of 10 Points)')
ax.set_title('Life Satisfaction by Business Freedom')
st.pyplot(fig)

values = st.slider( 'Select a GDP per capita range', happiness_and_economic_freedom['GDP per Capita (PPP)'].min(), happiness_and_economic_freedom['GDP per Capita (PPP)'].max(), (float(happiness_and_economic_freedom['GDP per Capita (PPP)'].min()), float(happiness_and_economic_freedom['GDP per Capita (PPP)'].max())))
#Subset where GDP is between the selected values
GDP_per_capita_subset = happiness_and_economic_freedom[happiness_and_economic_freedom['GDP per Capita (PPP)']>values[0]]
GDP_per_capita_subset = GDP_per_capita_subset[GDP_per_capita_subset['GDP per Capita (PPP)']<values[1]]

fig , ax = plt.subplots()
ax.scatter(GDP_per_capita_subset['GDP per Capita (PPP)'], GDP_per_capita_subset['LifeSatisfaction'])
ax.set_xlabel('GDP Per Capita (in USD)')
ax.set_ylabel('Life Satisfaction (Out of 10 Points)')
ax.set_title('Life Satisfaction by GDP Per Capita')
st.pyplot(fig)

st.text("GDP per capita is interesting. After GDP per capita passes ~$25,000, its correlation with happiness decreases.")

#FDI inflow has some outliers that are far away from the values for most countries. However, most countries have an FDI inflow between 1/4th of the max and 1/4th of the min value 
values = st.slider( 'Select a FDI inflow range', happiness_and_economic_freedom['FDI Inflow (Millions)'].min(), happiness_and_economic_freedom['FDI Inflow (Millions)'].max(), (float(happiness_and_economic_freedom['FDI Inflow (Millions)'].min()/4), float(happiness_and_economic_freedom['FDI Inflow (Millions)'].max()/4)))
fdi_inflow_subset = happiness_and_economic_freedom[happiness_and_economic_freedom['FDI Inflow (Millions)']>values[0]]
fdi_inflow_subset = fdi_inflow_subset[fdi_inflow_subset['FDI Inflow (Millions)']<values[1]]

fig , ax = plt.subplots()
ax.scatter(fdi_inflow_subset['FDI Inflow (Millions)'], fdi_inflow_subset['LifeSatisfaction'])
ax.set_xlabel('FDI Inflow (Millions)')
ax.set_ylabel('Life Satisfaction (Out of 10 Points)')
ax.set_title('FDI Inflow by Business Freedom')
st.pyplot(fig)

st.text("FDI inflow has very little correlation with life satisfaction, even when we zoom in on the scatter plot")

#Government spending is a score between 0 and 100
values = st.slider( 'Select a government spending range', 0, 100, (0,100))
government_spending_subset = happiness_and_economic_freedom[happiness_and_economic_freedom['Gov\'t Spending']>values[0]]
government_spending_subset = government_spending_subset[government_spending_subset['Gov\'t Spending']<values[1]]

fig , ax = plt.subplots()
ax.scatter(government_spending_subset['Gov\'t Spending'], government_spending_subset['LifeSatisfaction'])
ax.set_xlabel('Government Spending (Out of 100 Points)')
ax.set_ylabel('Life Satisfaction (Out of 10 Points)')
ax.set_title('Life Satisfaction by Government Spending')
st.pyplot(fig)

#The tarrif rate is a percent, so it is between 0 and 100
values = st.slider( 'Select a tarrif rate range', 0, 100, (0,30))
tarrif_rate_subset = happiness_and_economic_freedom[happiness_and_economic_freedom['Tariff Rate (%)']>values[0]]
tarrif_rate_subset = tarrif_rate_subset[tarrif_rate_subset['Tariff Rate (%)']<values[1]]

fig , ax = plt.subplots()
ax.scatter(tarrif_rate_subset['Tariff Rate (%)'], tarrif_rate_subset['LifeSatisfaction'])
ax.set_xlabel('Tariff Rate (%)')
ax.set_ylabel('Life Satisfaction (Out of 10 Points)')
ax.set_title('Life Satisfaction by Tariff Rate (%)')
st.pyplot(fig)

st.write("To see the correlation of every variable in the Economic Freedom Index with life satisfaction, go to the following URL:\
        https://deepnote.com/@john-giaquinto-685f/MA346-Final-Project-Giaquinto-and-Consiglio-a8eb658e-6f64-4544-bf57-cd04444e7be6")
st.write("Here is the original data:")
st.write("https://ourworldindata.org/happiness-and-life-satisfaction")
st.write("https://www.heritage.org/index/")