

# 진법 변경

# print(bin(12))
# print(oct(12))
# print(hex(12))


# print (2 / 3)
# print (5 / 3)



# a = 3.2 - 3.1
# b = 1.2 - 1.1

# import math
# print(math.isclose(a , b))


# f-string

# bugs = 'roaches'
# counts = 13
# area = 'room'
# print(f'Debugging roaches 13 room')
# print(f'Debugging {bugs} {counts} {area}')
# print('Debugging %s %d %s' % (bugs, counts, area))

# f-string 응용

# greeting = 'hi'
# print(f'{greeting:^10}')
# print(f'{greeting:>10}')
# print(f'{3.141592:.4f}')



# 문자열 뒤집기

# my_str = 'goodgreat'

# print(my_str[::-1])


# 불변과 가변

# my_str = 'hello'
# # my_str[0] = 'z'

# my_list = [1,2,3]
# my_list[0] = 100
# print(my_list) # [100, 2, 3]




# # 가변형과 불변형의 차이

# list_1 = [1, 2, 3]
# list_2 = list_1

# list_1[0] = 100
# print(list_1) # [100,2,3]
# print(list_2) # [100,2,3]


# x = 10
# y = x

# x = 20
# print(x) # 20
# print(y) # 10



# 2213

# book = '1'
# total = 10
# guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
# print(guide)
# print(int(book) * total)

# changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
# rental = 3.0
# print(changes)
# print(total - int(rental))



# 2214

# authors = ['작자 미상', '이항복', '임제', '임제', 
#            '조성기', '조성기', '조성기', '임제', 
#            '허균', '허균', '허균', '임제', '임제', 
#            '임제', '임제', '임제', '임제', '임제', 
#            '임제', '임제', '임제', '박지원', '이항복', 
#            '남영로', '남영로', '남영로', '이항복', '임제', '임제']

# list_authors = list(set(authors))

# print(list_authors)



# 1673

# print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n- 1연\n\t가야할 때 언제인가를\n\t분명히 알고 가는 이의\n\t뒷모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.')



# 1674

# author_1 = '권필'
# author_2 = '허균'
# book_1 = '주생전'
# book_2 = '홍길동전'

# print(f'{book_1}의 작가는 {author_1}이고,')
# print(f'{author_2}은 {book_2}를 집필하였다.')



# 1675

# books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
# authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

# print(authors[1],':', books[3])
# print(authors[3],':', books[1])
# print(authors[0],':', books[2])
# print(authors[2],':', books[0])
# print(authors[4],':', books[4])



# 1676

# information = dict()
# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# inf1 = information[authors[0]] = books[1]
# inf2 = information[authors[1]] = books[3]
# inf3 = information[authors[2]] = books[4]
# inf4 = information[authors[3]] = books[0]
# inf5 = information[authors[4]] = books[2]


# print(authors[0], ':', inf1)
# print(authors[1], ':', inf2)
# print(authors[2], ':', inf3)
# print(authors[3], ':', inf4)
# print(authors[4], ':', inf5)



# 1677

# catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
#     ['성공의 열쇠', '내면의 변화', '목표의 달성']
# ]

# backup_catalog = str(catalog)

# catalog[3][0] = '성공을 향한 한 걸음'
# catalog[3][1] = '내 삶의 변화'
# catalog[3][2] = '목표 달성의 비밀'

# print('catalog와 backup_catalog를 비교한 결과')
# print(bool(catalog==backup_catalog))
# print('backup_catalog : ')
# print(backup_catalog)
# print()
# print('catalog : ')
# print(catalog)