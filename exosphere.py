import streamlit as st
import requests 
from datetime import date


api_key = "mrusuysu3MxPRwSRFUi3JN3ezdTml4qbhUdVVJTU"

st.title('exosphere')
st.markdown("This app retrieves the space picture from your latest birthday")

birthday = st.date_input('Input your birthday', min_value=date(1960, 1, 1), max_value=date.today())

def get_picture(d):
    resp = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params={"date": d.isoformat(), "api_key": api_key, "thumbs": True},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()

today = date.today()

year = st.selectbox('Which year?', range(today.year, 1995, -1))

target = birthday.replace(year=year)
if target > today:
    st.warning("That birthday hasn't happened yet. Pick an earlier year.")
    st.stop()

st.write('Showing the picture from', target)

data = get_picture(target)
st.subheader(data["title"])
st.image(data["url"])
st.write(data["explanation"])






































































