from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, key, line):
        for word in line.split():
            yield(word, 1)

    def reducer(self, word, counts):
        yield(word, sum(counts))

# These lines enable the execution of mrjob; without them, the application will not work.
if __name__ == '__main__':
    MRWordCount.run()