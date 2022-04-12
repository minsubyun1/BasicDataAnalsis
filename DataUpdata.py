import pandas as pd
import numpy as np

df = pd.DataFrame(columns = ['이름', '나이', '주소']) # 데이터프레임 생성
df.loc[0] = ['길동', '26', '서울'] #리스트로 데이터 추가
df.loc[1] = {'이름': '철수', '나이':'25', '주소':'인천'} # 딕셔너리로 데이터 추가
df.loc[1, '이름'] = '영희' # 명시적 인덱스 활용하여 데이터 수정

# NaN값으로 초기화 한 새로운 컬럼 추가
df['전화번호'] = np.nan # 새로운 컬럼 추가 후 초기화
df.loc[0, '전화번호'] = '01012341234'
print(df)

# DataFrame에서 컬럼 삭제 후 원본 변경
df.drop('전화번호', axis = 1, inplace=True) #컬럼 삭제
# axis = 1 : 열 방향 / axis = 0: 행 방향
# inplace = True : 원본 변경 / inplace = False : 원본 변경 x
print(df)