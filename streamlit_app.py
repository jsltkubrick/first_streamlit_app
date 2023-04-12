
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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])   #list Lists out the indexes of the my fruit list, the avocado and strawb
                                                                                                 #bits are part of streamlit's multiselect indexing function
fruits_to_show = my_fruit_list.loc[fruits_selected]      #use the fruits in our fruits_selected list (i.e.avo and strawbs specifically) to pull rows from the full data set 
                                                          #(and assign that data to a variable called fruits_to_show)

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())  #writes the data to the app screen in the form of text, converted from json

# takes the json response and normalises it using JSON_NORMALIZE, which is pulled from the Pandas package we imported earlier
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# outputs it onto the app screen as a table
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')   #the streamlit version of input, here u can pre enter what u want too
streamlit.write('The user entered ', fruit_choice)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]) #sets a python variable which uses snowflake connector to 
#connect to the python script pulled by streamlit secrets
#it is the connection to the database
my_cur = my_cnx.cursor()
#Allows Python code to execute PostgreSQL command in a database session, allows you to iterate over a result set from the query
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#executes it with the above command within snowflake
my_data_row = my_cur.fetchone()
#fetchone() retrieves the next row of a query result set and returns a single sequence
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
