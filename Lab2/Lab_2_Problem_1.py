################################
# Name : Aditya Pradip Kulkarni # 
# ID : 1330344                  #
################################
from mrjob.job import MRJob
import re

class UniqueWordCount(MRJob):

    def configure_args(self):
        super(UniqueWordCount, self).configure_args()
        self.add_passthru_arg('--no-cleanup', dest='cleanup', default=True, action='store_false',
                              help='Prevent automatic cleanup of temporary directory')

    def mapper(self, _, line):

        words = re.findall(r'\w+', line.lower())
        for word in words:
            yield (word, 1)

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    UniqueWordCount.run()
