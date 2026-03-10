import streamlit as st

page_1 = st.Page("1.Getting_started.py",title="Getting started",icon=":material/home:")
page_2 = st.Page("2.More_in_streamlit.py",title="More in streamlit",icon=":material/home_max_dots:")
page_3 = st.Page("3.form_panels.py", title="form panels", icon=":material/assignment:")
page_4 = st.Page("4.statefullness.py", title="statefullness", icon=":material/readiness_score:")
page_5 = st.Page("5.caching.py", title="caching", icon=":material/folder_data:")
page_6 = st.Page("6.fragments.py", title="fragments", icon=":material/widget_medium:")
pg = st.navigation({"basics":[page_1,page_2,page_3],
                    "advance":[page_4, page_5, page_6]})
pg.run()