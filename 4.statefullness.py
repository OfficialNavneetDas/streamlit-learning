import streamlit as st

st.header("What is a State ?")
st.write("We define access to a Streamlit app in a browser tab as a session. For each browser tab that connects to the Streamlit server, a new session is created. Streamlit reruns your script from top to bottom every time you interact with your app")


# try making a counter
st.markdown("---")
code0, counter_button0= st.columns(2)
counter = 0

code0.code("""
counter = 0
increment = st.button("increment")
if increment:
    counter+=1
st.write(increment)
""",language="python")

increment = counter_button0.button("increment")
if increment:
    counter+=1
    st.warning("when ever the button is clicked the app re-run from start and initilized the value as zero after that it execute the code of count+=1 ot make the value 1")

counter_button0.write(counter)


# making a working counter
st.markdown("---")
code, counter_button1, session1 = st.columns(3)

code.code("""
if "counter" not in st.session_state:
    st.session_state["counter"] = 0

increment = st.button(f"working_button inc={st.session_state.counter}",key="working_button")
          
if increment:
    st.session_state.counter+=1
    st.write(st.session_state)
""",language="python")
if "count" not in st.session_state:
    st.session_state["count"] = 0

increment_count = counter_button1.button(f"working_button inc={st.session_state.count}",key="working_button")
if increment_count:
    st.session_state.count+=1
    session1.write(st.session_state)
    st.success("this code worked! the value of count is increasing")
    st.warning("but as you can see that the button value is a step back this is because it uses the previous value before the increment during the rerun of our code")
counter_button1.write(st.session_state.count)



# perfect counter
st.markdown("---")
code2, counter_button2 , session2 = st.columns(3,border=True)
code2.code("""
if "counter" not in st.session_state:
    st.session_state["counter"] = 0

def increment():
    st.session_state.counter+=1

increment = st.button(f"increment = {st.session_state.counter}",key="perfect_button",on_click=increment)
if increment:
    st.write(st.session_state)

st.write(st.session_state.counter)
""",language="python")
if "count2" not in st.session_state:
    st.session_state["count2"] = 0

def increment_count():
    st.session_state.count2+=1

increment_count2 = counter_button2.button(f"increment = {st.session_state.count2}",key="perfect_button",on_click=increment_count)
if increment_count2:
    session2.write(st.session_state)
    st.success("done! while useing a callback function like onclick first the callback function is run then the app re-runs from top to bottom")

counter_button2.write(st.session_state.count2)

# difference 
st.header("Difference between both are")