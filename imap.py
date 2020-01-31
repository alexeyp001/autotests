import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993) # Создаем сессию для подключение по IMAP
mail.login('alexeyplet00@gmail.com', 'Privet123!') # Указываем логин/пароль
mail.list() # Выводим список папок в почтовом ящике
mail.select('Inbox') # Выбираем для работы папку входящие (inbox)

result, data = mail.search(None, '(FROM "support")') # Получаем массив со списком писем

ids = data[0] # Сохраняем в переменную строку с номерами писем
id_list = ids.split() # Получаем массив номеров писем
latest_email_id = id_list[-1] # Задаем переменную latest_email_id, значением которой будет номер последнего письма

result, data = mail.fetch(latest_email_id, "(RFC822)") # Получаем письмо с идентификатором latest_email_id (последнее письмо)
raw_email = data[0][1] # В переменную заносим необработанное письмо
raw_email_string = raw_email.decode('utf-8')
print(raw_email_string)

