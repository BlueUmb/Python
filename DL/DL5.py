'''
    1. 퍼셉트론 (perceptron)
        1) 단층 퍼셉트론
            - 가장 단순한 인공신경망 모형
            - 입력 노드와 출력 노드로만 구성
            - AND 또는 OR 연산 : 2개의 입력 노드와 1개의 출력 노드로 구성되어 학습 가능
                - 학습 : 주어진 데이터로 가중치(w1, w2)와 편향(b)을 찾는 과정
                    - 신경망이 스스로 가중치를 자동으로 설정해 주는 알고리즘이 필요함 (학습 알고리즘)
                    - 가중치 변화(조정)
                        - 목표치와 오차를 줄이기 위함
        2) 다층 퍼셉트론
            - 은닉층이 있는 인공 신경망
            - XOR 연산 : 은닉층이 최소 1개 이상 필요
        3) 딥러닝은 은닉층이 2개 이상인 인공신경망 모형의 학습하는 것임.
        4) 은닉층과 출력층
            - 각 입력값을 처리하는 합성함수와 출력으로 보내기 위한 활성화 함수로 구성


'''
import numpy as np
