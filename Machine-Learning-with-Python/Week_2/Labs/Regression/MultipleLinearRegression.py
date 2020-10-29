import matplotlib.pyplot as plt 
import pandas as pd 
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score


class MultipleLinearRegression(object):
    def __init__(self,df,cdf,train,test):
        self.__number_of_rows = 9
        self.__df = df
        self.__cdf = cdf
        self.__train = train
        self.__test = test

    def process(self):
        y = self.__cdf.CO2EMISSIONS
        x = self.__cdf.ENGINESIZE
        print("------------------------------------------")
        print("Plotting each of these features vs the emission, to see how linear is their relation")
        self.draw_graphics(1,x,y,"Engine size","Emission")
        plt.show()
        self.training_draw()
        #Example 1 Multilinear regression
        vars_independientes_x = ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']
        var_depent_y = ['CO2EMISSIONS']
        train_x,train_y, regr = self.apply_multi_linear_reg(vars_independientes_x,var_depent_y)
        x, y = self.prediction(regr,vars_independientes_x,var_depent_y)
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % regr.score(x, y))

        print("-------------------------------------------------")
        #Example 2 Multilinear regression
        #Multiple Regression Model adding FUEL CITY AND HWY
        vars_independientes_x = ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']
        var_depent_y = ['CO2EMISSIONS']
        train_x,train_y, regr = self.apply_multi_linear_reg(vars_independientes_x,var_depent_y)
        x, y = self.prediction(regr,vars_independientes_x,var_depent_y)
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % regr.score(x, y))

    def draw_graphics(self,number_figure,variable_independent_x,variable_dependient_y,title_x,title_y):
        plt.figure(number_figure)
        plt.scatter(variable_independent_x, variable_dependient_y, color='blue')
        plt.xlabel(title_x) 
        plt.ylabel(title_y) 
    
    def training_draw(self):
        #Train data distribution
        plt.scatter(self.__train.ENGINESIZE, self.__train.CO2EMISSIONS,  color='green')
        plt.xlabel("Engine size")
        plt.ylabel("Emission")
        plt.show()

    def apply_multi_linear_reg(self,vars_x,var_y):
         #Multiple Regression Model
        regr = linear_model.LinearRegression()
        train_x = np.asanyarray(self.__train[vars_x])
        train_y = np.asanyarray(self.__train[var_y])
        regr.fit (train_x, train_y)
        # The coefficients
        print ('Coefficients: ', regr.coef_)
        return train_x,train_y,regr

    def prediction(self,regr,vars_x,var_y):
         #Prediction
        y_hat= regr.predict(self.__test[vars_x])
        x = np.asanyarray(self.__test[vars_x])
        y = np.asanyarray(self.__test[var_y])
        print("Residual sum of squares: %.2f" % np.mean((y_hat - y) ** 2))
        return x, y




