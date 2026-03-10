import streamlit as st

st.title("Fragments")
st.write("Streamlit provides a decorator (```st.fragment```) to turn any function into a fragment function. When you call a fragment function that contains a widget function, a user triggers a fragment rerun instead of a full rerun when they interact with that fragment's widget.")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")

@st.fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()

st.code("""
@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")

@st.fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()
""")

st.image("asstes\\fragment_diagram.png")

st.markdown("---")
st.header("Automate fragment reruns")
st.write("```st.fragment``` includes a convenient ```run_every``` parameter that causes the fragment to rerun automatically at the specified time interval")

st.code("""
if "count" not in st.session_state:
    st.session_state["count"]=0
@st.fragment(run_every="10s")
def clock():
    st.subheader(st.session_state["count"])
    st.session_state["count"]+=1
clock()
""",language="python")

if "count" not in st.session_state:
    st.session_state["count"]=0

@st.fragment(run_every="10s")
def clock():
    st.subheader(st.session_state["count"])
    st.session_state["count"]+=1

clock()