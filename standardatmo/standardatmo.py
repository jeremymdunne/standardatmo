# code to load in the atmospheric file
from os import path # for relative path import
import csv # for atmo data reading



######### CONSTANTS ##########
ATMO_ALTITUDE_INDEX = 0
ATMO_GEOPOTENTIAL_ALTITUDE_INDEX = 1
ATMO_TEMPERATURE_INDEX = 2
ATMO_PRESSURE_INDEX = 3
ATMO_DENSITY_INDEX = 4
ATMO_SPEED_OF_SOUND_INDEX = 5
ATMO_GRAVITY_INDEX = 6
ATMO_DYNAMIC_VISCOSITY_INDEX = 7
ATMO_KINEMATIC_VISCOSITY_INDEX = 8
ATMO_NUMBER_DENSITY_INDEX = 9
ATMO_PARTICLE_SPEED_INDEX = 10
ATMO_COLLISION_FREQUENCY_INDEX = 11
ATMO_MEAN_FREE_PATH_INDEX = 12
ATMO_THERMAL_CONDUCTIVITY_INDEX = 13
ATMO_MOLECULAR_WEIGHT_INDEX = 14
ATMO_PRESSURE_SCALE_HEIGHT_INDEX = 15


__atmodata = {}


########### CODE ##########
def loadAtmoData():
    global __atmodata
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "resources", "data.csv"))
    __atmodata = {
    "altitude":[], "geopotential_altitude":[], "temperature": [], "pressure":[],
    "density": [], "speed_of_sound":[], "gravity": [], "dynamic_viscosity":[],
    "kinematic_viscosity":[],"number_density":[], "particle_speed":[],
    "collision_frequency":[],"mean_free_path":[], "thermal_conductivity":[],
    "molecular_weight":[],"pressure_scale_height":[]
    }
    with open(filepath, newline='') as atmofile:
        atmoreader = csv.reader(atmofile, delimiter=',')
        for row in atmoreader:
            try:
                linedata = []
                for i in row:
                    linedata.append(float(i))
                __atmodata["altitude"].append(linedata[ATMO_ALTITUDE_INDEX] * 1000)
                __atmodata["geopotential_altitude"].append(linedata[ATMO_GEOPOTENTIAL_ALTITUDE_INDEX] * 1000)
                __atmodata["temperature"].append(linedata[ATMO_TEMPERATURE_INDEX])
                __atmodata["pressure"].append(linedata[ATMO_PRESSURE_INDEX])
                __atmodata["density"].append(linedata[ATMO_DENSITY_INDEX])
                __atmodata["speed_of_sound"].append(linedata[ATMO_SPEED_OF_SOUND_INDEX])
                __atmodata["gravity"].append(linedata[ATMO_GRAVITY_INDEX])
                __atmodata["dynamic_viscosity"].append(linedata[ATMO_DYNAMIC_VISCOSITY_INDEX])
                __atmodata["kinematic_viscosity"].append(linedata[ATMO_KINEMATIC_VISCOSITY_INDEX])
                __atmodata["number_density"].append(linedata[ATMO_NUMBER_DENSITY_INDEX])
                __atmodata["particle_speed"].append(linedata[ATMO_PARTICLE_SPEED_INDEX])
                __atmodata["collision_frequency"].append(linedata[ATMO_COLLISION_FREQUENCY_INDEX])
                __atmodata["mean_free_path"].append(linedata[ATMO_MEAN_FREE_PATH_INDEX])
                __atmodata["thermal_conductivity"].append(linedata[ATMO_THERMAL_CONDUCTIVITY_INDEX])
                __atmodata["molecular_weight"].append(linedata[ATMO_MOLECULAR_WEIGHT_INDEX])
                __atmodata["pressure_scale_height"].append(linedata[ATMO_PRESSURE_SCALE_HEIGHT_INDEX])
            except:
                pass
    atmofile.close()

def getAtmoData(altitude, key = None):
    if key is not None:
        return atmoInterpolate(altitude, key)
    else:
        # return all data at that point
        dict = {
        }
        for keys in __atmodata.keys():
            if keys is not "altitude":
                dict[keys] = atmoInterpolate(altitude, keys)
        return dict

def newtonsDividedDifferenceInterpolation(x, x_data, y_data):
    order = 10 # seems to fit the best 
    # bias to closest side
    arr = [] # rows, cols
    n = len(x_data) - 1# find index under the data
    for i in range(0,len(x_data) - 1):
        if x_data[i+1] > x:
            n = i
            break
    # correct for low data
    if x < x_data[0]:
        n = 0
    num_points = order + 1
    # bias order to closest data set
    if abs(x_data[n] - x) < abs(x_data[n+1]):
        # offset towards rear
        n_below = int(num_points/2 + 0.5)
        n_above = int(num_points/2)
    else:
        # offset above
        n_below = int(num_points/2 + 0.5)
        n_above = int(num_points/2)
    if n < n_below:
        n_below = n
        n_above = num_points - n_below
    elif (len(x_data) -1 - n) < n_above:
        n_above = len(x_data) - 1 - n
        n_below = num_points - n_above
    n_start = n - n_below
    for i in range(0, num_points):
        arr.append([n_start + i])
        arr[i].append(y_data[n_start + i])
    # print(arr)
    for i in range(2,order + 1): # col
        # construct the column
        for n in range(0, order - i + 2): # row
            # value = (arr[n][i-1] - arr[i+1][n-1]) / (x_data[arr[i][0]] - x_data[arr[i+1][0]])
            value = (arr[n][i-1] - arr[n+1][i-1]) / (x_data[arr[n][0]] - x_data[arr[n+i-1][0]])
            arr[n].append(value)
    # construct the final
    # print(arr)
    value = arr[0][1]
    for i in range(1, order): # col
        pre = 1
        for n in range(0, i): # row
            pre *= (x - x_data[arr[n][0]])
        # print(pre, ' ', arr[0][i+1])
        value += pre * arr[0][i+1]
    # print(value)
    return value

def atmoInterpolate(altitude, key):
    # use a fourth order newton's divided difference interpolation method
    arr = [] # rows, cols
    # find the closest lower index
    y_data = __atmodata[key]
    x_data = __atmodata['altitude']
<<<<<<< HEAD
    val = newtonsDividedDifferenceInterpolation(altitude, x_data, y_data)
    return val
=======
    n = 0
    if (altitude < x_data[0]) or (altitude > x_data[-1]):
        print("WARNING! standardatmo DATA SET OUT OF BOUNDS, INTERPOLATING PAST KNOWN DATA")
    # print('X_data ', x_data)
    # print('alt ', altitude)

    for i in range(0, len(x_data)):
        if x_data[i] > altitude:
            n = i-1
            break
    # print('n', n)
    # linear
    y_inter = (y_data[n] * (x_data[n+1] - altitude) + y_data[n+1] * (altitude - x_data[n])) / (x_data[n+1] - x_data[n])
    return y_inter

>>>>>>> 683da4d5e488c340b3f41e1286aa35ddb767ba33


loadAtmoData()

if __name__ == '__main__':
    # print(getAtmoData(1200))
    print(atmoInterpolate(3500, 'pressure'))
    # print(newtonsDividedDifferenceInterpolation(301, [300,304,305,307],[2.4771,2.4829,2.4843,2.4871]))
    # newtonsDividedDifferenceInterpolation(3499, [1000,2000,3000,4000,5000,6000],[])
