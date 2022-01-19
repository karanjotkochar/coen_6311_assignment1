import unittest
import compare_values


class TestClass(unittest.TestCase):
    def test_distance(self):  # Test Case 1 Distance between two same locations
        self.assertEqual(compare_values.get_distance((29.927395, 73.870167), (29.927395, 73.870167)), 0)

    def test_coordinate_boundaries(self):   # Test Case 2 Range of latitude and longitude in coordinates
        self.assertRaises(ValueError, compare_values.get_distance, (-92.927395, 73.870167), (29.927395, 73.870167))
        self.assertRaises(ValueError, compare_values.get_distance, (29.927395, 73.870167), (92.927395, 73.870167))
        self.assertRaises(ValueError, compare_values.get_distance, (29.927395, 180.870167), (29.927395, 73.870167))
        self.assertRaises(ValueError, compare_values.get_distance, (29.927395, 73.870167), (29.927395, -180.870167))

    def test_coordinate_format(self):   # Test Case 3 Format condition of describing latitude and longitude
        self.assertRaises(ValueError, compare_values.get_distance, (-92.927395, 56.894561, 73.870167), (29.927395, 73.870167))
        self.assertRaises(ValueError, compare_values.get_distance, (-92.927395, 73.870167), (29.927395, 56.894561, -73.870167))
        self.assertRaises(ValueError, compare_values.get_distance, (-92.927395, 56.894561, 73.870167), (29.927395, 56.894561, -73.870167))

    def test_coordinate_value(self):   # Test Case 4 Output condition for distance between coordinates
        self.assertIsNotNone(compare_values.get_distance, ((29.927395, 73.870167), (29.927395, 73.870167)))

    def test_input_datatype(self):   # Test Case 5 Datatype conditions for variable describing distance and limit
        self.assertRaises(TypeError, compare_values.check_limit)

    def test_input_value(self):   # Test Case 6 Output condition for variable describing distance and limit
        self.assertIsNotNone(compare_values.check_limit)


if __name__ == '__main__':
    unittest.main()
