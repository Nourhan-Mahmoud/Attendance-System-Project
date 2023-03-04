import streamlit as st
import pandas as pd
from datetime import datetime
import glob


st.set_page_config(
    page_title="Attendance System", page_icon="📊", layout="wide"
)

st.title(":writing_hand: Manual Attendance")
st.write("###")

with st.expander("Create New Attendence Sheet"):
    name_of_attendence_sheet = st.text_input("Enter Name of Attendence Sheet")
    if st.button("Create New Attendence Sheet"):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        df = pd.DataFrame(columns=['Date', 'Time', 'Name', 'Status'])
        sheet = name_of_attendence_sheet+" "+str(date)
        df.to_csv("6. Attendence" + sheet+ ".csv", index=False)


# datetime object containing current date and time
now = datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")

path = r"6. Attendence\\Manual\\"

tab1, tab2 = st.tabs(["View Sheet", "Add Record"])
with tab1:
    d_l = glob.glob(path+"*.csv")
    for i in range(len(d_l)):
        d_l[i] = d_l[i].split("\\")[-1].split(".")[0]
    sheet = st.selectbox("Select Date", d_l)
    df = pd.read_csv(path+str(sheet)+".csv")
    st.table(df)
with tab2:
    df = pd.read_csv(path+sheet+".csv")
    name = st.text_input("Enter Student Name")
    status = st.selectbox("Status", ["Present", "Absent"])
    new_row = {'Date': date, 'Time': time, 'Name': name, 'Status': status}
    df2 = df.append(new_row, ignore_index=True)
    if st.button("Save Record"):
        df2.to_csv(path+sheet+".csv", index=False)
        st.write("Record Saved")
        st.experimental_rerun()
