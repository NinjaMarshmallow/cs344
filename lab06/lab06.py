"""
Adapted from the numpy notebook code from kvlinden/cs344-code
Student: Jason Klaassen for CS344 at Calvin University
3/14/20

lab06.py prints out the training and testing data from the keras boston_housing dataset

"""
from tensorflow.keras.datasets import boston_housing


def print_structures():
    print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
                len(train_images),
                train_images.ndim,
                train_images.shape,
                train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \n'.format(
                len(test_labels),
                train_labels.ndim,
                test_labels.shape,
                test_labels.dtype
        )
    )


(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()
print_structures()