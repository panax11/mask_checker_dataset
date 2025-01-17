Mask checker dataset
====================
![license badge](https://img.shields.io/github/license/Onegold11/mask_checker_dataset)

Intro
-----
2020년 제14회 공개SW 개발자 대회를 위해 제작되었습니다.

개발 기간: 2020.07.16 ~ 2020.09.03

[MaskChecker][MaskChecker_Android] 앱에 사용할 데이터셋과 모델를 위한 저장소입니다.

[MaskChecker_Android]: https://github.com/Onegold11/MaskChecker_Android

Architecture
------------
<img src="./readme_image/00.png" width="600" height="200">

<img src="./readme_image/01.png" width="600" height="200">

이미지 데이터를 numpy를 사용해 전처리 후 데이터 셋으로 변환합니다.
데이터 셋을 사용해 MobileNetV2을 생성하고 모델을 저장합니다.
저장된 모델을 Tensorflow Lite의 tflite 모델 파일로 변환하여 안드로이드 기기에 탑재하여 사용합니다.


Performance
-----------
<img src="./readme_image/02.png" width="400" height="400">
Accuracy : About 99.3%

Data Source
-----------
+ https://www.kaggle.com/wobotintelligence/face-mask-detection-dataset/data?select=train.csv
+ https://www.kaggle.com/atulanandjha/lfwpeople?select=lfw-funneled.tgz
+ https://public.roboflow.ai/object-detection/mask-wearing
+ https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/

Using Models
------------
+ MobileNetV2

Required Version
-----------
+ Python 3.7
+ Tensorflow 2.2.0: https://github.com/tensorflow/tensorflow
+ Keras 2.4.3: https://github.com/keras-team/keras
+ scikit-learn 0.23.2: https://github.com/scikit-learn/scikit-learn
+ numpy 1.19.0: https://github.com/numpy/numpy
+ dlib: https://github.com/davisking/dlib
+ opencv-python 4.3.0.36: https://github.com/skvark/opencv-python

Contents
--------
+ image
  - 전처리 전 이미지 모음
  - mask : 마스크 이미지 모음
  - no_mask : 얼굴 이미지 모음
  - validation : 검증용 이미지 모음
+ source
  - 소스 코드 모음
  - dataset : 이미지 데이터셋
  - learning : 모델 학습 소스 코드 모음
    - models : 학습이 완료된 모델
  - preprocessing : 전처리 소스 코드 모음

Manual
------
+ 사용 순서
  + mask_image_set -> MobileNet -> TFLite_convert


+ 주의 사항
  + 미리 만들어진 모델 및 데이터 셋은 압축되어 있으므로 해제하고 사용해야 함
  + 소스 코드 상단에 저장 및 불러오는 데이터에 대한 경로를 설정할 수 있음


+ mask_image_set.py
  + 이미지를 이미지 데이터셋으로 변한
+ MobileNet.py
  + 이미지 데이터셋을 사용해 MobileNetV2 모델을 생성
+ TFLite_convert.py
  + MobileNetV2 모델을 tflite 모델 파일로 변환

Q&A
---
Onegold11 : ujini1129@gmail.com

yang20202 : yang202@ajou.ac.kr
