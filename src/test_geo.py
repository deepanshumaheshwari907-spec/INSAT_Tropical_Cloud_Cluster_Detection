import numpy as np
from insat_reader import load_tb_lat_lon

Tb, lat, lon = load_tb_lat_lon()

print("Lat min =", np.nanmin(lat))
print("Lat max =", np.nanmax(lat))

print("Lon min =", np.nanmin(lon))
print("Lon max =", np.nanmax(lon))
