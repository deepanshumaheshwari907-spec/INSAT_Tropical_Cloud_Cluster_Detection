def classify_severity(min_tb):
    if min_tb < 205:
        return "Severe"
    elif min_tb < 220:
        return "Moderate"
    else:
        return "Weak"
