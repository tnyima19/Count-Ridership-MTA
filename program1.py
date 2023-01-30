"""Name: Tenzing Nyima
Email: Tenzing.Nyima71@myhunter.cuny.edu
Resources Used pyuthong.org as a reminder of python.
Program1
Date: Jan 29 2022
"""

def get_min_max(data, kind="min"):
    """get dictionary of minimum or maximum number of entries from the data"""
    new_dict = {}
    for num in data:
        #split the n
        info = num.split(',')
        if kind == "min":
            if info[1]+','+ info[2] in new_dict:
                if int(info[9]) < new_dict[info[1]+','+info[2]]:
                    new_dict[info[1]+','+ info[2]] = int(info[9])
            else:
                new_dict[info[1]+','+ info[2]] = int(info[9])
        else:
            if info[1]+','+ info[2] in new_dict:
                if int(info[9]) > new_dict[info[1]+','+info[2]]:
                    new_dict[info[1]+','+ info[2]] = int(info[9])
            else:
                new_dict[info[1]+','+ info[2]] = int(info[9])

    return new_dict

def get_station(data, kind)-> dict:
    """This function reutrns the dctionary of remote unit id+ turnstile unit number : Stations"""
    stations = {}
    if kind == "station":
        for num in data:
            information = num.split(',')
            stations[information[1]+','+information[2]] = information[3]

    return stations



def make_dictionary(data, kind = "min")-> dict:
    """Create a dictionary with a key of remote unit ID + turnstile unit number:
    max entry number(int) / min entry number(int) / stations(string)
    """
    if kind in ("min", "max"):
        min_max_dict = get_min_max(data, kind)
        return min_max_dict
    stations_dict = get_station(data, kind)
    return stations_dict


def get_turnstiles(station_dict, stations = None):
    """If the stations is None, returns the names of all the turnstiles storea skeys
    in teh inputted dictionary.If non-null, returns the eys which have value from
    stations in inputeted dictionary """
    names_of_turnstiles = []
    none_var = None
    if stations == none_var:
        for key in station_dict:
            names_of_turnstiles.append(key)
    else:
        for key in station_dict:
            if station_dict[key] in stations:
                names_of_turnstiles.append(key)
    return names_of_turnstiles


def compute_ridership(min_dict, max_dict, turnstiles = None):
    """Takes as input two dictionarires and a list, possibly empty of turnstiles.
    If no value is passed for turnstile, the default value of None is ued
    (that is , the total ridership for every station in the dictionaries).
    Returns the ridership (the difference between the minimum and maximum values)
    across all turnstiles specified"""
    total = 0
    #none_var = None
    #print("This is min Dict")
    #print(min_dict)
    #print("This is max Dict")
    #print(max_dict)
    if turnstiles == None:
        total = sum(min_dict.values()) + sum(max_dict.values())
    else:
        for turnstile_name in turnstiles:
            #if turnstile_name in max_dict:
            total += max_dict[turnstile_name]
            #if turnstile_name in min_dict:
            total -= min_dict[turnstile_name]

    return total


def main():
    """Opens a data file and computer s ridership, using functions above. """
    file_name = 'turnstile_220611.txt'
    #Store file contents in data:
    with open(file_name, encoding='UTF-8') as file_d:
        lines = file_d.readlines()
    #Discard first line with headers
    data = lines[1:]
    print(type(data))
    #Set up three dictinoary
    min_dict = make_dictionary(data, kind="min")
    print(min_dict)
    max_dict = make_dictionary(data, kind ="max")
    print(max_dict)
    station_dict = make_dictionary(data, kind="station")
    #Print out the station names, alphbetically, without duplicates:
    print(f'Allstations: {sorted(list(set(station_dict.values())))}')

    #All teh turnstiles from teh data:
    print(f'All turnstiles: {get_turnstiles(station_dict)}')
    #Print only for Hunter & Roservelt Isalnd stastion:
    ridership = compute_ridership(min_dict,max_dict, turnstiles=["R051,02-00-00"])
    print(f'Ridership for turnstile, RO51,02-00-00: {ridership}.')
    print(get_turnstiles(station_dict, stations = ['68ST-HUNTER CO','ROOSEVELT ISLND']))
    hunter_turns = get_turnstiles(station_dict, stations = ['68ST-HUNTER CO'])
    print(hunter_turns)
    ridership = compute_ridership(min_dict, max_dict, turnstiles = hunter_turns)
    print(f'Ridership for Hunter College: {ridership}.')

if __name__ == "__main__":
    main()
