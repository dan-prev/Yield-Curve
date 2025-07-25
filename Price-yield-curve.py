#Importing numpy to do basic numerical operation and matplotlib to create and manipulate plots
import numpy as np
import matplotlib as plt

#Determines the GG plot style
plt.style.use('ggplot')

#Create a Class with functions to: generate cash flow times, compute full price from the yield, compute clean price from the yield, compute accrued interest and compute the duration

class Bond(object):
  def __init__(self, maturity, coupon, frequency):
    self._maturity = maturity
    self._coupon = coupon
    self._frequency = frequency
#Generate cash flow times
  def flowTimes(self):
    small = 1e-10
    numPaymentsMinusOne = int(self._maturity * self._frequency - small)
    firstPayment = self._maturity - numPaymentsMinusOne / self._frequency
    return np.linspace(firstPayment, self._maturity, numPaymentsMinusOne+1)
#Compute dirty price of the bond from the yield
  def fullPriceFromYield(self, y):
    paymentTimes = Bond.flowTimes(self)
    price = 0.0
    for t in paymentTimes:
      df = 1.0/(1.0 + y/self._frequency)**(t*self._frequency)
      price += (self._coupon / self._frequency) * df
    price += df
    return price
#Computes clean price of the bond from the yield
  def cleanPriceFromYield(self, y):
    cleanPrice = self.fullPriceFromYield(y) - self.accrued()
    return cleanPrice
#Computer accrued interest of the bond
  def accrued(self):
    paymentTimes - self.flowTimes()
    accruedPeriod = 1.0/self._frequency - paymentTimes[0]
    return accruedPeriod * self._coupon
#Computes duration of the bond
  def duration(self, y):
    paymentTimes = self.flowTimes()
    price = 0.0; df = 1.0; fv = 1.0
    weights = []
    for t in paymentTimes:
      df = 1.0/(1.0 = y/self._frequency)**(t*self._frequency)
      if t == paymentTimes[-1]:
        weight = (fv + self._coupon / self._frequency) * df / Bond.fullPriceFromYield(self, y)
      else:
        weight = (self._coupon / self._frequency) * df / Bond.fullPriceFromYield(self, y)
      weights.append(weight * t) 
    return np.sum(weights)

maturity = 10.2
coupon = 0.05
frequency = 2.0
bond = Bond(maturity, coupon, frequency)
y = 0.05

bond.fullPriceFromYield(y)

bond.duration(y)

bond.accrued()

#Set a maximum value
maxYield = 21
yieldCurve = [bond.fullPriceFromYield(i/100) for i in range (maxYield)]

#This list comprehension code makes in a single line the operation in comments put below
#YieldCurve = []
#for i in range(maxYield):
#yields = i/100
#yieldCurves = bond.fullPriceFromYield(yields)
#yieldCurve.append(yieldCurves)

plt.figure(figsize=(12,6)) #Sizing the plot
plt.plot(yieldCurve, 'o-') #Selecting market
plt.xlabel('Yield', size = 14) #Labeling X axis
plt.ylabel('Price', size = 14) #Labeling Y axis
plt.title('Relationship between Yields and Prices', size = 20); #Titling the graph

#Polynomial function for the relationship between yield and price
def fitAndPlot(y, price, d):
  coeffs = np.polfit(y, price, deg=d)
  ry = np.polyval(coeffs, y)
  plt.figure(figsize=(12,6))
  plt.plot(y, price, 'o-')
  plt.xlabel('Yield', size = 14) #Labeling X axis
  plt.ylabel('Price', size = 14) #Labeling Y axis
  plt.title('Relationship between Yields and Prices', size = 20);

yields = np.linspace(0.0,20,20, endpoint = True)/100 #Array of 20 equally spaced points between 0 and 20
fitAndPlot(yields*100, bond.fullPriceFromYield(yields), 3) #Showing the plot
