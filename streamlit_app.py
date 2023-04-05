
import streamlit

streamlit.title('My Parents new healthy diner') #sets the app's title - committing this change makes the title appear in the streamlit app

streamlit.header('Breakfast menu')
streamlit.text(' 🥣Omega 3 & Blueberry oatmeal')
streamlit.text(' 🥗 Kale, spinach and rocket smoothie')
streamlit.text(' 🐔 hard boiled free-range egg')
streamlit.text(' 🥑🍞avo toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")  #pandas reads the csv from the link and pulls it into DF
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)   #streamlit's version of Display

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberry'])   #list Lists out the indexes of the my fruit list, the avocado and strawb
                                                                                                 #bits are part of streamlit's multiselect indexing function

# Display the table on the page.
