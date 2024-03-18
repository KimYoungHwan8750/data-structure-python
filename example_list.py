import random
import time

random_ = random.Random()

class ExampleUtils:
    @staticmethod
    def create_list(num):
        arr = []
        for i in range(num):
            arr.append(random_.randint(0, 100))
        return arr

    @staticmethod
    def print_runtime(func):
        def wrap(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(result)
            print("소요시간 : %0.5fs" % (time.time() - start))
            return result
        return wrap
