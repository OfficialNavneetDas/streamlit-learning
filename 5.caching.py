import streamlit as st
import pandas as pd
import time
import pickle

st.title("Caching")
st.markdown("---")
st.header("why Caching?")
st.markdown("""
Streamlit runs your script from top to bottom at every user interaction or code change which comes with two major challenges
1. Long-running functions run again and again, which slows down your app.  
2. Objects get recreated again and again, which makes it hard to persist them across reruns or sessions            
""")
st.markdown("---")

st.header("Type of Caching")
st.write("Streamlit uses pre-build decorater function to impliment caching")
st.markdown("""
1. ```@st.cache_data:``` it cache computations that return data: loading a DataFrame from CSV, transforming a NumPy array, querying an API, or any other function that returns a serializable data object (str, int, float, DataFrame, array, list, …)
2. ```@st.cache_resource``` it cache global resources like ML models or database connections – unserializable objects that you don't want to load multiple times.
""")
st.image("asstes\\caching-high-level-diagram.png")
st.markdown("---")

# -------------------------------------------------------------------------
st.header("Example for @st.cache_data")
cach_data_col_1, cach_data_col_2 = st.columns(2)
cach_data_col_1.write("without caching!")
cach_data_col_1.code("""
def load_data():
    df = pd.read_csv("asstes\\airlines_flights_data.csv")
    return df
""",language="python")

old_time=time.time()
def load_data(URL):
    df = pd.read_csv(URL)
    return df
URL="asstes\\airlines_flights_data.csv"
cach_data_col_1.dataframe(load_data(URL))
cach_data_col_1.header(f"Time Taken: {time.time()-old_time} sec")
cach_data_col_1.warning("the dataframe is loaded again and again")



cach_data_col_2.write("with caching!")
cach_data_col_2.code("""
@st.cache_data
def load_data():
    df = pd.read_csv("asstes\\airlines_flights_data.csv")
    return df
""",language="python")

old_time=time.time()
@st.cache_data(ttl=3600)
def load_data(URL):
    df = pd.read_csv(URL)
    return df
URL="asstes\\airlines_flights_data.csv"
cach_data_col_2.dataframe(load_data(URL))
cach_data_col_2.header(f"Time Taken: {time.time()-old_time} sec")
cach_data_col_2.success("one the dataframe is loaded it is stored in cache")

st.markdown("""
* On the first run, Streamlit recognizes that it has never called the ```load_data``` function with the specified parameter value (the URL of the CSV file) So it runs the function and downloads the data.
* Now our caching mechanism becomes active: the returned DataFrame is serialized (converted to bytes) via pickle and stored in the cache (together with the value of the ```url``` parameter).
* On the next run, Streamlit checks the cache for an entry of ```load_data``` with the specific ```url```. There is one! So it retrieves the cached object, deserializes it to a DataFrame, and returns it instead of re-running the function and downloading the data again.
""")
st.warning("```st.cache_data``` implicitly uses the ```pickle``` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieva")

# -------------------------------------------------------------------------
st.markdown("---")
st.header("Example for @st.cache_resource")
cach_resource_col_1, cach_resource_col_2 = st.columns(2)
cach_resource_col_1.write("without caching!")
cach_resource_col_1.code("""
old_time=time.time()
def load_model(path):
    with open(path, "rb") as model:
        loaded_model=pickle.load(model)
    return loaded_model
model = load_model("asstes\\trained_model_6.0.pkl")
cach_resource_col_1.header(f"Time Taken: {time.time()-old_time} sec")
""",language="python")


cach_resource_col_2.write("without caching!")
cach_resource_col_2.code("""
old_time=time.time()
@st.cache_resource
def load_model(path):
    with open(path, "rb") as model:
        loaded_model=pickle.load(model)
    return loaded_model
model = load_model("asstes\\trained_model_6.0.pkl")
cach_resource_col_1.header(f"Time Taken: {time.time()-old_time} sec")
""",language="python")

