class sigma():
    def __init__(self, n)  :
        self.n = n
        
    def get_square_sum(self):
        # sigma °ø½Ä 
        return (self.n * (self.n + 1) * ((2 * self.n) + 1)) / 6
    
    def get_sum_square(self):
        sum = 0
        for x in range(1, self.n + 1):
            sum += x
            
        return sum * sum

    def compute(self):
        print self.get_square_sum()
        print self.get_sum_square()
        return self.get_sum_square() - self.get_square_sum()

if __name__ == '__main__':
    problem6 = sigma(100)
    print problem6.compute()
