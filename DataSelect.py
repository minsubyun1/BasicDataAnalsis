import pandas as pd

data = {
    'country' : ['china', 'japan', 'korea', 'usa'],
    'gdp': [1409250000, 516700000, 169320000, 2041280000],
    'population': [141500, 12718, 5180, 32676]
}

country = pd.DataFrame(data)
country = country.set_index('country')
# .loc 함수는 명시적인 인덱스를 참조하는 인덱싱/슬라이싱이다.

print(country.loc['china']) # 인덱싱
print(country.loc['japan':'korea', :'population']) # 슬라이싱 

# .iloc 함수는 파이썬 스타일의 정수 인덱스 인덱싱/슬라이싱 기법이다.

print(country.iloc[0]) #인덱싱 0번째 row
print(country.iloc[1:3, :2]) #슬라이싱 1번째 column~ 3-1번째 row, 2-1번째 column 

# 컬럼명 활용하여 DataFrame에서 데이터 선택 가능
print(country['gdp']) # Series(인덱스와 데이터로 이루어진) 자체를 출력
print(country[['gdp']]) # DataFrame 형식으로 인덱싱

# Masking 연산이나 query 함수를 활용하여 조건에 맞는 DataFrame 행 추출 가능
print(country[country['population'] < 10000]) # masking 연산 활용
print(country.query("population > 100000")) # query 함수 활용

#Series도 numpy array처럼 연산자 활용 가능
gdp_per_capita = country['gdp'] / country['population']
country['gdp per capita'] = gdp_per_capita
print(country[['gdp per capita']] )