st.markdown("""
* ```st.cache_resource``` does not create a copy of the cached return value but instead stores the object itself in the cache.
* Not creating a copy means there's just one global instance of the cached return object, which saves memory, e.g. when using a large ML model.
* Return values of functions do not need to be serializable. This behavior is great for types not serializable by nature, e.g., database connections, file handles, or threads. Caching these objects with ```st.cache_data``` is not possible.
""")

st.markdown("---")
st.header("Usecase Table")
st.markdown("""
|Use case	|Typical return types	|Caching decorator|
|-----------|-----------------------|----------------|
|Reading a CSV file with pd.read_csv|	pandas.DataFrame	|st.cache_data|
|Reading a text file|	str, list of str	|st.cache_data|
|Transforming pandas dataframes	|pandas.DataFrame, pandas.Series	|st.cache_data|
|Computing with numpy arrays	|numpy.ndarray	|st.cache_data|
|Simple computations with basic types	|str, int, float, …	|st.cache_data|
|Querying a database	|pandas.DataFrame	|st.cache_data|
|Querying an API	|pandas.DataFrame, str, dict	|st.cache_data|
|Running an ML model (inference)	|pandas.DataFrame, str, int, dict, list	|st.cache_data|
|Creating or processing images	|PIL.Image.Image, numpy.ndarray	|st.cache_data|
|Creating charts	|matplotlib.figure.Figure, plotly.graph_objects.Figure, altair.Chart	|st.cache_data (but some libraries require st.cache_resource, since the chart object is not serializable – make sure not to mutate the chart aft|er creation!)|
|Lazy computations	|polars.LazyFrame	|st.cache_resource (but may be better to use st.cache_data on the collected results)|
|Loading ML models	|transformers.Pipeline, torch.nn.Module, tensorflow.keras.Model	|st.cache_resource|
|Initializing database connections	|pyodbc.Connection, sqlalchemy.engine.base.Engine, psycopg2.connection, mysql.connector.MySQLConnection, sqlite3.Connection	|st.cache_resource|
|Opening persistent file handles	|_io.TextIOWrapper	|st.cache_resource|
|Opening persistent threads	|threading.thread	|st.cache_resource|
""")

st.markdown("---")
st.header("Advanced usage")
advance_use_col1, advance_use_col2 = st.columns(2)
advance_use_col1.subheader("ttl (time-to-live) parameter")
advance_use_col1.write("```ttl``` sets a time to live on a cached function. If that time is up and you call the function again, the app will discard any old,")
advance_use_col1.code("""
@st.cache_data(ttl=3600)  # 👈 Cache data for 1 hour (=3600 seconds)
# @st.cache_data(ttl=datetime.timedelta(hours=1))  # 👈 Cache data for 1 hour (=3600 seconds)
def get_api_data():
    data = api.get(...)
    return data""",language="python")


advance_use_col2.subheader("The max_entries parameter")
advance_use_col2.write("max_entries sets the maximum number of entries in the cache")
advance_use_col2.code("""
@st.cache_data(max_entries=1000)  # 👈 Maximum 1000 entries in the cache
def get_large_array(seed):
    np.random.seed(seed)
    arr = np.random.rand(100000)
    return arr""",language="python")
st.warning("These two solve the problum of The app running out of memory because the cache is too large problum.")

st.markdown("---")
st.header("The hash_funcs parameter")
st.write("Streamlit does not know how to hash custom classes. If you pass a custom class to a cached function, Streamlit will raise a ```UnhashableParamError```")
st.success("SOLUTION")
st.code("""
class MyCustomClass:
    def __init__(self, initial_score:int):
        self.my_score = initial_score

def hash_func(obj: MyCustomClass) -> int:
    return obj.my_score

@st.cache_data(hash_funcs={MyCustomClass: hash_func})
def multiple_score(obj:MyCustomClass, multiplier:int)->int:
    return obj.my_score*multiplier

st.subheader(multiple_score(MyCustomClass(15),2))
""")