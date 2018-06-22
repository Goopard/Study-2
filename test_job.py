from mrjob.job import MRJob


class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        max_word = sorted([word for word in line.split()], key=len)[len(line.split()) - 1]
        yield None, max_word

    def reducer(self, key, values):
        words = sorted([word for word in values], key=len)
        max_word = words[len(words) - 1]
        yield max_word, len(max_word)


if __name__ == '__main__':
    MRWordFrequencyCount.run()