# encoding: utf-8
HARVESTERS = ['TestHarvester,main', 'MarkdownUrlHarvester,harvest.harvesters']

import harvest
from harvest import Harvester


class TestHarvester(Harvester):
    def harvest(self, text):
        print 'TestHarvester:', text


def main():
    parse("[Test](example.com)")
    parse("[Test](http://example.com)")
    parse("[Test](https://example.com)")
    parse("[Test](ftp://example.com)")
    parse("[Test](file://D://example/blahblah/readme.txt)")
    parse("[Test](mailto://pennell.james@gmail.com)")


def parse(text):
    print "----------------------------------"
    print text
    #harvest.harvest(text, harvesters=HARVESTERS)
    harvest.harvest(text)


if __name__ == "__main__":
    main()
