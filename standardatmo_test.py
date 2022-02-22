import standardatmo
import matplotlib.pyplot as plt

# get atmo data from -1000 to 80000 m
altitude_data = []
pressure_data = []
temperature_data = []
gravity_data = []
density_data = []
viscosity_data = []

for h in range(-1000,80000,10):
    altitude_data.append(h)
    data = standardatmo.getAtmoData(h)
    pressure_data.append(data['pressure'])
    # temperature_data.append(standardatmo.getTemperatureData(h))
    # gravity_data.append(standardatmo.getGravityData(h))
    # density_data.append(standardatmo.getDensityData(h))
    # viscosity_data.append(standardatmo.getViscosityData(h))



plt.plot(altitude_data, pressure_data, label = 'pressure')
# plt.plot(altitude_data, temperature_data, label = 'temperature')
# plt.plot(altitude_data, gravity_data, label = 'gravity')
# plt.plot(altitude_data, density_data, label = 'density')
# plt.plot(altitude_data, viscosity_data, label = 'viscosity')

plt.legend()
plt.show()
