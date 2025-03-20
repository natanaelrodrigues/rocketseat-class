from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator_2_factory():
  nypy_handler = NumpyHandler()
  calc = Calculator2(nypy_handler)
  return calc