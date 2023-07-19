import unittest
import cal


class CalculatorTest(unittest.TestCase):
  def test_nothing(self):
    self.s = cal.cal(2,1,"sum")
    self.assertEqual(self.s,3)
  def test_nothing(self):
    self.s = cal.cal(2,1,"sum")
    self.assertEqual(self.s,2)
  

# if __name__ == '__main__':
#   unittest.main()

# python3 -m unittest test_cal.py