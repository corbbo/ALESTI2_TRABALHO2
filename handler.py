import read_data as rd
import time
class Handler:
    def __init__(self, filename: str = "exemplo.txt") -> None:
        self.graph = rd.read_data(filename)
        
    def time_delta(self) -> int:
        time_start = time.time()
        if self.graph is None: return
        self.graph.hydrogen_to_gold() 
        time_end = time.time()
        delta = time_end - time_start
        delta = round(delta, 10)
        return delta
    
    def handle(self, limit, filename) -> str:
        average = 0
        for i in range(limit):
            average += self.time_delta()
        average /= limit
        string = ""
        string += filename + ": "
        string += self.graph.assess()
        if average < 0.000001:
            string += " [" + "Average time: " + format(average * 1000000000, ".2f") + "ns]"
        elif average < 0.001:
            string += " [" + "Average time: " + format(average * 1000000, ".2f") + "us]"
        elif average < 1:
            string += " [" + "Average time: " + format(average * 1000, ".2f") + "ms]"
        else:
            string += " [" + "Average time: " + format(average, ".2f") + "s]"
        return string