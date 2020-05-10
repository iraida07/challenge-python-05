import math


def square_area(side):
    """Returns the area of a square"""
    area = pow(side,2)
    return area

def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    area = base * height
    return area


def triangle_area(base, height):
    """Returns the area of a triangle"""
    area = (base * height) / 2
    return area


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    area = (diagonal_1 * diagonal_2) / 2
    return area


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    area = ((base_major + base_minor) / 2) * height
    return area


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    area = (perimeter * apothem)/2
    return area

def circumference_area(radius):
    """Returns the area of a circumference"""
    area = round((math.pi * pow(radius, 2)),2)
    return area

if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):
        def setUp(self):
            self.values = {
                'square_area' : 16,
                'rectangle_area': 35,
                'triangle_area': 10,
                'rhombus_area': 20,
                'trapezoid_area': 9,
                'regular_polygon_area': 12,
                'circumference_area': 28.27
            }

        def test_square_area(self):
            value = self.values.get('square_area')
            self.assertEqual(value, square_area(4))
        
        def test_rectangle_area(self):
            value = self.values.get('rectangle_area')
            self.assertEqual(value, rectangle_area(7,5))            

        def test_triangle_area(self):
            value = self.values.get('triangle_area')
            self.assertEqual(value, triangle_area(5,4))

        def test_rhombus_area(self):
            value = self.values.get('rhombus_area')
            self.assertEqual(value, rhombus_area(8,5))

        def test_trapezoid_area(self):
            value = self.values.get('trapezoid_area')
            self.assertEqual(value, trapezoid_area(3,3,3))

        def test_regular_polygon_area(self):
            value = self.values.get('regular_polygon_area')
            self.assertEqual(value, regular_polygon_area(8,3))            

        def test_circumference_area(self):
            value = self.values.get('circumference_area')
            self.assertEqual(value, circumference_area(3))
        
        def tearDown(self):
            del(self.values)

    unittest.main()
