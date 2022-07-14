import datetime
import time
import locale

locale.setlocale(locale.LC_ALL, "")

# Убираем милисекунды с даты
now = datetime.datetime.now().strftime("%d %B %Y (%A)")

deposit = float(input('Сколько денег тебе пришло?'))
cost = float(input('Сколько денег тебе нужно потратить на важные расходы?'))

balance = deposit - cost

print('Столько денег осталось на различные плюшки:', balance)

# задержка с которой закроется консолька
time.sleep(3)

# команда открытия файла, метод 'a' требуется для дозаписи
with open('uchet.txt', 'a') as file:
    file.write('\n')
    file.write(str(now))
    file.write(' | ')
    file.write(' Денег осталось: ')
    file.write(str(balance))
    file.close()

