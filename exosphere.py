import streamlit as st
#import requests 
#from datetime import datetime 


st.title('exosphere')


st.markdown("""
This app retrieves the space pictures of you latest birthday
""")


birthday = st.date_input('Input your birthday', min_value=datetime.date(1960-0o1-0o1), max_value="today")
st.write('Your current selected birthday is', birthday)









































































