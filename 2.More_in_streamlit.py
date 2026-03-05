import streamlit as st

# useing html style property in markdown to hide the header of the streamlit app
# st.markdown(
#     """
# <style>
# header
# {
# visibility:hidden;
# }
# </style>
# """,unsafe_allow_html=True)

st.title(" Interactive Widgets")

# working with checkbox
# it return the value of checkbox (True,False)
toggle = st.checkbox("toggle me",value=True) 
if toggle == True:
    custom_delta=456
else:
    custom_delta=-456
st.metric(label="stock price",value=132, delta=custom_delta)


# we can also call a function when checkbox is clicked
def checked():
    print(f"checked with the value of {st.session_state.checker}")
st.checkbox("print status",on_change=checked,key="checker")


# working with radio button
radio_btn = st.radio("In which country do you live ?" ,options=("UK","US","INDIA"),index=None)
st.caption(f"{radio_btn} is a very powerful country")


# working with button
def fun_clicked():
    print("clicked")
btn = st.button("click me",on_click=fun_clicked)


# working with selectbox and multiselectbox
st.selectbox("what is your favourite teck brand ?",options=("google","amazon","meta","orical")) 

mul_select = st.multiselect("which code language do you use",options=("python","C","C++","java","R","javascript","react","express","nodejs","others"),default=None)
st.write(mul_select)

# uploading files
image = st.file_uploader("Please upload your file",type=["PNG","JPGE","JPG"])
if image is not None:
    st.image(image)


# select multiple images
mul_image = st.file_uploader("Please upload your file",type=["PNG","JPGE","JPG"],accept_multiple_files=True)
if mul_image is not None:
    for images in mul_image:
        st.image(images)


# working with slider
slider_value = st.slider("this is a slider",min_value=20,max_value=30,value=25)
st.write(slider_value)


# working with text
st.text_input("what is your name ?",max_chars=30,)
st.text_area("review")
st.date_input("date")
st.time_input("time")