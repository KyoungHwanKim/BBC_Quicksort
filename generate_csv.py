import random
import csv

f = open('number.csv', 'w', encoding='utf-8')
w = csv.writer(f)

num = [random.randint(-1000000, 1000000) for _ in range(1000000)]
w.writerow(num)
f.close()