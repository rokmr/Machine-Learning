# Linear Regression
Linear Regression would be appropriate since we are predicting a continuous value.

Linear Regression works when these 4 assumtion being followed:
1. **Linearity:** this means that the relationship must be linear between the independent variables and dependent variables. 
$y= \beta_0 + \beta_1 x_1 + \beta_2 x_2$ or $y= \beta_0 + \beta_1 sin(x) + \beta_2 cosx(x)$
2. **Homoscedasticity:** there is constant variance of the residuals (errors). 
3. **Independence:** independent variables (observations) are not highly correlated.
4. **Normality:** for any fixed value of our observations 

Note:
- Find the collinearity by using Variance Inflation Factors (VIF). VIF > 5 variable are dependent.
- Solve collinearity by either removing one of the features or linearly combine both features. 

## Metrics
- **Root Mean Square Error (RMSE) :** Calculates the average of the squared difference between the predicted and actual values. Thus, larger errors (outliers or poor prediction) are flagged 
more than when using MAE due to squaring errors. $RMSE = \sqrt{\frac{\sum_{i=1}^{N}(y_i - \hat{y_i})^2}{N}}$

- **Mean Absolute Error (MAE) :** Calculates the average of the absolute difference between the predicted and actual values. As a result, it does not punish large errors as much as RMSE. $MAE = \frac{\sum_{i=1}^{N}|y_i - \hat{y_i}|}{N}$

## Methods
1. Closed form solution: $w = (X^TX)^{-1}X^Ty$
- Useful, when optimal solution is needed. Issue when inverse does notexist and computationally expensive when data is too large.
2. Optimization algorithm, typically Gradient Descent (GD) or Stochastic Gradient Descent (SGD).

## Feature Importance
If the features are normalized then the coefficients are an indication of feature importance, i.e. features with higher coefficients are more useful for 
prediction.