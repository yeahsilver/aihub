# 선형대수학

#### Scalar

: 길이, 넓이, 질량, 온도 등 크기만 존재하는 양

#### Vector

: 속도, 위치 이동 힘 등 크기와 방향이 모두 존재하는 양



## 벡터

<img width="699" alt="스크린샷 2020-06-28 오후 3 44 23" src="https://user-images.githubusercontent.com/39258902/85940239-3eca6900-b956-11ea-9d30-8da75c6c4b77.png">




## 벡터 공간 / 내적

#### Norm

<img width="599" alt="스크린샷 2020-06-28 오후 3 46 53" src="https://user-images.githubusercontent.com/39258902/85940328-98329800-b956-11ea-9d94-7e7e92cf0b8c.png">



#### 내적 (= Euclidean inner product / Dot product)

<img width="619" alt="스크린샷 2020-06-28 오후 3 51 45" src="https://user-images.githubusercontent.com/39258902/85940425-48080580-b957-11ea-8d73-e3c0ac994619.png">

- 같은 차원끼리 곱함.
- 주의) 다른 차원에서는 곱셈을 할 수 없음. 



## 행렬

: 실수를 직사각형 모양으로 배열한 것

<img width="510" alt="스크린샷 2020-06-28 오후 3 53 16" src="https://user-images.githubusercontent.com/39258902/85940451-7d145800-b957-11ea-9487-0327a0493ad7.png">



#### Matrix Arithmetic

- 같은 차원을 가지고 있는 행렬끼리만 더하거나 뺄 수 있다. 

<img width="533" alt="스크린샷 2020-06-28 오후 3 54 35" src="https://user-images.githubusercontent.com/39258902/85940494-acc36000-b957-11ea-9aff-d678eb598d40.png">




- 행렬끼리 곱할 때는 차원을 주의해야 한다.


<img width="537" alt="스크린샷 2020-06-28 오후 3 56 25" src="https://user-images.githubusercontent.com/39258902/85940539-ee540b00-b957-11ea-9ade-8509d722fa18.png">

## Transpose( = 전치행렬)

: 전치행렬은 원행렬의 행과 열을 뒤바꾼 행렬이다.

<img width="321" alt="스크린샷 2020-06-28 오후 3 59 42" src="https://user-images.githubusercontent.com/39258902/85940615-63bfdb80-b958-11ea-8e31-416aad5c290b.png">




## Numpy 소개

- python에서 사용되는 과학컴퓨팅용 라이브러리

  - python 언어에서 기본으로 지원하지 않는 행렬과 같은 데이터 구조 지원 및 수학 / 과학 계산 함수 포함.

    

#### 행렬이 왜 필요한가?

: 머신러닝에서 대부분의 데이터는 행렬로 표현됨.



####  Numpy Array

```python
# 1 2
# 3 4
# 행렬 만들기
import numpy as np

A = np.array([1,2], [3,4])

print(A)

# 사칙연산
print(A * 3)
print(A + A)
print (A - A)

# 행렬 곱셈
x = np.array([1,2], [3,4])
y = np.array([3,4], [3,2])

print(np.dot(x,y)) # 행렬 곱셈
print(x * y) # 같은 위치에 있는 숫자 곱셈

# 비교 연산
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print(a == b) # [False, True, False, True]
print(a > b) # [False, False, True, False]

# 논리 연산
a = np.array([1,1,0,0], dtype=bool) #dtype: data type
b = np.array([1,0,1,0], dtype=bool)

np.logical_or(a, b) # [True, True, True, False]
np.logical_and(a, b) # [True, False, False, False]

# Reductions
a = np.array([1,2,3,4,5])

np.sum(a) # 15
a.sum() # 15

a.min() # 1
a.max() # 5

a.argmin() # 0
a.argmax() # 4 argmin/max: 최소/최대값의 index를 반환

# Logical Reductions
a = np.array([True, True, True])
b = np.array([True, True, False])

np.all(a) # True
np.all(b) # False

np.any(a) # True
np.any(b) # True

# Statistical Reductions
x = np.array([1,2,3,1])

np.mean(x) # 평균값: 1.75 
np.median(x) # 중간값: 1.5 
np.std(x) # 표준편차: 0.82915619758884995
```



