class Harvester(object):
    def harvest(self, text):
        print 'Harvester:', text


class MarkdownUrlHarvester(Harvester):
    def harvest(self, text):
        print 'MarkdownUrlHarvester:', text
