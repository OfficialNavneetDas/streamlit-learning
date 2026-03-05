import  streamlit as st
# open terminal and run ("streamlit run 1.Getting_started.py") to run the streamlit app


# ------------------------------------------------------------------------------------------------------------
# This is used to set the title
st.title("Hii! this is first web app")

# ------------------------------------------------------------------------------------------------------------
# This is used to set the subheading
st.subheader("This is a subheader")

# ------------------------------------------------------------------------------------------------------------
# This is use to set header
st.header("This is a header")

# ------------------------------------------------------------------------------------------------------------
# This is use to set the perahraph
st.text("This is a text and i am used in place of a paragraph tag")

# ------------------------------------------------------------------------------------------------------------
# This is use to set the markdown (https://www.markdownguide.org/cheat-sheet/)
st.markdown("This is a **markdown** _format_")
st.markdown("---")

# ------------------------------------------------------------------------------------------------------------
# This is use to set caption
st.caption("This is a caption")

# ------------------------------------------------------------------------------------------------------------
# This is use to write maths formulas in streamlit (https://katex.org/docs/supported.html)
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

# ------------------------------------------------------------------------------------------------------------
# To add json file
my_json={1:"navneet",2:"gopu",3:"others"}
st.json(my_json)

# ------------------------------------------------------------------------------------------------------------
# To display a code
my_code="""print("this is a random code")
def function():
    return 0;"""
st.code(my_code,language="python")

# ------------------------------------------------------------------------------------------------------------
# To display a any above things like (code, makdown, title)
st.write("this is a temp peragraph")

# ------------------------------------------------------------------------------------------------------------
# To make up down matrix
st.metric(label="A stock price", value="Rs 857", delta="Rs 45")
st.metric(label="B stock price", value="Rs 857", delta="-Rs 45")

# ------------------------------------------------------------------------------------------------------------
# Making table by a dataframe
import pandas as pd
data=pd.DataFrame({"ID":[1,2,3,4,5,6,7,8,9],"name":["Navneet","Yukta","Prakash","Rohit","Neha","Kunal","Vicky",None,"Vivek"]})
st.table(data)

# ------------------------------------------------------------------------------------------------------------
# Display dataframe
st.dataframe(data)


# ------------------------------------------------------------------------------------------------------------
# Import Image
st.markdown("## IMAGE")
st.markdown("---")
st.image("D:\\machine learning\\Streamlit\\asstes\\13729775.png", caption="This is a image from windBreaker",width=800)


# ------------------------------------------------------------------------------------------------------------
# Import Audio
st.markdown("## AUDIO")
st.markdown("---")
st.audio("D:\\machine learning\\Streamlit\\asstes\\Ride It [Lyrics] - Jay sean __ Hindi Version.mp3")


# ------------------------------------------------------------------------------------------------------------
# Import Video
st.markdown("## VIDEO")
st.markdown("---")
st.video("D:\\machine learning\\Streamlit\\asstes\\umbrella-anime-girl-city-night-rain-moewalls.com.mp4")