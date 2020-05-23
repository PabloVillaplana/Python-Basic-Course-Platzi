def average_temps(temps):
    som_of_temps = 0

    for temp in temps:
        som_of_temps += float(temp)

    return som_of_temps / len(temps)


if __name__ == "__main__":
    temps = [21,24,10,20,23,54]
    result = average_temps(temps)

    print('La temperatura promiedo es: {:.0f} %'.format(result))