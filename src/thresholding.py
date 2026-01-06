import numpy as np

def apply_irbt_threshold(Tb, threshold=235):
    """
    Returns a binary mask
    1 = cold cloud (TCC candidate)
    0 = non-cloud / warm region
    """

    mask = Tb <= threshold
    return mask.astype(int)


"""if __name__ == "__main__":
    # Test using sample data
    from data_loader import load_sample_irbt

    Tb, lat, lon = load_sample_irbt()

    cloud_mask = apply_irbt_threshold(Tb)

    print("Threshold Applied")
    print("Cold Pixel Count:", cloud_mask.sum())"""
