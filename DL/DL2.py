'''
    1. Intelligence(지능)
        1) 학습 능력, 추론 능력, 지각 능력, 언어 이해 능력을 통칭함
        2) 새로운 문제가 발생하면 그에 맞는 지시 제공
        3) 프로그램 : 문제를 해결할 때 따라야 하는 일들을 지시하는 것
        4) 컴퓨터가 스스로 방법을 찾아냄 : 데이터를 기반으로 스스로 학습할수 있음
            - 알파고 : 컴퓨터에 바둑 경기의 규칙과 이전 경기의 많은 데이터를 알려줌.
                    ==> 컴퓨터가 스스로 바둑의 원리를 학습하여 바둑을 둘수 있었던 것임.

        5)                          파라미터 수정                     평가
                                        ||                          /||\
                                       \||/                          ||
                    입력      ==> Model(동작을 결정하는 파라미터)    ==> 출력
                                융통성 있는 프로그램

            파라미터가 바뀌면 동작도 바뀌는 것임.
            좋은 동작이 나오도록 파라미터를 변경하는 일을 하는데, 이 과정을 학습이라고 부름.

    2. Artificial Intelligence(인공 지능)
        1) 인간의 학습 능력과 추론, 지각 능력을 인공적으로 구현한 것.
            - 인간처럼 사고하기, 인간처럼 행동하기, 합리적으로 사고하기, 합리적으로 행동하기
        2) 머신 러닝 (Machine learning)은 매우 구체적이고 엄밀한 정의를 가지고 있음.
            - 반복적인 학습을 통해 분류 성능을 점점 향상시킬 수 있는 효율적인 알고리즘이 기계학습을 수행함
        3) 요약
            - 학습(learning)
            - 빅데이터 (Big Data)
            - 추론(Reasoning)
            - 문제 해결(Problem Solving)
        4)
                                작업 T    (작업의 성능을 측정)
                (경험을 이용하여 작업 수행)
                    경험 E        성능개선        성능척도 P
            - 머신러닝을 공학적으로 세가지 중요한 요소가 필요함
                - 해결해야 할 문제(작업) T
                - P라는 성능 척도를 통해 평가할수 있어야 함
                - 지속적인 훈련 경험 E

            - 인공 신경망을 이용한 딥러닝 (Deep Learning) 분야 역시 이 머신러닝의 한 분야로 볼수 있음

    3. 머신러닝 종류
        1) 지도학습 (supervised learning)
            - 데이터와 정답의 역할을 하는 레이블(Label)을 제공받음
            - 입력을 출력에 매핑하는 일반적인 규칙을 학습하는 것임.
            - 예) 고양이, 개를 구분할 때 고양이인지 개인지 레이블링 된 데이터를 충분히 제공한 뒤에
                  학습을 하도록하는 과정이 필요.
                  - 학습단계 => 예측모델 => 테스트 단계
        2) 비지도학습(unsupervised Learning)
            - 정답(레이블)을 주지 않고 학습 알고리즘이 스스로 어떤 구조를 발견하는 학습
            - 군집합(clustering) : 주어진 데이터를 특성에 따라 둘 이상의 그룹으로 나누는 것
        3) 강화학습 (reinforcement Learning)
            - 학습 데이터를 줌
                - 에이전트(게임), 환경, 액션, 보상과 상태

    4. 회귀 분석
        1) 회귀 (Regression)
            - 어딘가로 돌아간다는 의미
        2) 회귀분석
            - 대표적인 지도학습 알고리즘
            - 데이터(독립변수)를 통해 종속변수 사이의 숨어 있는 관계를 추정하는 것
                - 독립변수 : 다른 변수에 영향을 받지 않는 변수
                - 종속변수 : 독립변수에 영향을 받아서 변화하는 변수
            - 주택의 면적이 큰 경우 판매가격도 높은 경우가 많음.
                - 독립변수 : 주택의 면적 (x좌표), 일조량, 접근성
                - 종속변수 : 거래 가격 (y좌표)
                - 관측된 데이터를 바탕으로 다차원 공간에 존재하는 데이터들을 가장 잘 설명하는 수학 함수를 찾는 것
                    - y = f(x)
                        - 입력 x, 출력 y 를 보면서 함수 f(x)를 예측하는 것을 회귀 기법이라고 할 수 있음.
                        - 이 상관관계를 가장 잘 설명하는 직선을 찾는 문제가 될수 있음

                - 이 둘 사이 상관관계가 1차 방정식으로 표현 될수 있는 선형관계라고 함
                    - 주택 면적 x와 거래 가격 y의 관계는 y = wx + b 로 표현됨
                    - 기울기 w와 절편 b를 어떻게 정의하는가에 따라 표현 할 수 있음.
                        - f1(x), f2(x)를 가설 혹은 모델이라고 부름
                        - 오차 (error)가 가장 작은 가설이 좋은 가설임
'''