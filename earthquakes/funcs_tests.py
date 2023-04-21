import unittest

import quake_funcs


class TestCases(unittest.TestCase):
    def test_earthquake_init(self):
        quake = quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290)

        self.assertEqual(quake.place, '12km SSW of Idyllwild, CA')
        self.assertAlmostEqual(quake.mag, 0.97)
        self.assertAlmostEqual(quake.longitude, -116.7551651)
        self.assertAlmostEqual(quake.latitude, 33.6391678)
        self.assertEqual(quake.time, 1488177290)

    def test_earthquakes_equal_0(self):
        quake1 = quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290)
        quake2 = quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290)
        self.assertEqual(quake1, quake2)

    def test_earthquakes_equal_1(self):
        quake1 = quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290)
        quake2 = quake_funcs.Earthquake(
            '13km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290)
        self.assertNotEqual(quake1, quake2)

    def test_earthquakes_repr_0(self):
        quake1 = quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290)
        repr1 = ('0.97 -116.7551651 33.6391678 1488177290 ' +
                 '12km SSW of Idyllwild, CA')

        self.assertEqual(repr(quake1), repr1)

    def test_earthquakes_repr_1(self):
        quake2 = quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538)
        repr2 = ('2.19 -121.5801697 36.9580002 1488173538 ' +
                 '5km S of Gilroy, California')

        self.assertEqual(repr(quake2), repr2)

    def test_earthquakes_str_0(self):
        quake1 = quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290)
        str1 = ('(0.97)                12km SSW of Idyllwild, CA ' +
                'at 2017-02-26 22:34:50 (-116.755, 33.639)')

        self.assertEqual(str(quake1), str1)

    def test_earthquakes_str_1(self):
        quake2 = quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538)
        str2 = ('(2.19)              5km S of Gilroy, California ' +
                'at 2017-02-26 21:32:18 (-121.580, 36.958)')

        self.assertEqual(str(quake2), str2)

    def test_sort_quakes_0(self):
        quakes = []
        quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        sorted_quakes = []
        sorted_quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        sorted_quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))
        sorted_quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))

        self.assertEqual(quake_funcs.sort_quakes(quakes, 'm'), sorted_quakes)

    def test_sort_quakes_1(self):
        quakes = []
        quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        sorted_quakes = []
        sorted_quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))
        sorted_quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        sorted_quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))

        self.assertEqual(quake_funcs.sort_quakes(quakes, 't'), sorted_quakes)

    def test_sort_quakes_2(self):
        quakes = []
        quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        sorted_quakes = []
        sorted_quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))
        sorted_quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        sorted_quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))

        self.assertEqual(quake_funcs.sort_quakes(quakes, 'l'), sorted_quakes)

    def test_sort_quakes_3(self):
        quakes = []
        quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        sorted_quakes = []
        sorted_quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        sorted_quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        sorted_quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        self.assertEqual(quake_funcs.sort_quakes(quakes, 'a'), sorted_quakes)

    # NOTE: This test requires that you *do not* modify quake_test0.txt.
    def test_read_file_0(self):
        quakes = quake_funcs.read_quakes_from_file(
            'test_files/quake_test0.txt')

        expected_quakes = []
        expected_quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        expected_quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))

        self.assertEqual(quakes, expected_quakes)

    def test_filter_by_mag_0(self):
        quakes = []
        quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        filtered = []
        filtered.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        filtered.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        self.assertEqual(quake_funcs.filter_by_mag(quakes, 1, 3), filtered)

    def test_filter_by_place_0(self):
        quakes = []
        quakes.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        quakes.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))
        quakes.append(quake_funcs.Earthquake(
            '100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548,
            1488219604))

        filtered = []
        filtered.append(quake_funcs.Earthquake(
            '12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678,
            1488177290))
        filtered.append(quake_funcs.Earthquake(
            '5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002,
            1488173538))

        self.assertEqual(quake_funcs.filter_by_place(quakes, 'ca'), filtered)

    # TODO: Remove the quotation marks once you're ready to test working
    # with JSON data.

    def test_quake_from_feature(self):
        feature = {
            'geometry': {
                'coordinates': [
                    -117.4906667,
                    33.9131667,
                    0.25
                ],
                'type': 'Point'
            },
            'id': 'ci37814000',
            'properties': {
                'code': '37814000',
                'detail': ('http://earthquake.usgs.gov/'
                           'earthquakes/feed/v1.0/detail/ci37814000.geojson'),
                'dmin': 0.2836,
                'gap': 87,
                'ids': ',ci37814000,',
                'mag': 1.24,
                'magType': 'ml',
                'net': 'ci',
                'nst': 8,
                'place': '5km NE of Home Gardens, CA',
                'rms': 0.27,
                'sig': 24,
                'sources': ',ci,',
                'status': 'automatic',
                'time': 1488179250520,
                'title': 'M 1.2 - 5km NE of Home Gardens, CA',
                'tsunami': 0,
                'type': 'earthquake',
                'types': (',geoserve,nearby-cities,origin,phase-data,'
                          'scitech-link,'),
                'tz': -480,
                'updated': 1488179487273,
                'url': ('http://earthquake.usgs.gov/'
                        'earthquakes/eventpage/ci37814000')
            },
            'type': 'Feature'
        }

        quake = quake_funcs.quake_from_feature(feature)
        expected_quake = quake_funcs.Earthquake(
            '5km NE of Home Gardens, CA', 1.24, -117.4906667, 33.9131667,
            1488179250)
        self.assertEqual(quake, expected_quake)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
