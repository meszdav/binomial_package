# TODO: import necessary libraries
import matplotlib.pyplot as plt
import math
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
    
 
    def __init__(self, p=.5, n =25):       
        Distribution.__init__(self)
        self.p = p
        self.n = n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        

    def calculate_mean(self):
        
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p * self.n
        
        return self.mean
         
    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        
        return self.stdev
        
   
    def replace_stats_with_data(self):
        
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        
        self.n = len(self.data)
        self.p = sum(self.data)/self.n
        
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n
    
    # TODO: write a method plot_bar() that outputs a bar chart of the data set according to the following specifications.
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.bar([0,1], [len(self.data)-sum(self.data),sum(self.data)])
     
    def pdf(self,k=20):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
       
        Returns:
            float: probability density function output
        """
        return math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k)) * \
               self.p**k*(1 - self.p)**(self.n-k)

    def plot_pdf():
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """        
        x = range(0, k)
       
        y_list = []
        
        for i in x:
            y = self.pdf(i)
            y_list.append(y)
            
        plt.bar(x,y)
        plt.title("Binomial Mass Distribution")
        plt.xlabel("[k]")
        plt.ylabel("pdf")
        
        return x,y

    def __add__(self, other):  
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
                
        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        
        return result
                        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"

