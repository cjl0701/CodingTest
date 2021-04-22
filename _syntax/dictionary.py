# key-value 쌍.
# Hash table을 이용하므로 O(1)
# key: immutable한 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
print(data)  # {'사과': 'Apple', '바나나': 'Banana'}
if '사과' in data:
    print(data['사과'])  # Apple

# {key1:value1, key2:value2} 형태 초기화
data2 = {'사과': 'Apple', '바나나': 'Banana'}
key_list = data2.keys()
print(key_list)  # dict_keys(['사과', '바나나'])
# dict_key 객체로 반환하므로 실제 리스트는 아님
# key_list.append('impossible') AttributeError: 'dict_keys' object has no attribute 'append'
# 따라서 리스트로 형변환 해줘야 함
value_list = list(data2.values())
value_list.append('new')
print(value_list)  # dict_values(['Apple', 'Banana', 'new])

for key in key_list:
    print(data2[key])

# 정수도 key가 된다
student_info = {15010681: "최재량", 1501234: "이성수"}
print(student_info.items())  # dict_items([(15010681, '최재량'), (1501234, '이성수')])
for k, v in student_info.items():
    print(k, v)  # 15010681 최재량 1501234 이성수
