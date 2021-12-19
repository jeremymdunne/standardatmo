# code to load in the atmospheric file
from os import path # for relative path import
import csv # for atmo data reading



######### CONSTANTS ##########
ATMO_ALTITUDE_INDEX = 0
ATMO_TEMPERATURE_INDEX = 1
ATMO_GRAVITY_INDEX = 2
ATMO_PRESSURE_INDEX = 3
ATMO_DENSITY_INDEX = 4
ATMO_VISCOSITY_INDEX = 5
__atmodata = {}


########### CODE ##########
def loadAtmoData():
    global __atmodata
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "resources", "standard_atmospheric_data.txt"))
    __atmodata = {
    "altitude":[], "temperature": [],"gravity": [],
    "pressure": [],"density": [],"viscosity": []
    }
    with open(filepath, newline='') as atmofile:
        atmoreader = csv.reader(atmofile, delimiter=',')
        for row in atmoreader:
            try:
                linedata = []
                for i in row:
                    linedata.append(float(i))
                __atmodata["altitude"].append(linedata[ATMO_ALTITUDE_INDEX])
                __atmodata["temperature"].append(linedata[ATMO_TEMPERATURE_INDEX])
                __atmodata["gravity"].append(linedata[ATMO_GRAVITY_INDEX])
                __atmodata["pressure"].append(linedata[ATMO_PRESSURE_INDEX])
                __atmodata["density"].append(linedata[ATMO_DENSITY_INDEX])
                __atmodata["viscosity"].append(linedata[ATMO_VISCOSITY_INDEX])
            except:
                pass
    atmofile.close()

def getAtmoData(altitude):
    # create a named dictionary of the data
    dict = {
        "altitude":altitude, "temperature": None,"gravity": None,
        "pressure": None,"density": None,"viscosity": None
        }
    # interpolate for each data set
    for key in dict.keys():
        if key != 'altitude':
            dict[key] = atmoInterpolate(altitude, key)
    return dict

def getTemperatureData(altitude):
    return atmoInterpolate(altitude, 'temperature')

def getGravityData(altitude):
    return atmoInterpolate(altitude, 'gravity')

def getPressureData(altitude):
    return atmoInterpolate(altitude, 'pressure')

def getDensityData(altitude):
    return atmoInterpolate(altitude, 'density')

def getViscosityData(altitude):
    return atmoInterpolate(altitude, 'viscosity')

def atmoInterpolate(altitude, key):
    # linear interpolation
    # find closest index
    y_data = __atmodata[key]
    x_data = __atmodata['altitude']
    n = 0
    if (altitude < x_data[0]) or (altitude > x_data[-1]):
        print("WARNING! standardatmo DATA SET OUT OF BOUNDS, INTERPOLATING PAST KNOWN DATA")
    for i in range(0, len(x_data)):
        if x_data[i] < altitude:
            n = i
            break
    # linear
    y_inter = (y_data[n] * (x_data[n+1] - altitude) + y_data[n+1] * (altitude - x_data[n])) / (x_data[n+1] - x_data[n])
    return y_inter



loadAtmoData()

if __name__ == '__main__':
    getAtmoData(-1200)
