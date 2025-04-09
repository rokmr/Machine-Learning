# Logistic Regression
It is used for te classification problem. It uses linear regressing equaition to predict the class probabilities.

Equation:

$y = wx+b$

This $y$ is feed to the sigmoid function to get the output between 0 and 1 as probailities. So,

$y = \frac{1}{1+ e^{-(wx+b)}}$


**Logistic regression doesn't require:**
- Normality of residuals
- Homoscedasticity

**Logistic regression specifically requires:**
- Binary/categorical outcome
- Linear relationship with log odds (not the outcome itself)

## Effect of Outlier
Since here we focus on finding the decision boundry that linearly seperate the classes. So we mostly focus on the points which are closer to the boundry. Therefore, otlier will have very less effect here.

## Logistic Regression as Maximum Likelihood Estimation(MLE)

Assuming the Bernoulli distribution (i.e., binary classification). Let, $y \in {0,1}$ if $p$ is the probability of class as 1. Then according to MLE we need to maximize $p^y$ if class is 1 and $(1-p)^{(1-y)}$ if class is 0.

$L = \Pi_{i=1}^{N} p_i^{y_i} (1-p_i)^{(1-y_i)}$

Multipying such large number may result in the overflow. So take `log` on both side.

$L = \sum_{i=1}^{N} (y_i \ln p_i + (1 - y_i) \ln (1 - p_i))$

$Loss = -Likelihood$

This loss penelizes much more than MSE when prediciton is wrong.

## Prediction
Here, $pred = \frac{1}{1+ e^{-(wx+b)}}$, if $pred > \tau$ then class 1 else class 0.

$\tau$ is decided according to problem statement.

## Multi-Class (N)
1. One-vs-all: We need to have N models 

    $pred = argmax_{i} f_{i}(x)$

2. One-vs-one: We need to have $\binom{N}{2}$ models, where each model is trained to distinguish between a pair of classes. For N classes, this results in $\frac{N(N-1)}{2}$ binary classifiers. The prediction is made by majority voting across all pairwise comparisons:

    $pred = argmax_{i} \sum_{j \neq i} \mathbb{I}(f_{ij}(x) = i)$

    where $f_{ij}(x)$ is the binary classifier for classes i and j, and $\mathbb{I}$ is the indicator function.

3. Mathematical: Use softmax instead of sigmoid and use cross-entropy loss.

