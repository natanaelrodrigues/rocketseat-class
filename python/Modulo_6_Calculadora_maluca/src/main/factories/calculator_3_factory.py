from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

def calculator_3_factory():
  nypy_handler = NumpyHandler()
  calc = Calculator3(nypy_handler)
  return calc