# 회귀 분석

## 단순선형회귀분석

예시) 키가 175인 신입생 A가 들어왔다. 이때 예상 몸무게는 몇인가?

<img width="498" alt="스크린샷 2020-06-29 오전 11 06 26" src="https://user-images.githubusercontent.com/39258902/85965735-95887f00-b9f8-11ea-9925-841e8217a345.png">

### 회귀 분석법

<img width="281" alt="스크린샷 2020-06-29 오전 11 08 15" src="https://user-images.githubusercontent.com/39258902/85965798-d5e7fd00-b9f8-11ea-8e03-8b9f68870fd8.png">


- 데이터: 광고 분석과 판매량
- 목표: 광고에 얼마를 투자하면 상품이 얼마나 팔릴까?
- 방법: 데이터를 가장 살 명하는 어떤 선을 하나 찾는다. 



### 변수 표기

<img width="650" alt="스크린샷 2020-06-29 오전 11 09 29" src="https://user-images.githubusercontent.com/39258902/85965841-02037e00-b9f9-11ea-9571-b71ef54aa819.png">



###문제정의

<img width="631" alt="스크린샷 2020-06-29 오전 11 19 05" src="https://user-images.githubusercontent.com/39258902/85966313-59561e00-b9fa-11ea-97be-1fa247855890.png">



###모델의 학습 목표

<img width="650" alt="스크린샷 2020-06-29 오후 1 27 02" src="https://user-images.githubusercontent.com/39258902/85972938-39c7f100-ba0c-11ea-8304-c3d8e716d770.png">

- 어떤 추세선이 좋은 것인지를 예측해야함. -> 트레이닝 중요!



<img width="639" alt="스크린샷 2020-06-29 오후 1 29 26" src="https://user-images.githubusercontent.com/39258902/85973031-90cdc600-ba0c-11ea-968d-5c9617404d8c.png">

- 실제값(x, y)과 추세선 사이의 거리를 최소화하는 것이 목표!

<img width="642" alt="스크린샷 2020-06-29 오후 1 31 38" src="https://user-images.githubusercontent.com/39258902/85973167-dee2c980-ba0c-11ea-8d04-15bd7be75a4e.png">

- 차이: 실제값 - 예측 값

- 전체 모델의 차이: <img width="273" alt="스크린샷 2020-06-29 오후 1 32 54" src="https://user-images.githubusercontent.com/39258902/85973220-0c2f7780-ba0d-11ea-82e7-9fe816c56509.png">

 --> 이렇게 하면 안됨!



### 반례

<img width="639" alt="스크린샷 2020-06-29 오후 1 34 08" src="https://user-images.githubusercontent.com/39258902/85973290-3719cb80-ba0d-11ea-9ad8-fda6b84eff4b.png">



### 해결

<img width="590" alt="스크린샷 2020-06-29 오후 1 35 36" src="https://user-images.githubusercontent.com/39258902/85973337-6c261e00-ba0d-11ea-8445-6690f06f6f23.png">



### 문제 재정의

<img width="636" alt="스크린샷 2020-06-29 오후 1 36 13" src="https://user-images.githubusercontent.com/39258902/85973375-83650b80-ba0d-11ea-8b6b-5490a26a7f93.png">



### 산 정상 오르기

- 산 정상이 되는 지점을 찾고 싶다. 아무 곳에서나 시작했을 때, 가장 정상을 빠르게 찾아가는 방법은?
- 가정
  - 정상의 위치는 알 수 없다.
  - 현재 나의 위치와 높이를 알 수 있다.
  - 내 위치에서 일정 수준 이동할 수 있다. 

