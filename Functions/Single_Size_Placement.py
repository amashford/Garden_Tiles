def place_tiles(area , tiles, type = 'ordered'):
    placement = []
    
    num_of_tiles_per_row = int(area[0] / tiles["Tile_Width"].mean())
    num_of_tiles_per_col = int(area[1] / tiles["Tile_Length"].mean())

    for c in range(num_of_tiles_per_col):
        cur_row_tiles = []

        for r in range(num_of_tiles_per_row):
            
            if c == 0 and r == 0:

              rand = rnd.randint(0,len(tiles.index) - 1)
              cur_row_tiles.append(tiles["Tile_Label"][rand])
              prev_tile = tiles["Tile_Label"][rand]
            
            elif type == 'ordered':

              next_tile_index = (tiles.index[tiles["Tile_Label"] == prev_tile][0] + 1) % len(tiles.index)
              next_tile = tiles["Tile_Label"][next_tile_index]
              cur_row_tiles.append(next_tile)
              prev_tile = next_tile
          
            elif type == 'random':

              rand = rnd.randint(0,len(tiles.index) - 1)
              cur_row_tiles.append(tiles["Tile_Label"][rand])

        placement.append(cur_row_tiles)
        prev_tile = cur_row_tiles[0]
    return placement
