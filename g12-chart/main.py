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
# Updated:     15-Nov-2023 (updated documentation)
#-----------------------------------------------------------------------------
#3-: https://stackoverflow.com/questions/12770213/writerow-csv-returns-a-number-instead-of-writing-rows
#2-: https://stackoverflow.com/questions/31328861/replacing-header-with-top-row
import csv
import os

import pandas as pd
from matplotlib import pyplot as plt

import databasefunctions

print("Hello ( >.<)\nSearch a pokemon and Choose 'n' if you want to see the chart and stat reference.\n")
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

class PokemonBase:
  """
  A base class representing common details of a Pokemon.

  Attributes
  ----------
  Number, Name, Type1, Type2, Total, HP, Attack, Defense, Sp_Atk, Sp_De, Speed, Generation, Legendary

  Methods
  -------
  details()
      Prints the details of a Pokemon.
  """

  def __init__(self, data, Number, Name, Type1, Type2, Total, HP, Attack, Defense, Sp_Atk, Sp_De, Speed, Generation, Legendary):
      self.data = data
      self.headers = data.columns.tolist()
      self.Number = Number
      self.Name = Name
      self.Type1 = Type1
      self.Type2 = Type2
      self.Total = Total
      self.HP = HP
      self.Attack = Attack
      self.Defense = Defense
      self.Sp_Atk = Sp_Atk
      self.Sp_De = Sp_De
      self.Speed = Speed
      self.Generation = Generation
      self.Legendary = Legendary

  def details(self):
      """
      Prints the details of a Pokemon.
      """
      print("\nDetails of Pokemon:"
            f"\nNumber: {self.Number}\nName: {self.Name}\nType1: {self.Type1}\nType2: {self.Type2}\nTotal: {self.Total}\n"
            f"HP: {self.HP}\nAttack: {self.Attack}\nDefense: {self.Defense}\nSp_Atk: {self.Sp_Atk}\nSp_De: {self.Sp_De}\n"
            f"Speed: {self.Speed}\nGeneration: {self.Generation}\nLegendary: {self.Legendary}\n")


class Pikachu(PokemonBase):
  def __init__(self, data):
      super().__init__(data, Number=25, Name="Pikachu", Type1="Electric", Type2="", Total=320, HP=35, Attack=55,
                       Defense=40, Sp_Atk=50, Sp_De=50, Speed=90, Generation=1, Legendary=False)

  def pika_stats(self):
      self.details()

  def shock_attack(self):
      print("Pikachu uses Thunderbolt!\n")


class Charizard(PokemonBase):
  def __init__(self, data):
      super().__init__(data, Number=6, Name="Charizard", Type1="Fire", Type2="Flying", Total=534, HP=78, Attack=84,
                       Defense=78, Sp_Atk=109, Sp_De=85, Speed=100, Generation=1, Legendary=False)

  def char_stats(self):
      self.details()

  def fire_attack(self):
      print("Charizard uses Flamethrower!\n")

print("Have a look at the most famous pokemons!!\n ")
pokemon_data = pd.read_csv('pokemon2.csv')
pikachu_instance = Pikachu(pokemon_data)
charizard_instance = Charizard(pokemon_data)
pikachu_instance.pika_stats()
charizard_instance.char_stats()
pikachu_instance.shock_attack()
charizard_instance.fire_attack()


class Pokemon:
  """
  A class representing details of the Pokemon searched by user.

  Attributes
  ----------
  Number, Name, Type1, Type2, Total, HP, Attack, Defense, Sp_Atk, Sp_De, Speed, Generation, Legendary

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

      number = number + 1
    #2
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
      print("\nYou can search more Pokemons by pressing 'y' or 'n' to see the chart and stats reference.\n")
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
                      #3
                        writer = csv.writer(file)#to write input in input csv
                        writer.writerow([number])
                    df = pd.read_csv('input.csv', usecols=['Input'])
                except ValueError:
                    print(" ")
                    break

                self.search(number)#searches for a matching string and returns if it is found
                st = input("\nDo you want to search more Pokemons? (y for Search/n for the chart and stats reference): ").lower()
          elif st == 'n':
              databasefunctions.clear()
              break
      print("Search a Pokémon in the Pokemon searcher!")



pokemon_data = pd.read_csv('pokemon2.csv')
pokemon_instance = Pokemon(pokemon_data)
pokemon_instance.searcher()

databasefunctions.clear()



print("\n\n\n\nHere is the stats reference:")

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
