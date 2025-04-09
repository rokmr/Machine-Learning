# Naive Bayes
Naive Bayes classifiers have a general assumption that the effect of an attribute value on a given class in independent of the values of the other attributes. This assumption is called class-conditional independence.

$P(A|B) = \frac{P(B|A) P(A)}{P(B)}$

Posterior = likelihood prob * prior/ marginal

In the context of Naive Bayes classification, we often work with log probabilities to avoid numerical underflow. The log posterior probability is calculated as:

$\log P(A|B) = \log P(B|A) + \log P(A) - \log P(B)$

The denominator $P(B)$ is omitted since it's constant across classes and doesn't affect the argmax

$\log P(A|B) = \log P(B|A) + \log P(A) $

$ posterior = posterior + prior$

This matches the implementation shown in the code where:
- $\log P(A)$ is the prior probability
- $\log P(B|A)$ is calculated as the sum of log probabilities from the PDF


## Additional Details
**Prior Probability(P(A)):** The prior probability represents our initial belief about the probability of each class before seeing any evidence. It's calculated by dividing the number of instances of a particular class by the total number of instances in the training dataset.

**Likelihood Probability(P(B|A)):** This represents the probability of observing the features given a particular class. It measures how likely we are to see these features if the class is true.

**Marginal Probability(P(B)):** This is the probability of observing the features regardless of the class. It acts as a normalizing constant to ensure our probabilities sum to 1.

**Posterior Probability(P(A|B)):** This is our final probability of a class given the observed features. It's calculated by multiplying the likelihood by the prior and dividing by the marginal probability.


$P(x|c) = \frac{1}{\sqrt{2\pi\sigma_c^2}} e^{-\frac{(x-\mu_c)^2}{2\sigma_c^2}}$

we assume that the data follows Gaussian distribution, due 
to which the probability of an item, given a class label c, can be defined as

## Advantages
1. Simple and fast to train and predict
2. Works well with small datasets
3. Can handle both continuous and discrete features
4. Less prone to overfitting

## Disadvantages
1. Assumes features are independent (naive assumption)
2. May not perform well when features are correlated
3. Requires features to be normally distributed for optimal performance
4. Sensitive to feature scaling


# Laplacian Smoothing

Laplacian smoothing (also known as additive smoothing) is a technique used to handle zero probability problems in Naive Bayes classification. It adds a small constant α to the count of each feature-class combination to prevent zero probabilities.

For a feature value x and class c, the smoothed probability is calculated as:

$P(x|c) = \frac{count(x,c) + \alpha}{count(c) + \alpha|V|}$

Where:
- count(x,c) is the number of times feature x appears with class c
- count(c) is the number of instances of class c
- α is the smoothing parameter (typically 1)
- |V| is the size of the vocabulary (number of unique feature values)
