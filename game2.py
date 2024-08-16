import random
import time
import sqlite3

conn = sqlite3.connect('project.db')
cur = conn.cursor()

def test(id,type):

    cur.execute(f"SELECT * FROM words WHERE id={id};")
    all_results = cur.fetchone()
    if type == "ru_eng":
         lang = "русского"
         w = all_results[2]
         r = all_results[1]
    else:
         lang = "английского"
         w = all_results[1]
         r = all_results[2]
  
    print (f"Как переводится с {lang} языка слово {w}?")
    answer = input () 
    
    if answer == r:
        print ("Правильно")
        return 1
    else:
        print ("Неверно.", answer, "," , r)
        return 0

print ("Введите своё имя.")
name = input()
print ("Введите количество вопросов.")
full = input ()
right = 0
print ("Введите направление перевода eng_ru  или ru_eng.")
type = input ()

for i in range(0, int(full)):
    a = random.randint (93, 1095)
    result = test(a,type)
    right += result
    now = int( time.time() )
    
    cur.execute(f"INSERT INTO results(user, word_id, result, date_time, type) VALUES('{name}', '{a}', '{result}', '{now}', '{type}')  RETURNING id;")
    row = cur.fetchone()
print (f"Вы ответили правильно на {right} вопрос из {full}. ")
conn.commit()

