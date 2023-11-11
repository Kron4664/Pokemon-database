#-----------------------------------------------------------------------------
# Name:        g12 Chart (python.py)
# Purpose:     To provide a graph of a pokemon based database and give some other 
#              uses such as a pokemon finder.
#
# References: 	This program uses the NumPy/SciPy style of documentation as found
#				here: https://numpydoc.readthedocs.io/en/latest/format.html with
#				some minor modifications based on Python 3 function annotations
#				(the -> notation). This program uses Pandas and Matplotlib as found here: 
#       https://pandas.pydata.org/docs/user_guide/10min.html
#       https://matplotlib.org/
#
# Author:      Krutin Jain
# Created:     4-Aug-2023
# Updated:     25-Aug-2023 (updated documentation)
#-----------------------------------------------------------------------------
import csv
import os

import pandas as pd
from matplotlib import pyplot as plt

import databasefunctions

print("Hello ( >.<)\nSearch a pokemon and Choose 'n' if you want to see the chart and stat reference.")
class Modify:
  """
  class used to form a new file using the pokemon.csv file and modify 
  it such that it develops a new column named stats and loses some 
  columns. 
  databasefunctions.modify_csv() was called to make a new csv which would be used to 
  create the chart.
  """ 
  databasefunctions.modify_csv()
  #print("\nThe cummulative Remainder is: ", cummulativeRemainder, "\n")#WIP


class Pokemon:
  """
  A class representing details of the Pokemon searched by user.

  Attributes
  ----------
  data : pandas.DataFrame
      The DataFrame containing Pokemon data.
  headers : list
      A list of column headers obtained from the DataFrame.

  Methods
  -------
  search(number)
      Searches for and prints details of a Pokemon based on the given index number.
  searcher()
      Initiates the Pokemon search process, prompting the user to input index numbers and displaying Pokemon details.
  """
  def __init__(self, data): 
      self.data = data
      self.headers = data.columns.tolist()

  def search(self, number):
      """
      Initializes a Pokemon instance with the provided DataFrame.

      Parameters
      ----------
      data : pandas.DataFrame
          The DataFrame containing Pokemon data.
      """
      number = number + 1
      if 0 <= number < len(self.data):
          row = self.data.iloc[number]
          for header, value in zip(self.headers, row):
              print(f"{header}: {value}")
      else:
          print(f"Pokemon number {number+1} is not in the local Pokemon dex")
     

  def searcher(self):
      """
      Initiates the Pokemon search process, prompting the user to input index numbers and displaying Pokemon details.
      """
      print("\nYou can search more Pokemons by pressing 'y' or 'n' to see the chart and its stats reference.\n")
      while True:
          st = input("Do you want to search Pokemons? (y for Search/n for chart and stats reference): ").lower()
          if st == 'y':
              databasefunctions.clear()
              print("\n")
              while True:
                try:
                    number = int(input("Enter the index number (national index+1, not Pokedex number) of the Pokémon you want to know about: "))
                    number=number-2
                    with open('input.csv', mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["Input", number])
                    df = pd.read_csv('input.csv', usecols=['Input'])
                except ValueError:
                    print(" ")
                    break
    
                self.search(number)
                st = input("\nDo you want to search more Pokemons? (y for Search/n for chart and stats reference): ").lower()
          elif st == 'n':
              databasefunctions.clear()
              break
      print("Search a Pokémon in the Pokemon searcher!")
      

pokemon_data = pd.read_csv('pokemon2.csv')
pokemon_instance = Pokemon(pokemon_data)
pokemon_instance.searcher()
  
  
class Stats:
  """
  Forms a stats table by plotting the values obtained in the new csv 
  file made by modify module. 

  databasefunctions.stats() was called to display a stats reference table.
  """
  databasefunctions.Stats()
  
  
class Charts:
  """
  class used to form a stats chart using the csv obtained from modify 
  module.

  databasefunctions.charts() was called to display the main part, the chart.
  """
  databasefunctions.Charts()

#WIP
class Types:
  """
  used to call a function to display data related to types of various 
  pokemon

  databasefunctions.Types() was called to display a types reference table.

  """
  databasefunctions.Types()

  
  
"""
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Make data
np.random.seed(101)
n = 300
rng = np.random.default_rng()
xs = rng.uniform(26, 32, n)
ys = rng.uniform(0, 50, n)
zs = rng.uniform(-50, -25, n)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)

ax.set(xticklabels=[],
  yticklabels=[],
  zticklabels=[])

plt.show()
"""

"""
class Stats:
  with open('pokemon.csv')
  databasefunctions.Stats()

"""