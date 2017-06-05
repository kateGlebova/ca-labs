"""
Unit test for Serializer subclasses.
"""

from io import StringIO, BytesIO
import unittest

from serialization.json_serialization import JSONSerializer
from serialization.pickle_serialization import PICKLESerializer
from serialization.yaml_serialization import YAMLSerializer


class TestSerializeMethods(unittest.TestCase):

    def setUp(self):
        self.data = {"bmr":
                         {"1503.7": {"sex": "female", "age": 45, "weight": 78.0, "height": 173.0},
                          "805.4": {"sex": "male", "age": 48, "weight": 34.0, "height": 120.0}
                          },
                     "calories":
                         {"1877.3": {"sex": "male", "age": 46, "weight": 93.0, "height": 170.0, "exercise_level": "None"},
                          "805.4": {"sex": "male", "age": 48, "weight": 34.0, "height": 120.0, "exercise_level": "None"}
                          },
                     "bmi":
                         {"17.67453604342886": {"weight": 56.0, "height": 178.0},
                          "23.61111111111111": {"weight": 34.0, "height": 120.0}
                          }
                     }

    def test_pickle(self):
        """
        Test pickle serialization.
        """
        with BytesIO() as io:
            PICKLESerializer.s_dump(self.data, io)
            dumped = io.getvalue()

        with BytesIO(dumped) as io:
            extracted_data = PICKLESerializer.s_load(io)

        self.assertEqual(self.data, extracted_data)

    def test_yaml(self):
        """
        Test yaml serialization.
        """
        with StringIO() as io:
            YAMLSerializer.s_dump(self.data, io)
            dumped = io.getvalue()

        with StringIO(dumped) as io:
            extracted_data = YAMLSerializer.s_load(io)

        self.assertEqual(self.data, extracted_data)

    def test_json(self):
        """
        Test json serialization.
        """
        with StringIO() as io:
            JSONSerializer.s_dump(self.data, io)
            dumped = io.getvalue()

        with StringIO(dumped) as io:
            extracted_data = JSONSerializer.s_load(io)

        self.assertEqual(self.data, extracted_data)


if __name__ == "__main__":
    unittest.main()