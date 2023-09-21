################################
# Name : Aditya Pradip Kulkarni # 
# ID : 1330344                  #
################################

from mrjob.job import MRJob
import re

class WordCountWithStopwords(MRJob):

    def configure_args(self):
        super().configure_args()
        self.add_file_arg('--stopwords', help='Path to stopwords file')

    def mapper_init(self):
        with open(self.options.stopwords, 'r') as stopwords_file:
            self.stopwords = set(line.strip() for line in stopwords_file)

    def mapper(self, _, line):
        words = re.findall(r'\w+', line.lower())
        for word in words:
            if word not in self.stopwords:
                yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    WordCountWithStopwords.run()
