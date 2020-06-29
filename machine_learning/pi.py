import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import elice_utils

def main():
    plt.figure(figsize=(5,5)) # figure 크기 조정.
    
    X = [] # 1000개의 점을 저장
    Y = [] # 1000개의 점을 저장
    
    # N을 10배씩 증가할 때 파이 값이 어떻게 변경되는지 확인해보세요.
    N = 1000
    
    for i in range(N): # 1000개의 점 생성
        X.append(np.random.rand())  # 점을 랜덤으로 찍음
        Y.append(np.random.rand()) # 점을 랜덤으로 찍음
    X = np.array(X)
    Y = np.array(Y)
    
    X = X * 2 - 1 # [0, 1] --> [0,2] --> [-1, 1] (X가 -1부터 1까지의 값에 고르게 퍼짐.)
    Y = Y * 2 - 1# [0, 1] --> [0,2] --> [-1, 1] (Y가 -1부터 1까지의 값에 고르게 퍼짐.)
    
    dist = np.sqrt(X ** 2 + Y ** 2) # norm을 구함
    is_inside_circle = dist <= 1 # 원이 영역 밖에 있는지 안에있는지를 알려줌. 
    
    # distance_from_zero = np.sqrt(X * X + Y * Y) # 원점과 랜덤의 점 사이의 거리를 구함. 
    # is_inside_circle = distance_from_zero <= 1 
    
    print("Estimated pi = %f" % (np.average(is_inside_circle) * 4))
    
    plt.scatter(X, Y, c=is_inside_circle)
    plt.savefig('circle.png')
    elice_utils.send_image('circle.png')

if __name__ == "__main__":
    main()
