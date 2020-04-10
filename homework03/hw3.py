"""
Adapted from the numpy notebook code from kvlinden/cs344-code
Student: Jason Klaassen for CS344 at Calvin University
3/14/20

hw3.py prints out the training and testing data from the keras boston_housing dataset

"""
from tensorflow.keras.datasets import boston_housing
import pandas as pd
import numpy as np

(trainingSet, trainingLabels), (testingSet, testingLabels) = boston_housing.load_data()
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


# Exercise 3a Part
print_structures()

# Exercise 3b Part
# Create Training DataFrame from boston housing data
trainingDataFrame = pd.DataFrame(trainingSet)
trainingDataFrame["target"] = trainingLabels

# Exercise 3c Part
# Create Synthetic Feature to see how the percentage of Blacks per town varies with the ratio of pupil to teacher
trainingDataFrame["Black Learning Access"] = trainingDataFrame[10] * trainingDataFrame[11]

# Create Testing DataFrame from boston housing data
testingDataFrame = pd.DataFrame(testingSet)
testingDataFrame["target"] = testingLabels

# Shuffle the Training Data - Must be before Picking Validation Step
trainingDataFrame = trainingDataFrame.reindex(np.random.permutation(trainingDataFrame.index))

# Calculate divisions
numRows = len(trainingDataFrame)
validationRows = Math.floor(numRows * .2)
trainingRows = Math.ceil(numRows * .8)

# Seperate Validation Set from Training Set with a split of 80% Training and 20% Validation
validationDataFrame = trainingDataFrame.head(validationRows)
trainingDataFrame = trainingDataFrame.tail(trainingRows)


