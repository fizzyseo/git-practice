slist = []
while True:
    item=input('원하는 물건을 입력하세요:')
    if item == 'quit':
        break
    slist.append(item)   # slist에 항목 추가하기
    slist.sort()        # 오름차순 정렬하기
    for i, value in enumerate(slist,1): # 인덱스 번호와 요소 출력
        print(i,value)  
