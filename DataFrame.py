import pandas as pd

# DataFrame은 여러 개의 Series가 모여서 행과 열을 이룬 데이터이다.
# Dictionary를 활용하여 DataFrame 생성 가능
data = {
    'country' : ['china', 'japan', 'korea', 'usa'],
    'gdp': [1409250000, 516700000, 169320000, 2041280000],
    'population': [141500, 12718, 5180, 32676]
}

country = pd.DataFrame(data)
country = country.set_index('country')
print(country.shape) # 4개의 행과 2개의 열
print(country.size) # country를 인덱스로 지정해서, 8개의 데이터
print(country.ndim) # country를 인덱스로 지정해서 데이터는 2차원
print(country.values) 

# DataFrame의 index와 column에 이름 지정
country.index.name = "Country" # 인덱스에 이름 지정 
country.columns.name = "Info" # 컬럼에 이름 지정

print(country.index)

print(country.columns)

# 데이터 프레임 저장 및 불러오기도 가능
# country.to_csv("./country.csv")
# country.to_excel("country.xlsx")
# country = pd.read_csv("./country.csv")
# country = pd.read_excel("country.xlsx")


