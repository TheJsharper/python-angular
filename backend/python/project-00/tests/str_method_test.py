import unittest
class TestStringMethod(unittest.TestCase):
    
    def test_upper(self):
        #Arrange
        line="foo"
        expected="FOO"
        
        #Act
        result=line.upper()
        
        #Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()