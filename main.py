readings = [2.1, 3.4, 5.6, 7.2, 9.1, 11.3]
def titrations(readings):
    minimum = min(readings)
    maximum = max(readings)
    crossing = None

    for position, reading in enumerate(readings):

        if reading >= 7:
            crossing = position, reading
            break

    if crossing is None:
            print("pH never crossed the neutral point")
    return crossing, minimum, maximum
results = titrations(readings)

crossing, minimum, maximum = results
if crossing is None:
    exit(0)
index, ph = crossing

print(f"Minimum pH: {minimum}")
print(f"Maximum pH: {maximum}")
print(f"Neutral point crossed at index: {index}")





