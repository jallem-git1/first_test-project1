from random import choice

color = ['땡땡이', '베이지', '블랙', '블루', '회색', '청색', '레드', '파란', '핑크', 
         '그레이', '베이지', '화이트', '청', '초록', '회색', '노랑', '인디안 핑크', 
         '차콜', '브라운', '검은', '분홍']
food = ['소라과자', '아이스 바닐라 라떼', '소보로', '쭈꾸미', '요거트 아이스크림', '오란다',
         '와플', '아이스티', '로제 떡볶이', '스트로베리', '커피', '진라면', '초코퍼지', '닭갈비', 
         '크래커', '맥스봉', '라떼', '참외', '소시지', '햄버거', '콰삭칩', '된찌', '오렌지', '옹심이', 
         '아메리카노']

print(choice(color) + ' ' + choice(food))