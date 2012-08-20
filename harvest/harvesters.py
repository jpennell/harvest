import re
from utils import escape


class Entity(object):
    def __init__(self):
        self.display_text = None
        self.display_html = None
        self.start_index = None
        self.end_index = None

    def __str__(self):
        return '%s [%d, %d]' % (self.display_html, self.start_index, self.end_index)


class Harvester(object):
    def harvest(self, text):
        print 'Harvester:', text


class MarkdownUrlHarvester(Harvester):
    def __init__(self):
        self.regex = re.compile("""\[([^\]]+)\]\(([^)]+)\)""")
        self.entities = []

    def harvest(self, text):
        self.regex.sub(self._harvest_url, text)
        return self.entities

    def _harvest_url(self, match):
        matched_text = match.group(0)
        matched_text_split = matched_text.split("](")

        text = escape(matched_text_split[0][1:])
        link = escape(matched_text_split[1][:len(matched_text_split[1]) - 1])

        protocols = ['http://', 'https://', 'ftp://', 'file://', 'mailto://']
        protocol_specified = [link.find(protocol) >= 0 for protocol in protocols]

        if not any(p for p in protocol_specified):
            link = "http://%s" % link

        html = '<a href="%s" rel="external nofollow">%s</a>' % (link, text)

        entity = Entity()
        entity.display_text = text
        entity.display_html = html
        entity.start_index = match.start()
        entity.end_index = match.end()

        self.entities.append(entity)
