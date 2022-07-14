import datetime
import time

now = datetime.datetime.now().replace(microsecond=0)
deposit = float(input('Сколько денег тебе пришло?'))
cost = float(input('Сколько денег тебе нужно потратить на важные расходы?'))
balance = deposit - cost
print('Столько денег осталось на различные плюшки:', balance)
time.sleep(3)
with open('uchet.txt', 'a') as file:
    file.write('\n')
    file.write(str(now))
    file.write(' | ')
    file.write(' Денег осталось: ')
    file.write(str(balance))
    file.close()

