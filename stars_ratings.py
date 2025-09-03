def StarRating(strParam):
    # Convert input to float and round to nearest 0.5
    rating = round(float(strParam) * 2) / 2
    stars = []
    # Add full stars
    full = int(rating)
    half = 1 if rating - full == 0.5 else 0
    empty = 5 - full - half
    stars += ["full"] * full
    if half:
        stars.append("half")
    stars += ["empty"] * empty
    return " ".join(stars)