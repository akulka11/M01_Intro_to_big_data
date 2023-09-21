################################
# Name : Aditya Pradip Kulkarni # 
# ID : 1330344                  #
################################
from mrjob.job import MRJob
import re

class BigramCount(MRJob):

    def mapper(self, _, line):

        words = re.findall(r"[\w']+", line.lower())
        
        for i in range(len(words) - 1):
            bigram = f"{words[i]},{words[i+1]}"
            yield (bigram, 1)

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    BigramCount.run()
