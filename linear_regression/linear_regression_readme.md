Covariance: 
Covariance is all about to find the linear relationship between two variables. Covariance tell us the direction of variables and help to measures how two variables move together.
If one variable increases as the other decreases that means *negative covariance*

If one variable increases as the other variable also increases that means *positive covariance*


The values of covariance can be any positive or negative number.


Correlation coefficient is a powerful tool for understanding the linear association between variables. Correlation coefficient tell us the direction and strength of variables.
Correlation coefficient value comes from -1 to 1.

If value 1 that means a positive linear relationship between the variables.

If value −1 that means a perfect negative linear relationship between the variables.

If value 0 that means no linear relationship between the variables.


How Covariance & Correlation coefficient help in linear regression?
Covariance directly measures how two variables change together. A positive covariance indicates that as one variable increases, the other tends to increase as well, while a negative covariance indicates the opposite.
Correlation coefficient provides a clear indication of both the strength and direction of the linear relationship between two variables. It's easy to interpret: close to 1 indicates a strong positive linear relationship, close to -1 indicates a strong negative linear relationship, and close to 0 indicates no linear relationship.

Suppose we have dataset of human height corresponding weights.If the covariance between height and weights is positive, this suggests that more height might be associated with higher weights. The correlation coefficient, if also positive and high (close to 1), would confirm not only that this relationship is linear but also strong.


Regression: regression is all about to understand the relationship between a dependent variable (the outcome you are trying to predict) and one or more independent variables (the variables are used to predict the dependent variable).

What is dependent and independent variable.
Independent variables are input variables help to predict the outcome mainly we denoted as x.
Dependent variable are the predictor/outcome variable mainly we denoted as Y.

Linear regression is a statistical way used to model and analyze relationship between a dependent variable and one or more independent variables where the relationships are linear (straight line). Linear regression help us to Predict the dependent variable using independent variables. The goal is to find a linear equation(straight line) that best fits through the data points.

When to use Linear regression:
When there is +ve or -ve Correlation between the variables.
If one variable increases as the other decreases that means *negative correlation*
If one variable increases as the other variable also increases that means *positive correlation*


Example
Suppose we have dataset of houses and you want to predict the price of a house based on various factors so there is Dependent and Independent Variable is: 
Dependent Variable (y): House price
Independent Variable (x): SqFT, no of bedrooms, Lot Size etc.

Types of Linear Regression:
Simple Linear Regression:
It is all about the one dependent variable and one independent variable and we predict dependent variable using one one independent variable.
simple linear regression equation is :
Y = mx+b

Y is the dependent variable
x is the independent variable
b is the intercept
m is the slope


Multiple Linear Regression
It is all about the one dependent variable and more than one independent variable and we predict dependent variable using multiple independent variable.
simple linear regression equation is :

Y = mx++m2x2.........mnxn + b

Y is the dependent variable
x,x2, xn is the independent variables
b is the intercept
m is the slope


Steps in Linear Regression Analysis:
1. Collecting Data.
Here's an example of loading a dataset:

2. Cleaning the data.
Clean the data by handling missing values and outliers, and ensuring data types are correct.

3.Check Correlation coefficient between variables.
	Calculate the correlation matrix to understand the relationships between variables.

	If value 1 that means a positive linear relationship between the variables.

	If value −1 that means a perfect negative linear relationship between the variables.

	If value 0 that means no linear relationship between the variables.

4.Visual Inspection:
To more ensure create scatter plots to visually inspect the relationship between variables. A linear pattern suggests that linear regression might be appropriate.

5. Find the best fit line
Use libraries such as scikit-learn to perform linear regression and determine the best fit line.

6. Making Predictions
Use the trained model to make predictions on new data and evaluate its performance.




