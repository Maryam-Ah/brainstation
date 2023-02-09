import streamlit as st
### import libraries
import pandas as pd
import streamlit as st
import joblib



st.write("hello world")

st.write('Streamlit is an open-source app framework for Machine Learning and Data Science teams. For the docs, please click [here](https://docs.streamlit.io/en/stable/api.html). \
    This is is just a very small window into its capabilities.')


### Create a title

st.title("Kickoff - Live coding an app")

# Press R in the app to refresh after changing the code and saving here

### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

# You can also use markdown syntax.
st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)



### DATA LOADING

### A. define function to load data
@st.cache # <- add decorators after tried running the load multiple times
def load_data(path, num_rows):

    df = pd.read_csv(path, nrows=num_rows)

    # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates

    df = df.rename(columns={'Start Station Latitude': 'lat', 'Start Station Longitude': 'lon'})     
    df['Start Time'] = pd.to_datetime(df['Start Time'])      # reset dtype for column
     
    return df

### B. Load first 50K rows
df = load_data("NYC_bikes_small.csv", 50000)

### C. Display the dataframe in the app
st.dataframe(df)



#######################################################################################################################################
### DATA ANALYSIS & VISUALIZATION

### B. Add filter on side bar after initial bar chart constructed

st.sidebar.subheader("Usage filters")
round_trip = st.sidebar.checkbox('Round trips only')

if round_trip:
    df = df[df['Start Station ID'] == df['End Station ID']]


### A. Add a bar chart of usage per hour

st.subheader("Daily usage per hour")

counts = df["Start Time"].dt.hour.value_counts()
st.bar_chart(counts)

### The features we have used here are very basic. Most Python libraries can be imported as in Jupyter Notebook so the possibilities are vast.
#### Visualizations can be rendered using matplotlib, seaborn, plotly etc.
#### Models can be imported using *.pkl files (or similar) so predictions, classifications etc can be done within the app using previously optimized models
#### Automating processes and handling real-time data




#######################################################################################################################################
### STATION MAP

st.subheader('Location Map - NYC bike stations')      

st.map(df) 



