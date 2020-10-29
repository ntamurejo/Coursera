import matplotlib.pyplot as plt 
import pandas as pd 
import pylab as pl
import numpy as np
import sys
from sklearn import linear_model
from sklearn.metrics import r2_score
from SimpleLinearRegression import SimpleLinearRegression
from MultipleLinearRegression import MultipleLinearRegression
from PolynomialRegression import PolynomialRegression
from NoneLinearRegression import NoneLinearRegression


class Regression(object):
    def __init__(self):
        #Read file with data
        self.__df = pd.read_csv("FuelConsumptionCo2.csv")
        self.__df_none = pd.read_csv("china_gdp.csv")
        self.__cdf = None
        self.__train_data = None
        self.__test_data = None

    def show_data(self):
        print("Show header data:\n %s" %self.__get_header())
        print("------------------------------------------")
        print("Summarize:\n %s" %self.__get_describe())
        print("------------------------------------------")

    def compute(self,type_regression):
        if str(type_regression) == "1":
            print("Simple")
            self.__set_cdf(self.__df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]) 
            self.__split_data()
            simple_reg = SimpleLinearRegression(self.__df, self.__cdf, self.__train_data,self.__test_data)
            simple_reg.process()
        elif str(type_regression)== "2":
            print("Multiple")
            self.__set_cdf(self.__df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']])
            self.__split_data()
            multi_reg = MultipleLinearRegression(self.__df,self.__cdf, self.__train_data,self.__test_data)
            multi_reg.process()   
        elif str(type_regression)== "3":
            print("Polynomial") 
            self.__set_cdf(self.__df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]) 
            self.__split_data()
            poly_reg = PolynomialRegression(self.__df,self.__cdf, self.__train_data,self.__test_data)
            poly_reg.process()  
        elif str(type_regression)== "4":
            print("None Linear Regression")
            none_reg = NoneLinearRegression(self.__df_none)
            none_reg.process()  
            
        else:
            print("Value error")       

    def __split_data(self):
        #Next step is split data in train and test set, 80% of the entire data for training, and the 20% for testing. We create
        # a mask to select random rows.
        msk = np.random.rand(len(self.__df)) < 0.8
        self.set_train_data(self.__cdf[msk])
        self.set_test_data(self.__cdf[~msk])

    #Take a look at the dataset
    def __get_header(self):
        return self.__df.head()

    #Lets first have a descriptive exploration on our data
    # summarize the data
    def __get_describe(self):
        return self.__df.describe()

    def set_train_data(self,value):
        self.__train_data = value

    def set_test_data(self,value):
        self.__test_data = value

    def get_train_data(self):
        return self.__train_data

    def get_test_data(self):
        return self.__test_data

    def __set_cdf(self,value):
        self.__cdf = value

    def __get_cdf(self):
        return self.__cdf


regression = Regression()
regression.show_data()
print("\n1 --> Simple")
print("\n2 --> Multiple")
print("\n3 --> Polynominal")
print("\n4 --> None Linear Regression")
type_regression = input("Please, choose type regression:")
regression.compute(type_regression)


