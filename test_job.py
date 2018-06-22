from mrjob.job import MRJob


class TestJob(MRJob):

    def mapper(self, _, line):
        if len(line) > 0:
            words = sorted(line.split(), key=len)
            max_word = words[len(words) - 1]
        else:
            max_word = ''
        yield None, max_word

    def reducer(self, key, values):
        words = sorted([word for word in values], key=len)
        max_word = words[len(words) - 1]
        yield max_word, len(max_word)


if __name__ == '__main__':
    TestJob.run()
