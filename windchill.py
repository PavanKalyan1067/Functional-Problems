import math


def wind_chill():
    t = int(input("Enter the Temperature between '0' to '50': "))
    if (t >= 0) and (t <= 50):
        print()
        v = int(input("Enter the wind speed between '3' to '120': "))
        if (v >= 3) and (v <= 120):
            converter = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
            print()
            print("Temperature = ", t)
            print("Wind speed = ", v)
            print("Wind chill = ", converter)


if __name__ == '__main__':
    wind_chill()
