import standardatmo
import matplotlib.pyplot as plt

# get atmo data from -1000 to 80000 m
altitude_data = []
pressure_data = []
temperature_data = []


for h in range(-1000,80000,100):
    altitude_data.append(h)
    data = standardatmo.getAtmoData(h) # get all data at the altitude
    pressure_data.append(data['pressure'])
    temperature_data.append(data['temperature'])


plt.plot(altitude_data, pressure_data, label = 'pressure')
plt.plot(altitude_data, temperature_data, label = 'temperature')


plt.legend()
plt.show()
