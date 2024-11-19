import math
from random import SystemRandom


class DataTupler:
    def __init__(self, headings: list[str], noise=False):
        self.headings = headings
        self.function_order_headings = headings.copy()
        SystemRandom().shuffle(self.function_order_headings)
        self.functions = []
        for _ in self.function_order_headings[1:]:
            # multiple = SystemRandom().random() * 2 + SystemRandom().random() - SystemRandom().random()
            multiple = 2 * (SystemRandom().random() - SystemRandom().random())
            base = SystemRandom().random() - SystemRandom().random() + 2
            self.functions.append(SystemRandom().choice([lambda p: multiple * math.atan(p + base / 100), lambda p: p * multiple + base]))
        self.noise = noise
    
    def get_tuple(self) -> tuple:
        """returns a tuple ordered by headings as passed to __init__."""
        a_list = [SystemRandom().random()]
        for f in self.functions:
            a_list.append(f(a_list[-1] + 0 if not self.noise else SystemRandom().random() / 10))
        return tuple([a_list[self.function_order_headings.index(h)] for h in self.headings])
    

class ArithmeticTree:  # for arbitrary functions
    def __init__():
        pass

    def evaluate(self):
        # omits data that involves division by 0, returning None
        # interprets uninitialized arguments as 1
        pass

