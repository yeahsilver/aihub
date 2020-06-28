## 선형대수학

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