--> 가장 좋은 방법: 경사가 가장 높은 곳으로 가는 것. 



### 거꾸로 된 산을 내려가기

<img width="633" alt="스크린샷 2020-06-29 오후 2 20 53" src="https://user-images.githubusercontent.com/39258902/85975716-c0cc9780-ba13-11ea-91b2-cc50d1ac96da.png">

<img width="492" alt="스크린샷 2020-06-29 오후 2 22 01" src="https://user-images.githubusercontent.com/39258902/85975775-e9549180-ba13-11ea-8f34-3ace1611fbcf.png">



## 다중 선형 회귀 분석

<img width="606" alt="스크린샷 2020-06-29 오후 2 44 32" src="https://user-images.githubusercontent.com/39258902/85977185-0ccd0b80-ba17-11ea-8453-87f2d0d6a985.png">

### 다중 회귀 분석

<img width="592" alt="스크린샷 2020-06-29 오후 2 46 31" src="https://user-images.githubusercontent.com/39258902/85977292-53bb0100-ba17-11ea-98a3-ec22fb1fbe11.png">
<img width="631" alt="스크린샷 2020-06-29 오후 2 47 06" src="https://user-images.githubusercontent.com/39258902/85977352-69302b00-ba17-11ea-9c22-899156704ae2.png">


- x: vector
- y: scalar



### 문제 정의

-  데이터: N개의 FB, TV, 신문 광과 예산과 판매량

- 목표: FB, TV, 신문에 각각 얼마씩을 투자했을 때 얼마나 팔릴까?

- 가설: 학습 알고리즘이 주어진 데이터를 학습.

- 가정: 판매량은 FB, TV, 신문 광고료와 선형적인 관계를 가지고 있다

  <img width="333" alt="스크린샷 2020-06-29 오후 2 50 32" src="https://user-images.githubusercontent.com/39258902/85977601-e3f94600-ba17-11ea-9ccd-4f3d62296e23.png">




#### 모델의 학습 목표

- 단순선형회귀분석과 동일
- 완벽한 예측은 불가능함.
- 각 데이터의 실제값과 모델이 예측하는 값을 최소한으로 하자!



#### 수학적으로 다시 쓰기

<img width="607" alt="스크린샷 2020-06-29 오후 2 52 39" src="https://user-images.githubusercontent.com/39258902/85977763-2fabef80-ba18-11ea-81c7-0b56e04e554f.png">



## 다항식회귀분석

#### 더 좋은 방법

- 단순한 선형 회귀 법은 데이터를 잘 설명하지 못한다.

- 조금 더 데이터에 맞게 모델을 학습시킬 수 없을까?

  <img width="433" alt="스크린샷 2020-06-29 오후 3 10 30" src="https://user-images.githubusercontent.com/39258902/85978987-af3abe00-ba1a-11ea-9b34-5f4e4f3a7d4e.png">

<img width="613" alt="스크린샷 2020-06-29 오후 3 11 43" src="https://user-images.githubusercontent.com/39258902/85979088-db563f00-ba1a-11ea-8efc-4f7689cd8f57.png">

<img width="630" alt="스크린샷 2020-06-29 오후 3 12 46" src="https://user-images.githubusercontent.com/39258902/85979209-ff198500-ba1a-11ea-9a8b-084fb8f653c2.png">



# 나이브 베이즈 분류

 ### 조건부 확률

: 사건 B가 일어났을 때 A가 일어날 확률

<img width="310" alt="스크린샷 2020-06-29 오후 8 49 49" src="https://user-images.githubusercontent.com/39258902/86001601-158b0500-ba4a-11ea-9d93-43a29f15a5dd.png">




#### 확률로 파이 구하기

##### Monte Carlo Method

- 임의의 점을 찍으면서 모양과 넓이를 구함.

