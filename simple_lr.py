import numpy as np

# Load data from data set
myFile = np.genfromtxt('another_dataset.txt',delimiter=",")
x_val = myFile[:,0]
y_val = myFile[:,1]
x_val = x_val.tolist()
y_val = np.reshape(y_val,(97,))
y_val = y_val.tolist()
class SingleLinearRegression:

    def __init__(self):
        print("Model created")
    def mean(self,array):
        total = 0
        for i in array:
            total += i
        return total/len(array)
    def calc_slope(self,x,y):
        m_x = self.mean(x)
        m_y = self.mean(y)
        ss_xy = 0
        ss_xx = 0
        for i in range(len(x)):
            ss_xy += (x[i] - m_x)*(y[i] - m_y)
            ss_xx += (x[i] - m_x)*(x[i] - m_x)
        slope = ss_xy/ss_xx
        return slope

    def intercept(self,x,y):
        slope = self.calc_slope(x,y)
        y_m = self.mean(y)
        x_m = self.mean(x)
        intercept = y_m - slope*x_m
        return intercept

model = SingleLinearRegression()
slope = model.calc_slope(x_val,y_val)
intercept = model.intercept(x_val,y_val)
print("y = ",slope,"x + ",intercept)
