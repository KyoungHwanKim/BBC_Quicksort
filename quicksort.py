import csv
import time
import psutil
import os


def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) - 1]  # 가장 마지막 원소를 pivot으로 설정

    L = [i for i in arr[:-1] if i <= pivot]
    R = [i for i in arr[:-1] if i > pivot]

    return QuickSort(L) + [pivot] + QuickSort(R)


f = open('number.csv', 'r', encoding='utf-8')
r = csv.reader(f)

num = list(r)[0]
num = list(map(int, num))

# 실행 전 메모리 체크
pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
print(f"실행 전 : {current_process_memory_usage_as_KB: 9.3f}KB")

# 시작 시간 체크
start = time.time()

result = QuickSort(num)

# 종료 시간 출력
print(round(time.time() - start, 3), "초 소요")

# 실행 후 메모리 체크
pid = os.getpid()
current_process = psutil.Process(pid)
current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
print(f"실행 후 : {current_process_memory_usage_as_KB: 9.3f}KB")

