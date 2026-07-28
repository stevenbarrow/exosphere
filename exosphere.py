import streamlit as st
#import requests 
#from datetime import datetime 


st.title('exosphere')


st.markdown("""
This app retrieves the space pictures of you latest birthday
""")


birthday = st.date_input('Input your birthday', datetime(1990, 1, 1))
st.write('Your current selected birthday is', birthday)









































































