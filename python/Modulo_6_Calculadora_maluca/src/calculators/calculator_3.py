from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)

    variance = self.__calculate_variance(input_data)

    multiplication = self.__calculate_multiplation(input_data)

    self.__verify_results(variance, multiplication)
       
    formated_response = self.__format_response(variance)

    return formated_response

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise Exception("body mal formatado!")
    
    input_data = body['numbers']
    return input_data
  
  def __calculate_variance(self, numbers: List[float]) -> float:
    variante = self.__driver_handler.variance(numbers)

    return variante
  
  def __calculate_multiplation(self, numbers: List[float])-> float:
    multiplication = 1

    for num in numbers: multiplication *=num

    return multiplication
  
  def __verify_results(self, variance: float, multiplication: float) -> None:
    if variance < multiplication:
      raise Exception('Falha no processo: Variância menor que multiplicação!')
    

  def __format_response(self, variance: float) -> Dict:
    return {
      "data": {
        "calculator": 3,
        "value": float(variance),
        "success": True
      }
    } 