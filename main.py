# encoding: utf-8
HARVESTERS = ['TestHarvester,main', 'MarkdownUrlHarvester,harvest.harvesters']

import harvest
from harvest import Harvester


class TestHarvester(Harvester):
    def harvest(self, text):
        print 'TestHarvester:', text


def main():
    parse("[Test](http://example.com)")


def parse(text):
    print "----------------------------------"
    print text
    harvest.harvest(text, harvesters=HARVESTERS)


if __name__ == "__main__":
    main()
