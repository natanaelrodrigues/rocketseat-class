import numpy
from typing import List

class NumpyHandler:
  def __init(self) -> None:
    self.__np = numpy

  def standard_derivarion(self, numbers: List[float]) -> float:
    return self.__np.std(numbers)