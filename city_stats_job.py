from mrjob.job import MRJob
from mrjob.job import MRStep
import re
from user_agents import parse


class CityStatsJob(MRJob):
    KEY_FIELD_SEPARATOR = ';'

    JOBCONF = {
        'mapreduce.job.reduces': 5,
        'mapreduce.map.output.key.field.separator': KEY_FIELD_SEPARATOR,
        'mapreduce.partition.keypartitioner.options': '-k2',
    }

    REGEXP = re.compile('([a-z\d]+)\s+(\d+)\s+(\d+)\s+([\w\d~]+)\s+(.*)\s+([0-9]+\.[0-9]+\.[0-9]+\.\*)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)\s+([\w\d]+)')

    def partitioner(self):
        return 'org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner'

    def configure_options(self):
        super().configure_options()
        self.add_file_option("--cities")
        self.cities_dict = None

    def steps(self):
        return [MRStep(mapper=self.mapper, combiner=self.combiner, reducer=self.reducer), MRStep(reducer=self.reducer_second)]

    def mapper(self, _, line):
        if not self.cities_dict:
            with open(self.options.cities, 'r') as cities_file:
                r = '(\d+)\s+(\w+)'
                self.cities_dict = {int(pair[0]): pair[1] for pair in re.findall(r, cities_file.read())}
        try:
            contents = re.findall(self.REGEXP, line)[0]
        except IndexError:
            contents = None
        if contents:
            city_id = int(contents[7])
            price = int(contents[-1])
            try:
                city_name = self.cities_dict[city_id]
                if price >= 250:
                    os = parse(contents[4]).os.family
                    output_key = self.KEY_FIELD_SEPARATOR.join([city_name, os])
                    yield output_key, 1
            except KeyError:
                pass

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        actual_key = ''
        for letter in key:
            if letter != ';':
                actual_key += letter
            else:
                break
        yield actual_key, sum(values)

    def reducer_second(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    CityStatsJob().run()
