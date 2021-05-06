"""
File: model.py
Project 8.4

Models multiple cashiers.
"""

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus
        self.cashiers = list()
        for count in range(numCashiers):
            self.cashiers.append(Cashier(count + 1))
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        """Run the clock for n ticks."""

        for currentTime in range(self.lengthOfSimulation):
            customer = Customer.generateCustomer(self.probabilityOfNewArrival,currentTime,self.averageTimePerCus)# Attempt to generate a new customer
            if customer != None: #checks that a customer is created
                # Sends customer to a randomly chosen cashier if successfully generated
                random.choice(self.cashiers).addCustomer(customer)
            for cashier in self.cashiers: # Tell all cashiers to provide another unit of service
                cashier.serveCustomers(currentTime) # serves customers randomly timed

    def __str__(self):
        """Returns the string rep of the results of the simulation."""
        return "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
               "        PROCESSED   WAIT TIME   LINE\n" + \
               "\n".join(map(str, self.cashiers))
