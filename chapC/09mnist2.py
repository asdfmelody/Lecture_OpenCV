import cv2, numpy as np
import  gzip
import matplotlib.pyplot as plt

IMAGE_SIZE = 28
PIXEL_DEPTH = 255
NUM_LABELS = 10


# 1
def extract_data(filename, num_images):
    # Extract the images into a 4D tensor [image index, y, x, channels].
    #   Values are rescaled from [0, 255] down to [0, 1].

    with gzip.open(filename) as bytestream:
        bytestream.read(16)
        buf = bytestream.read(IMAGE_SIZE * IMAGE_SIZE * num_images)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        ##    data = data/PIXEL_DEPTH
        data = data.reshape(num_images, IMAGE_SIZE, IMAGE_SIZE)
        return data


def extract_labels(filename, num_images):
    # Extract the labels into a vector of int64 label IDs.'''
    with gzip.open(filename) as bytestream:
        bytestream.read(8)
        buf = bytestream.read(1 * num_images)
        labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int32)
    return labels


# Extract it into np arrays.
def load_MINIST():
    x_train = extract_data('./mnist/train-images-idx3-ubyte.gz', 60000)
    y_train = extract_labels('./mnist/train-labels-idx1-ubyte.gz', 60000)
    x_test = extract_data('./mnist/t10k-images-idx3-ubyte.gz', 10000)
    y_test = extract_labels('./mnist/t10k-labels-idx1-ubyte.gz', 10000)

    x_train = x_train.reshape(-1, IMAGE_SIZE * IMAGE_SIZE)  # (60000, 784)
    x_test = x_test.reshape(-1, IMAGE_SIZE * IMAGE_SIZE)  # (10000, 784)

    return (x_train, y_train), (x_test, y_test)


def graph_image(data, lable, title, nsample):
    plt.figure(num=title, figsize=(6, 9))
    rand_idx = np.random.choice(range(data.shape[0]), nsample)
    for i, id in enumerate(rand_idx):
        img = data[id].astype(np.uint8)
        img = img.reshape(28, 28)
        plt.subplot(6, 4, i + 1), plt.axis('off'), plt.imshow(img, cmap='gray')
        plt.title('%s: %d' % (title , lable[id]))
    plt.tight_layout()


(train_data, train_label), (test_data, test_label ) = load_MINIST()
## MNIST 로드 데이터 크기 확인
print('train_set=', train_data.shape)
print('test_set', test_data.shape)

knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_label)


def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(dst, (x, y), 10, (255, 255, 255), -1)
    cv2.imshow('dst', dst)


dst = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
cv2.imshow('dst', dst)
cv2.setMouseCallback('dst', onMouse)


cv2.destroyAllWindows()

