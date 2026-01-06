import h5py
import numpy as np

def load_tb_lat_lon():

    filepath = "C:/Users/lenovo/OneDrive/Desktop/TCC_INSAT_Project/data/3DIMG_18JUN2024_0000_L1C_SGP_V01R00.h5"

    with h5py.File(filepath, "r") as f:

        # ---- Tb same as before ----
        raw = f["IMG_TIR1"][0]
        lut = f["IMG_TIR1_TEMP"][:]
        Tb  = lut[raw]

        X = f["X"][:]   # scan angle grid
        Y = f["Y"][:]

    # ---- INSAT geostationary constants ----
    sat_lon = 82.0          # INSAT-3D longitude (deg E)
    H       = 42164000.0    # satellite height (m)
    Re      = 6378137.0
    Rp      = 6356752.3

    # create mesh grid
    xx, yy = np.meshgrid(X, Y)

    x = np.deg2rad(xx)
    y = np.deg2rad(yy)

    # eqn from geos projection spec
    cosx = np.cos(x)
    cosy = np.cos(y)
    sinx = np.sin(x)
    siny = np.sin(y)

    a = (H * cosx * cosy)**2 - (cosy**2 + (Re/Rp)**2 * siny**2) * (H**2 - Re**2)

    a[a < 0] = np.nan
    a = np.sqrt(a)

    sn = (H*cosx*cosy - a) / (cosy**2 + (Re/Rp)**2 * siny**2)

    sx = sn * cosx * cosy
    sy = -sn * sinx * cosy
    sz =  sn * siny

    lon = np.rad2deg(np.arctan2(sy, sx)) + sat_lon
    lat = np.rad2deg(np.arctan((Re**2 / Rp**2) * (sz / np.sqrt(sx**2 + sy**2))))

    return Tb, lat, lon
