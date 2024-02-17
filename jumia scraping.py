import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
@st.cache
def load_data():
    return pd.read_csv('clean_data.csv')  # Replace 'clean_df.csv' with your actual file path

data = load_data()

# Set page title
st.title('Top 10 Products with the Best Bonus')

# Sort data by 'Bonus' column in descending order and select top 10 rows
top_10_products = data.sort_values(by='Bonus', ascending=False).head(10)

# Display the top 10 products
st.subheader('Top 10 Products')
st.write(top_10_products)

# Draw bar plot for top 10 products
plt.figure(figsize=(10, 6))
sns.barplot(x='Bonus', y='Name', data=top_10_products)
plt.title('Top 10 Products with the Best Bonus')
plt.xlabel('Bonus')
plt.ylabel('Product Name')
st.pyplot()
