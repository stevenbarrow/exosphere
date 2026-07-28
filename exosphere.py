import streamlit as st
#import requests 
#from datetime import datetime 


st.title('exosphere')


st.markdown("""
This app retrieves the space pictures of you latest birthday
""")


birthday = st.date_input('Input your birthday', min_value=datetime.date(1900, 1, 1), max_value=datetime.today())
st.write('Your current selected birthday is', birthday)









































































