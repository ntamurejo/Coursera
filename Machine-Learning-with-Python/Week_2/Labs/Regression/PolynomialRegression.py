import matplotlib.pyplot as plt 
import pandas as pd 
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

class PolynomialRegression(object):
    def __init__(self,df,cdf,train,test):
        self.__number_of_rows = 9
        self.__df = df
        self.__cdf = cdf
        self.__train = train
        self.__test = test

    def process(self):
        vars_independientes_x = ['ENGINESIZE']
        var_depent_y = ['CO2EMISSIONS']
        train_x_poly, train_y, test_x, test_y = self.apply_polynomial_reg(vars_independientes_x,var_depent_y,2)
        clf = self.apply_linear_reg(train_x_poly, train_y)
        self.draw_polynomial_degree_2_reg(clf)
        self.evaluation(2,test_x,test_y,clf)
    def apply_polynomial_reg(self,vars_x,var_y,grado_polynomio):
         #Multiple Regression Model
        poly = PolynomialFeatures(degree=grado_polynomio)
        train_x = np.asanyarray(self.__train[vars_x])
        train_y = np.asanyarray(self.__train[var_y])
        train_x_poly = poly.fit_transform(train_x)

        test_x = np.asanyarray(self.__test[vars_x])
        test_y = np.asanyarray(self.__test[var_y])
        
        return train_x_poly,train_y, test_x, test_y

    def apply_linear_reg(self,train_polynomio,train_y):
        clf = linear_model.LinearRegression()
        train_y_ = clf.fit(train_polynomio, train_y)
        # The coefficients
        print ('Coefficients: ', clf.coef_)
        print ('Intercept: ',clf.intercept_)
        return clf

    def draw_polynomial_degree_2_reg(self,clf):
        plt.scatter(self.__train.ENGINESIZE, self.__train.CO2EMISSIONS,  color='blue')
        XX = np.arange(0.0, 10.0, 0.1)
        yy = clf.intercept_[0]+ clf.coef_[0][1]*XX+ clf.coef_[0][2]*np.power(XX, 2)
        plt.plot(XX, yy, '-r' )
        plt.xlabel("Engine size")
        plt.ylabel("Emission")
        plt.show()

    def evaluation(self,grado_polynomio, test_x, test_y, clf):
        poly = PolynomialFeatures(degree=grado_polynomio)
        test_x_poly = poly.fit_transform(test_x)
        test_y_ = clf.predict(test_x_poly)

        print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
        print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
        print("R2-score: %.2f" % r2_score(test_y_ , test_y) )
