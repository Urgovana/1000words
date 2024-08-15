#ИГРА
#импортировать нужные библиотеки
import random
import sqlite3

#Подключиться к БД
conn = sqlite3.connect('project.db')
cur = conn.cursor()
#Определить рандомное число = id
a = random.randint (93, 1095)
#print (a)
#Получить из БД строку где id = а

cur.execute(f"SELECT * FROM words WHERE id={a};")
all_results = cur.fetchone()
#print(all_results)

#read word w
w = all_results[1]
#print (w)
print (f"Как переводится с english языка слово {w}?")
answer = input () #- получить ответ от пользователя
#print (answer)
#Если введиённый ответ = значению из БД то
r = all_results[2]
if answer == r:
    print ("Правильно")
#else: print: ("Неверно.", ответ пользователя, значение из БД)
else:
    print ("Неверно.", answer, "," , r)
