import pandas as pd 
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from matplotlib import colors

def place_tiles(area , tiles):
    
    placement = np.empty(shape=(area[1],area[0]), dtype = "str")

    for c in range(area[1]):

        for r in range(area[0]):
            
            if c == 0 and r == 0:
              
              #Decide which tile to place
              rand = rnd.randint(0,len(tiles.index) - 1)

              #Loop to place that tile label in neighbouring squares if it's larger than 1
              for l in range(tiles["Tile_Length"][rand]):
                
                for w in range(tiles["Tile_Width"][rand]):
                
                  placement[c + l][r + w] = tiles["Tile_Label"][rand]
  
            
            else:
              
              #Skip if position is already filled
              if placement[c][r] != '': continue

              #Filter to list of tiles to valid tiles that can be placed
              valid_tiles = tiles[(tiles["Tile_Width"] <= placement.shape[1] - r) & (tiles["Tile_Length"] <= placement.shape[0] - c)]

              #Find out how many empty spaces we have to use
              space = 0
              for item in placement[c][r:(area[0] + 1)]:
                if item == '': space += 1
                elif item != '': break
              
              #Filter valid tiles to those <= number of availabile spaces
              valid_tiles = valid_tiles[valid_tiles["Tile_Width"] <= space]

              #Filter out previous tiles if possible
              if valid_tiles.shape[0] > 1: 
                valid_tiles = valid_tiles[valid_tiles["Tile_Label"] != placement[c][r - 1]]
 
              #Choose one from list of valid
              next_tile = valid_tiles.sample(n = 1)
              
              for l in range(next_tile["Tile_Length"].to_numpy()[0]):
                
                for w in range(next_tile["Tile_Width"].to_numpy()[0]):
                
                  placement[c + l][r + w] = next_tile["Tile_Label"].to_numpy()[0]

    return placement
