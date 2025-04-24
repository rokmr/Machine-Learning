# PCA
High dimensional data could be a problem: 
- An obvious reason would be more computing power/time needed to build a model 
- The curse of dimensionality: When the number of dimensions (features) increases our model starts to become more complex and dependent on the data it was trained on and so it overfits thus reducing our model performance 
- For models that use distance metrics, when the number of dimensions is too high, then each datapoint seems very similar to each other. This is because, with very large features, the distance between two data points are almost equal since they are all very far from each other. 

Method to resolve : PCA, LDA, t-SNE(non-linear correlation), AutoEncoder

## PCA 
It is `unspervised machine learning`

**Assumption:**

PCA needs a linear correlation  between all variables  (It should not have  non-linear correlations )

It is a linear combination of variables that results in a line or axis/axes that explain a maximal amount of variance from the original dataset. More formally, the eigenvectors of the covariance matrix (of the data) are the principal components and the eigenvalues represent the amount of variance carried in each principal component. 

If the eigenvectors are, all the same, PCA would not be able to select which principal component since we select the top n eigenvectors and there would be no top n since they are all equal. 

It is not necessary to remove variables that are highly correlated because PCA would project all the correlated variables onto the same principal 
component. 

Choose number of principle component such that it captures 95-99% or the variance.

## Process
1. Standardize our data (since, PCA is sensitive to the variance within features.)
2. Calculate the covariance matrix 
3. Then using this matrix we calculate eigenvectors and eigenvalues and thus the principal components from the eigenvectors

## Drawback
1. Computationally expensive 
2. Information is always lost 
3. Explainability becomes much more difficult.






