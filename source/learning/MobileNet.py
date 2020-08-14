from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.applications.mobilenet_v2 import MobileNetV2
import matplotlib.pyplot as plt
import numpy as np

# 데이터 셋 경로
DATASET_PATH = './dataset/images_v3.npy'
# 모델 파일 저장 경로
MODEL_PATH = './models/MobileNet/'


def get_data_set():
    X_train, X_test, y_train, y_test = np.load(DATASET_PATH, allow_pickle=True)

    # 데이터 정규화(0~1)
    X_train = X_train.astype("float") / 256
    X_test = X_test.astype("float") / 256
    print('X_train shape:', X_train.shape)
    print('Y_train shape:', y_train.shape)
    print('X_test shape:', X_test.shape)
    print('Y_test shape:', y_test.shape)
    return X_train, X_test, y_train, y_test


def create_model(X_train, X_test, Y_train, Y_test):
    # MobileNet 모델 생성
    transfer_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(64, 64, 3))
    transfer_model.trainable = False

    # 모델 생성
    model = Sequential()

    # MobileNet 모델 연결
    model.add(transfer_model)

    # 완전 연결 계층
    # fc1
    model.add(Flatten())
    # fc2
    model.add(Dense(5012, activation='relu'))
    # fc3
    model.add(Dense(2, activation='softmax'))

    model.summary()
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # 모델 중간 세이브
    model_path = MODEL_PATH + '{epoch:02d}-{val_loss:.4f}.hdf5'
    check_pointer = ModelCheckpoint(filepath=model_path, monitor='val_loss', verbose=1, save_best_only=True)

    # 조기 멈춤
    early_stopping_callback = EarlyStopping(monitor='val_loss', patience=5, mode='auto')

    # 학습
    history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=100, batch_size=100, verbose=0,
                        callbacks=[early_stopping_callback, check_pointer])

    # 학습 과정 손실 값 그래프
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    y_vloss = history.history['val_loss']
    y_loss = history.history['loss']

    print("acc_train")
    print(acc)
    print("acc_test")
    print(val_acc)

    x_len = np.arange(len(y_loss))
    plt.plot(x_len, acc, marker='.', c='red', label='Trainset_acc')
    plt.plot(x_len, val_acc, marker='.', c='lightcoral', label='Testset_acc')
    plt.plot(x_len, y_vloss, marker='.', c='cornflowerblue', label='Testset_loss')
    plt.plot(x_len, y_loss, marker='.', c='blue', label='Trainset_loss')

    plt.legend(loc='upper right')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.show()


#  from keras.models import load_model
#   model.save('mask_detection_v3.h5')

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = get_data_set()
    create_model(X_train, X_test, y_train, y_test)
