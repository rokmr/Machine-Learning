# k-nearest neighbor (KNN)
It is non-parametric learning algorithm. It is mainly used for classification but also can be used for regression by averaging out the nearest value based on distance.

## Process
1. Choose the number of k and a distance metric(Euclidean, Manhattan, Cosine etc.)
2. Find the k-nearest neighbors of the data record that we want to classify
3. Assign the class label by majority vote

The right choice of k is crucial to finding a good balance between overfitting and underfitting.

## k

`Effect of k:` As k increases, variance decreases while bias increases. Conversely, as k decreases, variance increases while bias decreases.

`Choice of k:` Choosig based on validation error:
<div align='center'>
<img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2024/08/training-error_11.webp">
</div>



## Key Points
- It is a memory-based approach immediately adapts as we collect new training data. 
- The computational complexity for classifying new examples grows linearly with the number of examples in the training dataset in the worst-case scenario.
- KNN is very susceptible to overfitting due to the curse of dimensionality (the closest neighbors as being too far away in a high-dimensional space to give a good estimate.). Regularization method cannot be applied here.
- All the features should be scaled as we will be taking distnace based on features.
- Optimization can be done through the dimensionality reduction by using method like PCA, LDA etc.
