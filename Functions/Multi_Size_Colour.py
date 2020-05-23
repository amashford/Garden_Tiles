import pandas as pd 
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from matplotlib import colors

def colour_tiles(tiles, area):

  #Create discrete colormap
  cmap = colors.ListedColormap(tiles["Tile_Colour"])
  bounds = tiles.index.to_list()
  bounds.append(len(tiles.index))
  norm = colors.BoundaryNorm(bounds, cmap.N)

  #Create a lookup dictionary to replace tile labels with numeric values
  lookup = dict(zip(tiles["Tile_Label"], tiles.index.to_list()))

  #Create the tile arrangement
  arrangement = place_tiles(area, tiles)

  #Replace the tile labels with numbers
  data = []

  for line in arrangement:
    n_line = (pd.Series(line)).map(lookup)
    data.append(list(n_line))

  #Create the plot
  fig, ax = plt.subplots()
  ax.imshow(data, cmap=cmap, norm=norm)

  #Draw gridlines
  ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)

  #Set plot area
  ax.set_xticks(np.arange(-0.5, area[0], 1));
  ax.set_yticks(np.arange(-0.5, area[1], 1));

  #Hide Tick Labels
  ax.set_xticklabels([]);
  ax.set_yticklabels([]);

  #Show plot
  plt.show()
