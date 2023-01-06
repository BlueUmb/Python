'''
    1. 인공 신경망
        1) artificial neural network
            - 사람 뇌의 기본 단위는 뉴런
            - 인공 신경망은 뉴런 구조에서 영감을 얻어 고안한 것
            - 딥러닝 구조의 핵심

        2) perceptron
            - 뉴런의 원리를 본따 만든 인공 구조
                - 입력값과 가중치를 곱함
                - 곱한 값들의 총합을 구함
                - 총합이 0을 넘으면 1, 넘지 않으면 0을 출력
            - 입력값, 가중치, 활성화 함수로 이루어진 간단한 구조
                - 원하는 출력값을 내보내도록 가중치 조정해가는 작업 ==> 학습, 훈련 (training)
                - 모델을 훈련시켜 최적인 가중치를 구함
            - 단순 퍼셉트론은 선형 분류 문제만 해결한다는 한계가 있음
                - 입력값과 가중치의 선형 결합으로 이루어진 구조
                - 퍼셉트론 하나로는 비선형 분류 문제 해결 안됨
                    => 다중 퍼셉트론(multi-layer perceptron)을 만들면 해결됨

        3) 신경망
            - 입력층, 은닉층(중간층), 출력층 구성

        4) 활성화 함수 (activation function)
            - 입력값을 어떤 값으로 변환해 출력할지 결정하는 함수
            - 입력값과 가중치를 곱한 값들은 활성화 함수를 거쳐 출력값이 됨
            - 시그모이드 함수와 ReLU 함수
                - sigmoid function
                    - 입력값이 커질수록 출력값은 1에 가까워짐
                    - 입력값이 작아질수록 출력값은 0에 가까워짐
                - Rectified Linear Unit function
                    - 입력값이 0보다 크면 입력값을 그대로 유지
                        - max(0, x)
                    - 입력값이 0이하면 0을 출력

        5) 경사 하강법
            - 신경망 훈련의 목표는 최적 파라미터를 찾는 것임
                - 파라미터는 가중치와 편향
            - 최적 파라미터 손실 함수가 최소값일 떄의 파라미터를 뜻함.
                - 매 훈련 단계마다 손실값이 줄어드는 방향으로 파라미터를 갱신하며 최적 파라미터를 찾음

            - 손실 함수 (loss function)
                - 모델 성능이 얼마나 좋은지 나쁜지 측정하는 함수
                - 예측한 값과 실제값의 차이(손실)를 구하는 함수
                    - 당연히 차이는 작을수록 좋음
                    - 손실 함수의 값이 작을수록 좋은 모델이라고 볼 수 있음
                - 평균 제곱 오차(MSE), 교차엔트로피(crossentropy)
                - 손실함수 값이 최소가 되는 가중치와 편향을 구하는 작업(신경망 훈련)

            - 경사 하강법 (gradient descent)
                - 경사를 따라 내려가는 방법
                - 절차 (①②③)
                    -① 현재 위치에서 기울기(경사)를 구함
                    -② 기울기 아래 방향으로 일정 거리를 이동함
                    - 현재 위치의 기울기가 0이 될때까지 ① ~ ②단계를 반복함
                        - 손실 함수가 최소가 될때까지임
                    - 학습률(learning rage)
                        - 기울기 방향으로 얼마만큼 이동할지 결정하는 값
                        - 가중치를 한 번에 얼마나 갱신할지 결정
                        - 다음 가중치
                            - 기존 가중치에서 '학습률과 기울기를 곱한 값'을 뺀 값
                        - 학습률에 따라 훈련 속도가 달라짐
                            - 한 걸음에 얼마만큼 이동할지 결정하는게 학습률임
                                - 학습률이 너무 크면 훈련 속도는 빠르지만, 더 빠른 길로 이어지는 지점을 건너뛰어서
                                  최적 가중치를 찾지 못할 수도 있음.
                                - 학습률이 너무 작으면 훈련 속도가 느려짐
                            - 하이퍼파라미터이기에 우리가 직접 설정해 줘야 함
                                - 보통 0.1 ~ 0.0001 범위의 값을 사용함
                    - mini batch
                        - 데이터를 미니배치 단위로 무작위로 추출해 경사 하강법을 수행
                            - 여러 데이터의 묶음
                            - 데이터를 하나씩 훈련하기보다는 여러 개를 한 묶음으로 처리함(효율적임)
                        - 미니 배치 경사 하강법 (mini batch gradient descent)

        6) 순전파 & 역전파
            - forward propagation 순전파
                - 신경망에서 입력값이 입력층과 은닉층을 거쳐 출력층에 도달하기까지의 계산 과정
                - 각 층을 통과할때마다 입력값에 가중치를 곱해 다음 층으로 출력할 값을 계산
                - 입력값과 가중치를 활용해 출력값을 구하는 과정
            - back propagation 역전파
                - 순전파의 반대 개념
                - 신경망 훈련에서 가장 중요한 내용임
                - 손실값을 통해 기울기를 구해 가중치를 갱신하는 과정

            - 절차
                - 순전파로 구한 타깃 예측값과 실제 타깃값의 차이(손실)를 구함
                - 손실값을 줄이는 방향으로 가중치의 기울기를 구함
                - 기울기를 바탕으로 가중치를 갱신함. 이떄 출력층 => 입력층 방향으로 가중치를 갱신(역전파)
                - 갱신된 가중치를 바탕으로 반복함. 손실값이 줄어듦

            - 순전파와 역전파를 반복하며 최적 가중치를 찾아 신경망 학습이 이뤄짐

    2. 딥러닝 알고리즘 성능 향상
        1) 드롭아웃(dropout)
            - 과대적합을 방지하기 위하여 신경망 훈련 과정에서 무작위로 일부 뉴런을 제외하는 기법
            - 얼마나 많은 뉴런을 드롭아웃할지는 하이퍼파라미터로 설정할수 있음
                - 드롭아웃 비율을 0.2로 설정하면 전체 뉴런의 20%를 제외함
            - 훈련 단계에서만 적용함, 검증이나 예측 단계에서는 적용하지 않음

        2) 옵티마이저(optimizer)
            - 신경망의 최적 가중치를 찾아주는 알고리즘
            - 확률적 경사 하강법
            - 모멘텀, Adam, RMSProp, Adagrad
                - Adam  : 딥러닝 모델을 설계할 때 가장 많이 사용하는 옵티마이저.

'''