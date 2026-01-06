import numpy as np

def load_sample_irbt():
    # fake brightness temperature grid (200 x 200 pixels)
    Tb = np.random.randint(200, 290, (200, 200))

    # fake latitude grid
    lat = np.linspace(-20, 20, 200)

    # fake longitude grid
    lon = np.linspace(40, 120, 200)

    return Tb, lat, lon


if __name__ == "__main__":
    Tb, lat, lon = load_sample_irbt()
    print("Sample Data Loaded")
    print("Temperature Shape:", Tb.shape)
