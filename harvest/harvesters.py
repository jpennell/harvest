import re
from utils import escape
from urlparse import urlparse, urlunparse


class Entity(object):
    """
    Entity object
    """
    def __init__(self):
        """
        Initialize entity object
        """
        self.original_text = None  # Original text a harvester will match (not the full text, but the matched text)
        self.display_text = None  # Display text harvester determines, in case we're in a situation where we cannot display html
        self.display_html = None  # HTML text harvester determines
        self.start_index = None  # Index in full text where the pattern started
        self.end_index = None  # Index in the full text where the pattern ended

    def __str__(self):
        return '%s [%d, %d]' % (self.display_html, self.start_index, self.end_index)


class Harvester(object):
    """
    Base harvester object, just defines the interface
    """
    def harvest(self, text):
        """
        Extract entities from text that contains a markdown link

        Returns a list of entities found in the text
        """
        print 'Harvester:', text


class MarkdownUrlHarvester(Harvester):
    """
    Markdown URL Harvester

    Matches patterns like:
    [text](url)
    [text](<url>)
    [text](url "tooltip")

    and converts them to html:
    <a href="href" rel="external nofollow" title="title">text</a>
    <a href="href" rel="external nofollow">text</a>

    or text:
    text (href)
    """
    def __init__(self):
        """
        Initialize Markdown URL Harvester
        """
        #Matches '[text]'
        square_brackets_re = '''\[([^\]]+)\]'''

        #Matches any whitespace (or nothing)
        all_whitespace_re = '''\s*'''

        #Matches 'whitespace <url> whitespace'
        angle_bracket_url_re = all_whitespace_re + '''<[^\)\s]+>''' + all_whitespace_re

        #Matches 'whitespace url whitespace'
        url_re = all_whitespace_re + '[^\)\s<>]+' + all_whitespace_re

        #Matches 'whitespace url whitespace title whitespace'
        url_title = all_whitespace_re + url_re + all_whitespace_re + '''"[^\)]+"''' + all_whitespace_re

        #Matches <url> or url "title"
        angle_bracket_url_or_url_title_re = angle_bracket_url_re + '''|''' + url_re + '''|''' + url_title

        #Matches (url) or (url "title") or (<url>)
        circular_brackets_re = '''\((''' + angle_bracket_url_or_url_title_re + ''')\)'''

        #Final regex, matches [text](url), or [text](<url>), or [text](url "title")
        r = square_brackets_re + all_whitespace_re + circular_brackets_re

        self.regex = re.compile(r)
        self.entities = []

    def harvest(self, text):
        """
        Extract entities from text that contains a markdown link
        """
        self.regex.sub(self._harvest_url, text)
        return self.entities

    def _sanitize_url(self, url):
        """
        Sanitize a url
        """
        default_url = '#'

        #Try and parse the url
        try:
            scheme, netloc, path, params, query, fragment = url = urlparse(url)
        except ValueError:
            # Bad url - so bad it couldn't be parsed.
            return default_url

        locless_schemes = ['', 'mailto', 'news']
        if netloc == '' and scheme not in locless_schemes:
            return default_url

        for part in url[2:]:
            if ":" in part:
                # Not a safe url
                return default_url

        # Url passes all tests. Return url as-is.
        return urlunparse(url)

    def _harvest_url(self, match):

        #Group 0 is the entire matched text
        matched_text = match.group(0)

        #Group 1 is the text of the markdown url pattern
        text = match.group(1).strip()

        #Group 2 is the text inside the circle brackets in the markdown url pattern
        href = match.group(2).strip()

        #href could be:
        #http://example.com
        #<http://example.com>
        #http://example.com "title"
        if href:

            if href[0] == "<":
                #pattern is <http://example.com>
                href = href[1:-1]
                title = None

            elif href[-1] == '"':
                #pattern is http://example.com "title"
                #split and find href/title (getting rid of the quotes around title)
                split = re.split(ur'[\u200b\s]+"', href, flags=re.UNICODE)  # split on any whitespace and a double quote
                href = split[0].strip()
                title = split[1][:-1].strip()

            else:
                #pattern is: http://example.com
                #therefore the is no title attribute
                title = None

            #Sanitize the url
            href = self._sanitize_url(href)
        else:
            #There was some problem and there is no href
            #Make sure there is no title and the href address goes nowhere
            href = '#'
            title = None

        if title:
            title = escape(title)
            html = '<a href="%s" rel="external nofollow" title="%s">%s</a>' % (href, title, text)
        else:
            html = '<a href="%s" rel="external nofollow">%s</a>' % (href, text)

        #Build the entity
        entity = Entity()
        entity.original_text = matched_text
        entity.display_text = '%s (%s)' % (text, href)
        entity.display_html = html
        entity.start_index = match.start(0)
        entity.end_index = match.end(0)

        self.entities.append(entity)
