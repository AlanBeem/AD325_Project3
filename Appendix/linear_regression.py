class LinearRegression:
    def __init__(self, x: list, y: list):
        if len(x) != len(y):
            print("x and y must be the same length")
            raise IndexError
        else:
            # y = mx + b (by least squares):
            x_bar = sum(x) / len(x)
            y_bar = sum(y) / len(y)
            m_div = sum([(x[i] - x_bar)**2 for i in range(len(x))])
            if m_div > 0:
                self.m = (sum([(x[i] - x_bar) * (y[i] - y_bar) for i in range(len(x))]) /
                    m_div)
            else:
                self.m = 0
            self.b = y_bar - self.m * x_bar
            # r squared:
            if sum([y[i] - y_bar for i in range(len(y))]) != 0:
                self.r_2 = 1 - sum([(y[i] - self(x[i]))**2 for i in range(len(x))]) / sum([(y[i] - y_bar)**2 for i in range(len(x))])
            else:
                self.r_2 = 0
    
    def __call__(self, x: float|int):
        return self.m * x + self.b
    

class PolynomialRegression:
    pass


class MultipleRegression:
    # multiple linear regression, or polynomial regression
    pass

