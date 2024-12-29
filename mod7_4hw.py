#Пример входных данных:
team1_num = 5 # количество участников первой команды
team2_num = 6 # количество участников второй команды
score_1 = 40 # количество задач, решённых командой 1
score_2 = 42 # количество задач, решённых командой 2
team1_time = 18015.2 # время, за которое команда 1 решила задачи
team2_time = 2153.31451 # время, за которое команда 2 решила задачи
tasks_total = 82 # общее количество решённых задач
time_avg = 350.4 # среднее время решения задач
challenge_result = 'Результат битвы' # исход соревнования

# Использование %:
print('В команде Мастера кода участников: %s !' % (team1_num))
print('Итого сегодня в командах участников %s и %s !' % (team1_num, team2_num))

# Использование format():
print('Команда Волшебники данных решила задач {} !' .format(score_2))
print('Волшебники данных решили задачи за {} !' .format(team1_time))

#Использование f-строк, Вариант №1: ручной ввод
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'{challenge_result}: победа команды Мастера кода!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

# Использование f-строк: Вариант №2: с расчётом
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result2 = 'Победа команды Мастера кода'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result2 = 'Победа команды Волшебники Данных!'
else:
    challenge_result2 = 'Ничья!'

tasks_total2 = score_1 + score_2
time_avg2 = (team1_time + team2_time) / 2

print(f'{challenge_result2} !')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg2} секунды на задачу!')

