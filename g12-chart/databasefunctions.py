import csv
import os

import pandas as pd
from matplotlib import pyplot as plt

#WIP 
cummulativeRemainder = 0 

"""
importing various libraries and csv 
"""


def modify_csv():
  """
  function to make a copy of the csv file and mpdify it by adding a 
  column derived from integer division of another column. Also shows 
  the total stats recieved from rounding off to the previous number.
  """
  df = pd.read_csv('pokemon.csv', usecols = ["Name", "Total"])
  df.head() #used to make column titles 
  #cummulativeRemainder = cummulativeRemainder + (df['Total']%3).sum()
  df['Stats'] = (df['Total'] // 3)
  df.to_csv('newpokemon.csv')
  df = pd.read_csv('newpokemon.csv')#, index=False) #used to store values to csv
  """
  Explicitly casts columns to desired data types after using these 
  methods.
  """
  df['Total'] = df['Total'].astype(int)
  df['Name'] = df['Name'].astype(str)
  df['Stats'] = df['Stats'].astype(int)



if __name__ == "__main__": #block
  modify_csv()



def Stats():
  """
  fucntion to make a chart us8ng the new csv file
  """
  df = pd.read_csv('pokemon.csv', usecols=['Total', 'Name', 'Stats'])
  """
  Explicitly casts columns to desired data types after using these 
  methods.
  """
  df['Total'] = df['Total'].astype(int)
  df['Name'] = df['Name'].astype(str)
  df['Stats'] = df['Stats'].astype(int)

  print("Contents in csv file:\n", df)
  plt.plot(df['Name'], df['Stats'])
  plt.xlabel('Names')
  plt.ylabel('Stats')
  plt.title('Pokemon')
  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.show



def Charts():
  """
  function to make and display a table showing stats of various 
  Pokémon.
  """
  plt.rcParams["figure.figsize"] = [7.00, 3.50]
  plt.rcParams["figure.autolayout"] = True
  df = pd.read_csv('newpokemon.csv', usecols=['Total', 'Name', 'Stats'])
  """
  Explicitly casts columns to desired data types after using these 
  methods.
  """
  df['Total'] = df['Total'].astype(int)
  df['Name'] = df['Name'].astype(str)
  df['Stats'] = df['Stats'].astype(int)
  plt.plot(df.Name, df.Stats)
  plt.show()

with open('input.csv', mode='a', newline='') as file:
  """
  used to create and append  (mode a for append) a new 
  file which has the input from the user.
  """
  writer = csv.writer(file)

  # Write a header row
  writer.writerow(["Input"])


def clear():
  os.system('cls' if os.name=='nt' else 'clear') # clears the terminal/console


