# encoding: utf-8
HARVESTERS = ['TestHarvester,main', 'MarkdownUrlHarvester,harvest.harvesters']

import harvest
from harvest import Harvester


class TestHarvester(Harvester):
    def harvest(self, text):
        print 'TestHarvester:', text


def main():
    parse("test [Test](example.com)")
    parse("[Test](http://example.com) test")
    parse("asdfasdfasdf [Test](https://example.com)")
    parse("[Test](ftp://example.com)")
    parse("[Test](file://D://example/blahblah/readme.txt)")
    parse("[Test](mailto://pennell.james@gmail.com)")

    parse("blah [Test](http://example.com) test [Test](http://example.com)")

    parse("nothing nothing")


def parse(text):
    print "----------------------------------"
    print text
    #harvest.harvest(text, harvesters=HARVESTERS)
    print harvest.harvest(text)


if __name__ == "__main__":
    main()
