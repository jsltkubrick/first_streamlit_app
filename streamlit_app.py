
import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError   #adds a new import command for error message handling

streamlit.title('My Parents new healthy diner') #sets the app's title - committing this change makes the title appear in the streamlit app

streamlit.header('Breakfast menu')
streamlit.text(' 🥣Omega 3 & Blueberry oatmeal')
streamlit.text(' 🥗 Kale, spinach and rocket smoothie')
streamlit.text(' 🐔 hard boiled free-range egg')
streamlit.text(' 🥑🍞avo toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')   #the streamlit version of input, here u can pre enter what u want too
  if not fruit_choice:
    streamlit.error('please select a fruit to get info!')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
 
except URLError as e:
  streamlit.error()

#streamlit.text(fruityvice_response.json())  #writes the data to the app screen in the form of text, converted from json

# takes the json response and normalises it using JSON_NORMALIZE, which is pulled from the Pandas package we imported earlier

# outputs it onto the app screen as a table




#dont run anything past here while we troubleshoot
streamlit.stop()

streamlit.header("The fruit load list contains:")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur: #Allows Python code to execute PostgreSQL command in a database session, allows you to iterate over a result set from the query
    my_cur.execute("SELECT * FROM fruit_load_list") #executes it with the above command within snowflake
    return my_cur.fetchall() #fetchone() retrieves the next row of a query result set and returns a single sequence, fetchall() retrieves everything

#adding a button to load the fruit: (so list won't show until you click the button)
if streamlit.button('Get fruit load list!'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])   #sets a python variable which uses snowflake connector to connect to the python script pulled by streamlit secrets
  my_data_rows = get_fruit_load_list()                                                                        ##it is the connection to the database
  streamlit.dataframe(my_data_row)   #can swap .dataframe for .text if you prefer

#Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?')   
#the streamlit version of input, here u can pre enter what u want too
streamlit.write('Thanks for adding', add_my_fruit)

my_cur.execute("INSERT INTO fruit_load_list VALUES ('from streamlit')")
