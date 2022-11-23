import pytest
from app.calculator import Calculator

class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 2, 2) == 4

   def test_multiply_failed(self):
       assert self.calc.multiply(self, 2, 2) == 5



   def test_division_correctly(self):
       assert self.calc.division(self, 4, 4) == 1

   def test_division_failed(self):
       assert self.calc.division(self, 4, 4) == 2



   def test_adding(self):
       assert self.calc.adding(self, 2, 3) == 5

   def test_adding_failed(self):
       assert self.calc.adding(self, 2, 3) == 6



   def test_subtraction(self):
       assert self.calc.adding(self, 3, 2) == 1

   def test_subtraction_failed(self):
       assert self.calc.adding(self, 3, 2) == 2
