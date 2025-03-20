from abc import ABC, abstractmethod

class NotificationSender(ABC):

  @abstractmethod
  def send_notification(self, message: str) -> None:
    pass

# Definir a regra de construção para as demais classes
class EmailNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
    print(f'Email Message {message}')

class SMSNotificationSender(NotificationSender):
  def send_notification(self, message: str) -> None:
    print(f'SMS Message {message}')    


class Notificator:
  def __init__(self, notification_sender: NotificationSender) ->None:
    self.__notification_sender = notification_sender
  
  def send(self, message: str) -> None:
    #Validação de dados
    self.__notification_sender.send_notification(message)




obj = EmailNotificationSender()
obj.send_notification('Ola Mundo!')
print()
obj = SMSNotificationSender()
obj.send_notification('Ola Mundo!')
print()
obj = Notificator(SMSNotificationSender())
obj.send('Olá mundo via Notificador')