import matplotlib.pyplot as plt 
import pandas as pd 
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

class NoneLinearRegression(object):
    def __init__(self,df):
        self.__df = df
        self.__beta_1 = 0.10
        self.__beta_2 = 1990.0

    def process(self):
        #self.__draw_types_non_linear()
        x_data, y_data = (self.__df["Year"].values, self.__df["Value"].values)
        self.__plot_data(x_data,y_data)
        self.__choose_model()
        #logistic function
        Y_pred = self.sigmoid(x_data)

        #plot initial prediction against datapoints
        plt.plot(x_data, Y_pred*15000000000000.)
        plt.plot(x_data, y_data, 'ro')
        plt.show()

        # Lets normalize our data
        xdata =x_data/max(x_data)
        ydata =y_data/max(y_data)

        popt, pcov = curve_fit(self.sigmoid, xdata, ydata)
 
        #print the final parameters
        print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))

        x = np.linspace(1960, 2015, 55)
        x = x/max(x)
        plt.figure(figsize=(8,5))
        y = self.sigmoid(x, *popt)
        plt.plot(xdata, ydata, 'ro', label='data')
        plt.plot(x,y, linewidth=3.0, label='fit')
        plt.legend(loc='best')
        plt.ylabel('GDP')
        plt.xlabel('Year')
        plt.show()

    def sigmoid(self,x):
        y = 1 / (1 + np.exp(-self.__beta_1*(x-self.__beta_2)))
        return y

    def __ecuation_linear_reg(self):

        x = np.arange(-5.0, 5.0, 0.1)
        ##You can adjust the slope and intercept to verify the changes in the graph
        y = 2*(x) + 3
        y_noise = 2 * np.random.normal(size=x.size)
        ydata = y + y_noise
        #plt.figure(figsize=(8,6))
        plt.plot(x, ydata,  'bo')
        plt.plot(x,y, 'r') 
        plt.ylabel('Dependent Variable')
        plt.xlabel('Indepdendent Variable')
        plt.show()

    def __draw_types_non_linear(self):
        print("Plotting some none linear functions")
        self.__cubic()
        self.__logarithmic()
        self.__quadratic()
        self.__exponential()
        self.__sigmoidal()

    ## Types of Non-Linear functions
    def __cubic(self):
        x = np.arange(-5.0, 5.0, 0.1)
        #You can adjust the slope and intercept to verify the changes in the graph
        y = 1*(x**3) + 1*(x**2) + 1*x + 3
        y_noise = 20 * np.random.normal(size=x.size)
        ydata = y + y_noise
        plt.plot(x, ydata,  'bo')
        plt.plot(x,y, 'r') 
        plt.ylabel('Dependent Variable')
        plt.xlabel('Indepdendent Variable')
        plt.title("Cubic")
        plt.show()
    
    def __quadratic(self):
        x = np.arange(-5.0, 5.0, 0.1)
        ##You can adjust the slope and intercept to verify the changes in the graph
        y = np.power(x,2)
        y_noise = 2 * np.random.normal(size=x.size)
        ydata = y + y_noise
        plt.plot(x, ydata,  'bo')
        plt.plot(x,y, 'r') 
        plt.ylabel('Dependent Variable')
        plt.xlabel('Indepdendent Variable')
        plt.title("Quadratic")
        plt.show()

    def __exponential(self):
        X = np.arange(-5.0, 5.0, 0.1)
        ##You can adjust the slope and intercept to verify the changes in the graph
        Y= np.exp(X)
        plt.plot(X,Y) 
        plt.ylabel('Dependent Variable')
        plt.xlabel('Indepdendent Variable')
        plt.title("Exponential")
        plt.show()

    def __logarithmic(self):
        X = np.arange(-5.0, 5.0, 0.1)

        Y = np.log(X)

        plt.plot(X,Y) 
        plt.ylabel('Dependent Variable')
        plt.xlabel('Indepdendent Variable')
        plt.title("Logarithmic")
        plt.show()

    def __sigmoidal(self):
        X = np.arange(-5.0, 5.0, 0.1)
        Y = 1-4/(1+np.power(3, X-2))
        plt.plot(X,Y) 
        plt.ylabel('Dependent Variable')
        plt.xlabel('Indepdendent Variable')
        plt.title("Sigmoidal")
        plt.show()

    def __plot_data(self,x_data, y_data):
        plt.figure(figsize=(8,5))
        
        plt.plot(x_data, y_data, 'ro')
        plt.ylabel('GDP')
        plt.xlabel('Year')
        plt.show()

    def __choose_model(self):
        X = np.arange(-5.0, 5.0, 0.1)
        Y = 1.0 / (1.0 + np.exp(-X))

        plt.plot(X,Y) 
        plt.ylabel('Dependent Variable')
        plt.xlabel('Indepdendent Variable')
        plt.show()

