from typing import Dict, List
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from pytest import raises

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandlerError:
  def variance(self, numbers: List[float]) -> float:
    return 3

class MockDriverHandler:
  def variance(self, numbers: List[float]) -> float:
    return 1000000

def test_calculate_with_variance_error():
  mock_request = MockRequest({"numbers": [1,2,3,4,5]})
  calculator3 = Calculator3(MockDriverHandlerError())

  with raises(Exception) as excinfo:
    calculator3.calculate(mock_request)

  assert str(excinfo.value) == 'Falha no processo: Variância menor que multiplicação!'
  print()
  print(excinfo.value)

def test_calculate():
  mock_request = MockRequest({"numbers": [1,1,1,1,100]})
  calculator3 = Calculator3(MockDriverHandler())

  response = calculator3.calculate(mock_request)

  assert "data" in response
  assert response == {'data': {'calculator': 3, 'value': 1000000, 'success': True}}
  

  print()
  print(response)
