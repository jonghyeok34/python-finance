

## 4. 

1. install matplot.finance
```
pip install mpl_finance

```

## 5.
```
pip install bs4
```

## 10. 

## 12.
1. 표본내 성능 검증(in-sample testing)  
학습용 데이터 집합(traning data set)이라고 한다. 이 학습 데이터 집합의 종속 변수값을 얼마나 잘 예측하였는지를 나타내는 성능 

2. 검증용 데이터 집합  
교차검증을 하려면 두 종류의 데이터 집합이 필요하다.
```
	- 학습을 위한 데이터 집합 (training data set)
	- 성능 검증을 위한 데이터 집합 (test data set)
```
따라서 학습/검증 데이터 분리(train-test split) 방법을 사용한다 
-- 학습용 데이터만을 사용하여 회귀분석 모형을 만들고 검증용 데이터로 성능을 계산함

3. fit 
```
Fitting a classifier means taking a data set as input, then outputting a classifier, which is chosen from a space of possible classifiers.
fitting a knn classifier simply requires storing the training set.
```

4. Voting classifier
```
Voting is one of the simplest way of combining the predictions from multiple machine learning algorithms. 
```