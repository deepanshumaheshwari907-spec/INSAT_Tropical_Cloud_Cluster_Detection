def generate_tcc_summary(tcc):

    min_tb = tcc["min_tb"]
    mean_tb = tcc["mean_tb"]
    radius = tcc["mean_radius_km"]
    std_tb = tcc["std_tb"]

    summary_parts = []

    # ------ Convection Strength ------
    if min_tb < 200:
        summary_parts.append("Very deep and intense convection")
    elif min_tb < 220:
        summary_parts.append("Strong deep convective cloud system")
    elif min_tb < 240:
        summary_parts.append("Moderate convective cloud cluster")
    else:
        summary_parts.append("Weak or shallow cloud system")

    # ------ Cluster Size ------
    if radius > 300:
        summary_parts.append("with large spatial spread")
    elif radius > 150:
        summary_parts.append("with medium spatial extent")
    else:
        summary_parts.append("with small spatial coverage")

    # ------ Cloud Organization ------
    if std_tb < 10:
        summary_parts.append("and highly organised cloud structure")
    else:
        summary_parts.append("and fragmented convection pattern")

    return " ".join(summary_parts)
