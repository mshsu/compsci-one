import datetime
import json
import math
import ssl
import urllib.request
from operator import attrgetter


class Earthquake:
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return (self.place == other.place and
                math.isclose(self.mag, other.mag) and
                math.isclose(self.longitude, other.longitude) and
                math.isclose(self.latitude, other.latitude) and
                self.time == other.time)

    def __repr__(self):
        return ('%s %s %s %s %s' %
                (self.mag, self.longitude, self.latitude,
                 self.time, self.place))

    def __str__(self):
        return ('(%.2f) %40s at %s (%.3f, %.3f)' %
                (self.mag, self.place, time_to_str(self.time),
                 self.longitude, self.latitude))


def quake_from_feature(feature):
    prop = feature['properties']
    coords = feature['geometry']['coordinates']
    return Earthquake(prop['place'], prop['mag'],
                      float(coords[0]), float(coords[1]),
                      int(prop['time']) // 1000)


def read_quakes_from_file(filename):
    in_file = open(filename, 'r')
    quakes = []
    raw_data = []
    new_place = ''
    new_quake = None
    for line in in_file:
        raw_data = line.split()
        new_place = ' '.join(raw_data[4:])
        new_quake = Earthquake(new_place, float(raw_data[0]),
                               float(raw_data[1]), float(raw_data[2]),
                               int(raw_data[3]))
        quakes.append(new_quake)
        raw_data = []
        new_place = ''
        new_quake = None
    in_file.close()
    return quakes


def filter_by_mag(quakes, low, high):
    return [quake for quake in quakes if (quake.mag >= low and
                                          quake.mag <= high)]


def filter_by_place(quakes, word):
    return [quake for quake in quakes if word.lower() in quake.place.lower()]


def sort_quakes(quakes, choice):
    if choice == 'm':
        return sorted(quakes, key=attrgetter('mag'), reverse=True)
    elif choice == 't':
        return sorted(quakes, key=attrgetter('time'), reverse=True)
    elif choice == 'l':
        return sorted(quakes, key=attrgetter('longitude'))
    elif choice == 'a':
        return sorted(quakes, key=attrgetter('latitude'))


# NOTE: Do not change this function.
def get_json(url):
    """Gets JSON data from the given url, and returns it as a
    dictionary.

    Args:
        url: A string of the url from which to get the JSON data.

    Returns:
        A dictionary with the JSON data.
    """
    ctx = ssl.SSLContext()
    with urllib.request.urlopen(url, context=ctx) as response:
        response_text = response.read().decode('utf-8')

    return json.loads(response_text)


# NOTE: Do not change this function.
def time_to_str(time):
    """Converts the given Unix time stamp to a formatted string.

    Args:
        time: An integer number of seconds since Jan 1, 1970 00:00 UTC

    Returns:
        The time string formatted as YY-MM-DD HH:MM:SS in the local time
        zone.
    """
    return datetime.datetime.fromtimestamp(time).isoformat(
        sep=' ', timespec='seconds')
