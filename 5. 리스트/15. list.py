'''
    * 리스트 자료형
        - 리스트명 = [데이터,데이터,데이터,...]

'''
# 데이터가 없는 리스트
empty = []

# 데이터가 있는 리스트
earPods = ["액티브 노이즈 캔슬링", "적용형 주변음 허용 모드", "터치 제어", "개인 맞춤형 공간 음향"]

print(earPods[2])
print(earPods[-1])

earPods.append("강한 생활 방수 디자인")
print(earPods[-1])

earPods[1] = "기기 간 자동 전환"
print(earPods)

del earPods[0]
print(earPods)

print(earPods[1:-1])
print(earPods[:])
print(earPods[:3])
print(earPods[1:])

print(len(earPods))
earPods.sort()
print(earPods)
