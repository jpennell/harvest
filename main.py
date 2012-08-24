# encoding: utf-8
HARVESTERS = ['TestHarvester,main', 'MarkdownUrlHarvester,harvest.harvesters']

import harvest
from harvest import Harvester


class TestHarvester(Harvester):
    def harvest(self, text):
        print 'TestHarvester:', text


def main():
    parse("nothing")
    parse("[example](http://example.ca)")
    parse("[example](<http://example.ca>)")
    parse("[example](http://example.ca 'example title')")


def parse(text):
    print "----------------------------------"
    print text
    #harvest.harvest(text, harvesters=HARVESTERS)
    print harvest.harvest(text)


if __name__ == "__main__":
    main()
