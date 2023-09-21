################################
# Name : Aditya Pradip Kulkarni # 
# ID : 1330344                  #
################################
from mrjob.job import MRJob
import re

class InvertedIndex(MRJob):

    def mapper(self, _, line):
        doc_id = line.split(":")[0].strip()
        words = re.findall(r"[\w']+", line.lower())
        
        for word in words:
            yield (word, doc_id)

    def reducer(self, key, values):
        doc_ids = set(values)
        yield (key, list(doc_ids))

if __name__ == '__main__':
    InvertedIndex.run()
