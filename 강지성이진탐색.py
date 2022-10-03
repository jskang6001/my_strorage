import time
import random


def seqsearch(nbrs, target): #nbrs는 전체 숫자 리스트. target은 찾을 숫자들의 리스트.
    for i in range(0, len(nbrs)): #for문을 전체 숫자 갯수만큼 반복함. 숫자가 100개면 100번돌아감.
        if (target == nbrs[i]): #target은 찾으려는 숫자 하나씩 들어옴. 전체 숫자 리스트에서 같은게 있으면 i를 리턴
            return i
    return -1 #없으면 -1을 리턴


def recbinsearch(L, l, u, target):
    global middle
    middle= int((l+u)//2)
    if L[middle] == target:
        return target
    elif L[middle] < target:
        l = middle + 1
    elif L[middle] > target:
        u = middle - 1
    else:
        return -1






numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs): #입력한 숫자 개수만큼의 랜덤 리스트를 생성.
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers) #생성된 리스트를 크기순으로 정렬


numoftargets = int(input("Enter the number of targets: ")) #찾을 숫자의 개수 입력
targets = []
for i in range(numoftargets): #입력한 갯수만큼의 숫자가 들어있는 랜덤리스트 생성
    targets += [random.randint(0, 999999)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets: #찾을 숫자들의 리스트에서 target으로 하나씩 찾음. 타갯의 갯수만큼 for문 반복
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts)) #순서대로 찾을 숫자의 갯수, 못 찾은 숫자의 갯수, 걸린 시간.

ts = time.time()

# sequential search
cnt = 0
for target in targets:#찾을 숫자들의 리스트(targets)에서 target으로 하나씩 찾음.
    idx = seqsearch(numbers, target) #동일한 숫자를 찾으면 idx는 찾아낸 숫자값.
    if idx == -1: #찾지 못하면 idx는 -1
        cnt += 1 #찾지 못할때마다 cnt가 +1됨. 못 찾은 숫자의 개수가 증가함.
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts)) #순서대로 찾을 숫자의 갯수, 못 찾은 숫자의 갯수, 걸린 시간.
