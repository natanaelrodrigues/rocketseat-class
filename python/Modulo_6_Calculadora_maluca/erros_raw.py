
class HttpUnprocessableEntityError(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)
    self.message = message
    self.name = 'HttpUnprocessableEntityError'
    self.status_code = 422


try:
  print('Estou no bloco try')
  raise HttpUnprocessableEntityError('Estou lançando a exception')
except Exception as exception:
  print('Estou no except - tratamento de erro')
  print(f'Status name: {exception.name}')
  print(f'Status code: {exception.code}')
  print(f'Status message: {exception.message}')