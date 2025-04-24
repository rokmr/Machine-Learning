# Linear Discriminant Analysis (LDA)

LDA is a supervised dimensionality reduction and classification algorithm. Unlike PCA which focuses on maximizing variance, LDA aims to find a linear combination of features that maximizes class separation while minimizing within-class variance.

### Within-Class Scatter Matrix (SW)
Measures the variance within each class:
$S_W = \sum_c S_c$

Where for each class c:
$S_c = \sum_{i \in c} (x_i - \bar{x}_c) \cdot (x_i - \bar{x}_c)^T$

### Between-Class Scatter Matrix (SB)
Measures the variance between different classes:
$S_B = \sum_{c} n_c \cdot (\bar{x}_c - \bar{x}) \cdot (\bar{x}_c - \bar{x})^T$

Where:
- $n_c$ is the number of samples in class c
- $\bar{x}_c$ is the mean of class c
- $\bar{x}$ is the overall mean

## Fisher's Linear Discriminant

### Objective Function
To maximize class separation while minimizing within-class variance, we use Fisher's criterion:
$J(w) = \frac{w^TS_Bw}{w^TS_Ww}$

Taking the derivative with respect to w and setting it to zero:
$\frac{\partial}{\partial w}J(w) = \frac{2S_B w(w^T S_W w) - 2S_W w(w^T S_B w)}{(w^T S_W w)^2} = 0$

Simplifying:
$S_B w(w^T S_W w) = S_W w(w^T S_B w)$

$S_W^{-1}S_B w = \frac{(w^T S_B w)}{(w^T S_W w)} w$

$S_W^{-1}S_B w = \lambda w$

## Implementation Steps
1. Calculate the within-class scatter matrix ($S_W$)
2. Calculate the between-class scatter matrix ($S_B$)
3. Compute eigenvalues and eigenvectors of $S_W^{-1}S_B$
4. Select top k eigenvectors based on eigenvalues
5. Transform the data using selected eigenvectors

## Advantages
- Preserves class discriminatory information
- Reduces dimensionality while maintaining class separation
- Works well for normally distributed classes

## Limitations
- Assumes normal distribution of features
- May fail if within-class covariance is not equal across classes
- Limited by the number of classes (max components = number of classes - 1)