import streamlit as st
import pandas


st.set_page_config(layout="wide")


st.header("The Best Company")
st.write("""
Welcome to The Best Company, where innovation meets excellence. We pride ourselves on our dedication to delivering top-notch solutions that exceed expectations. Our team of experts works tirelessly to ensure every project we undertake is a resounding success. Explore our website to learn more about our services and how we can help you achieve your goals.
""")
st.subheader("Our Team")


col1, col2, col3 = st.columns(3)


df = pandas.read_csv("data.csv")


with col1:
    
    for index, row in df[:4].iterrows():
        
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        
        st.write(row["role"])
        
        st.image("images/" + row["image"])


with col2:
   
    for index, row in df[4:8].iterrows():
        
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
      
        st.write(row["role"])
       
        st.image("images/" + row["image"])


with col3:
    
    for index, row in df[8:].iterrows():
        
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
       
        st.write(row["role"])
      
        st.image("images/" + row["image"])
