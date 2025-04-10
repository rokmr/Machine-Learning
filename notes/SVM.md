# Support Vector Machine (SVM)

- SVM is a supervised learning algorithm used for classification and regression tasks. 
- SVM finds an optimal hyperplane that maximizes the margin between different classes in an N-dimensional space. While there may be multiple hyperplanes that can separate two classes of data points, SVM specifically aims to find the one with the maximum distance (margin) between the data points of both classes.

## Mathematical Formulation

### Linear Model
Let it be a binary classification with $y \in \{1, -1\}$
<div align='center'>
<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/SVM_margin.png/960px-SVM_margin.png', width=300, height=300>
</div>

$w \cdot x_i - b = 0$ (optimal hyperplane)

$w \cdot x_i - b \ge 1$ if $y_i = 1$    - (i)

$w \cdot x_i - b \le 1$ if $y_i = -1$   - (ii)

Combining (i) & (ii) we get

$y_i (w \cdot x_i - b) \ge 1$

**Hinge Loss**

<div align='center'>
<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Hinge_loss_vs_zero_one_loss.svg/2560px-Hinge_loss_vs_zero_one_loss.svg.png', width=300, height=300>
</div>


$L(y, \hat{y}) = max(0, 1 - y \cdot \hat{y})$

- The loss is 0 when prediction is correct (same sign as true label)
- The loss increases linearly when prediction is incorrect.

Now adding regularization to above, the final loss function becomes:

$J(w,b) = \frac{1}{n}\sum_{i=1}^n max(0, 1 - y_i(w^T x_i + b)) + \frac{\lambda}{2}||w||^2$

$\lambda$ is the regularization parameter

    Above equation can be seen as contrained optimization:
        - minimize: $\frac{1}{2}||w||^2$
        - subject to: $y_i(w^T x_i + b) \geq 1$ for all $i$

### Optimization
To optimize for above loss we need to compute gradient wrt to parameters and then update them.

$\frac{\partial J}{\partial w} = \lambda w - \frac{1}{n}\sum_{i=1}^n y_i x_i \cdot I(y_i(w^T x_i + b) < 1)$

$\frac{\partial J}{\partial b} = -\frac{1}{n}\sum_{i=1}^n y_i \cdot I(y_i(w^T x_i + b) < 1)$

where,  $I()$ is the indicator function.

**Gradient Updates:**

1. No misclassification ($y_i(w^T x_i + b) \geq 1$):
   $w = w - \eta \lambda w$


2. Misclassification ($y_i(w^T x_i + b) < 1$):
   $w = w - \eta(\lambda w - y_i x_i)$
   $b = b - \eta(-y_i)$

where $\eta$ is the learning rate.


### Dual Form

The dual form of the optimization problem is:

For classification:
maximize: $\sum_{i=1}^n \alpha_i - \frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n \alpha_i \alpha_j y_i y_j x_i^T x_j$

subject to: 
- $\sum_{i=1}^n \alpha_i y_i = 0$
- $\alpha_i \geq 0$ for all $i$

The dual form is particularly useful because:
- It allows us to use the kernel trick
- Only support vectors (points with $\alpha_i > 0$) contribute to the decision boundary
- It's often more efficient to solve than the primal form


### Kernel Trick
For non-linear classification and regression, we can use kernel functions to implicitly map data to higher dimensions without explicitly computing the transformation:

Common kernels:
- Linear: $K(x,y) = x^T y$
- Polynomial: $K(x,y) = (x^T y + 1)^d$ where $d$ is the degree of the polynomial kernel.
- RBF: $K(x,y) = exp(-\gamma ||x-y||^2)$,  where $\gamma = \frac{1}{2\sigma^2}$ is the inverse of twice the variance of the Gaussian distribution. 

The kernel trick works because:
- It allows us to compute dot products in high-dimensional space without explicitly mapping to that space
- It's computationally efficient
- It enables SVM to find non-linear decision boundaries and regression functions

### Soft Margin SVM

For non-linearly separable data, we introduce slack variables $\xi_i$ to allow some misclassification:

minimize: $\frac{1}{2}||w||^2 + C\sum_{i=1}^n \xi_i$

subject to: $y_i(w^T x_i + b) \geq 1 - \xi_i$ for all $i$

where:
- $\xi_i$ represents how far a point is from its correct margin

## Advantages
- Excellent for high-dimensional data where dimensions > number of samples
- Creates clear decision boundaries through max-margin classification
- Memory efficient by only storing support vectors
- Versatile through kernel functions for non-linear classification and regression
- Good generalization due to margin maximization
- Robust to outliers in regression tasks

## Disadvantages
- Performs poorly with overlapping classes due to difficulty in finding clear margins
- Does not provide direct probability estimates (requires N-fold cross-validation)
- Computationally expensive for large datasets
- Requires careful feature scaling
- Memory requirements grow with the number of support vectors
- Sensitive to the choice of kernel parameters