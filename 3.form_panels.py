import streamlit as st
import time
from datetime import time as dt


# making a progress bar
timer = st.time_input("set the progress bar time",value=dt(0,0,0))

if str(timer) == "00:00:00":
    st.write("please set timer")
else:
    m,ss,ms=str(timer).split(":")
    seconds = (int(m)*60)+int(ss)+(int(ms)/60)
    per = seconds/100
    bar = st.progress(0)
    progress_status = st.empty()
    for i in range(1,100):
        bar.progress(i+1)
        progress_status.write(f"{i+1}%")
        time.sleep(per)


# making a form
# METHOD 1
st.markdown("---")
st.header("FORM")
form = st.form("Form 1")
form.text_input("Name",key="input1")
form.form_submit_button("Submit",key="submit_button_1")


st.markdown("---")
# METHOD 2
with st.form("Form 2",clear_on_submit=True):
    col1,col2 = st.columns(2)
    col1.text_input("First Name",key="input2")
    col2.text_input("last Name",key="input3")

    st.text_input("email",key="email")
    st.text_input("password",key="password")
    st.text_input("conform password",key="password2")

    day, month, year = st.columns(3)
    day.text_input("day")
    month.text_input("month")
    year.text_input("year")

    submit = st.form_submit_button("Submit",key="submit_button_2")
    if submit:
        if st.session_state.input2 == "":
            st.warning("please fill above fields")
        else:
            st.success("Submitted Successfully")

st.sidebar.write("side bar")
