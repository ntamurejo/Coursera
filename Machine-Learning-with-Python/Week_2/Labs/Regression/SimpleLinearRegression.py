import matplotlib.pyplot as plt 
import pandas as pd 
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score


class SimpleLinearRegression(object):
    def __init__(self,df,cdf,train,test):
        self.__number_of_rows = 9
        self.__df = df
        self.__cdf = cdf
        self.__train = train
        self.__test = test

    def process(self):
        y = self.__cdf.CO2EMISSIONS
        x_1 = self.__cdf.FUELCONSUMPTION_COMB
        x_2 = self.__cdf.ENGINESIZE
        x_3 = self.__cdf.CYLINDERS
        #Select some features to explore more.
        print("------------------------------------------")
        print("Plotting each of these features vs the emission, to see how linear is their relation")
        self.draw_graphics(1,x_1,y,"FUELCONSUMPTION_COMB","Emission")
        self.draw_graphics(2,x_2,y,"Engine size","Emission")
        self.draw_graphics(3,x_3,y,"CYLINDERS","Emission")
        plt.show()
        self.training_draw()
        train_x,train_y, regr = self.apply_linear_reg('ENGINESIZE','CO2EMISSIONS')
        self.plots_output(train_x,train_y,regr)
        self.evaluation(regr)

    def show_hist_features(self):
        print("Plotting each of these features")
        viz = self.__cdf
        viz.hist()
        plt.show()

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

    def plots_output(self,train_x,train_y,regr):
        #Plot outputs
        plt.scatter(self.__train.ENGINESIZE, self.__train.CO2EMISSIONS,  color='blue')
        plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
        plt.xlabel("Engine size")
        plt.ylabel("Emission")
        plt.show()

    def apply_linear_reg(self,var_x,var_y):
        #Linear Regression Simple Model
        regr = linear_model.LinearRegression()
        train_x = np.asanyarray(self.__train[[var_x]])
        train_y = np.asanyarray(self.__train[[var_y]])
        regr.fit (train_x, train_y)
        # The coefficients
        print ('Coefficients: ', regr.coef_)
        print ('Intercept: ',regr.intercept_)
        return train_x, train_y, regr

    def evaluation(self,regr):
        #Evaluation
        #Evaluation metrics provide a key role in the development of a model, as it provides insight to areas that require improvement.
        test_x = np.asanyarray(self.__test[['ENGINESIZE']])
        test_y = np.asanyarray(self.__test[['CO2EMISSIONS']])
        test_y_ = regr.predict(test_x)

        print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
        print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
        print("R2-score: %.2f" % r2_score(test_y , test_y_) )

        # #Note:- R-squared is not error, but is a popular metric for accuracy of your model. 
        # # It represents how close the data are to the fitted regression line. 
        # # The higher the R-squared, the better the model fits your data. 
        # # Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).