# encoding: utf-8

import unittest
from harvest.harvesters import MarkdownUrlHarvester


class TestMarkdownUrlHarvester(unittest.TestCase):
    """
    Test Markdown URL Harvester
    """

    def setUp(self):
        self.harvester = MarkdownUrlHarvester()

    def test_no_url(self):
        """
        Text: 'nothing'
        Should return an empty list
        """
        entities = self.harvester.harvest('nothing')
        self.assertEqual(entities, [])

    def test_single_entity(self):
        """
        Text: '[example](http://example.ca)'
        Should a single entity
        """
        entities = self.harvester.harvest('[example](http://example.ca)')
        self.assertEqual(len(entities), 1)

    def test_single_entity_original_text(self):
        """
        Text: '[example](http://example.ca)'
        Original text should be '[example](http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca)')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')

    def test_single_entity_display_text(self):
        """
        Text: '[example](http://example.ca)'
        Display text should be 'example (http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')

    def test_single_entity_display_html(self):
        """
        Text: '[example](http://example.ca)'
        Display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        """
        entities = self.harvester.harvest('[example](http://example.ca)')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')

    def test_single_entity_start_index(self):
        """
        Text: '[example](http://example.ca)'
        Start index should be 0
        """
        entities = self.harvester.harvest('[example](http://example.ca)')
        self.assertEqual(entities[0].start_index, 0)

    def test_single_entity_end_index(self):
        """
        Text: '[example](http://example.ca)'
        End index should be 28
        """
        entities = self.harvester.harvest('[example](http://example.ca)')
        self.assertEqual(entities[0].end_index, 28)

    def test_single_entity_text_before_original_text(self):
        """
        Text: 'text [example](http://example.ca)'
        Original text should be '[example](http://example.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca)')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')

    def test_single_entity_text_before_display_text(self):
        """
        Text: 'text [example](http://example.ca)'
        Display text should be 'example (http://example.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')

    def test_single_entity_text_before_display_html(self):
        """
        Text: 'text [example](http://example.ca)'
        Display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        """
        entities = self.harvester.harvest('text [example](http://example.ca)')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')

    def test_single_entity_text_before_start_index(self):
        """
        Text: 'text [example](http://example.ca)'
        Start index should be 5
        """
        entities = self.harvester.harvest('text [example](http://example.ca)')
        self.assertEqual(entities[0].start_index, 5)

    def test_single_entity_text_before_end_index(self):
        """
        Text: 'text [example](http://example.ca)'
        End index should be 33
        """
        entities = self.harvester.harvest('text [example](http://example.ca)')
        self.assertEqual(entities[0].end_index, 33)

    def test_single_entity_text_after_original_text(self):
        """
        Text: '[example](http://example.ca) text'
        Original text should be '[example](http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca) text')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')

    def test_single_entity_text_after_display_text(self):
        """
        Text: 'text [example](http://example.ca)'
        Display text should be 'example (http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca) text')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')

    def test_single_entity_text_after_display_html(self):
        """
        Text: 'text [example](http://example.ca)'
        Display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        """
        entities = self.harvester.harvest('[example](http://example.ca) text')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')

    def test_single_entity_text_after_start_index(self):
        """
        Text: 'text [example](http://example.ca)'
        Start index should be 0
        """
        entities = self.harvester.harvest('[example](http://example.ca) text')
        self.assertEqual(entities[0].start_index, 0)

    def test_single_entity_text_after_end_index(self):
        """
        Text: 'text [example](http://example.ca)'
        End index should be 28
        """
        entities = self.harvester.harvest('[example](http://example.ca) text')
        self.assertEqual(entities[0].end_index, 28)

    def test_single_entity_text_before_and_after_original_text(self):
        """
        Text: 'text [example](http://example.ca) text'
        Original text should be '[example](http://example.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')

    def test_single_entity_text_before_and_after_display_text(self):
        """
        Text: 'text [example](http://example.ca)'
        Display text should be 'example (http://example.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')

    def test_single_entity_text_before_and_after_display_html(self):
        """
        Text: 'text [example](http://example.ca)'
        Display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')

    def test_single_entity_text_before_and_after_start_index(self):
        """
        Text: 'text [example](http://example.ca)'
        Start index should be 5
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text')
        self.assertEqual(entities[0].start_index, 5)

    def test_single_entity_text_before_and_after_end_index(self):
        """
        Text: 'text [example](http://example.ca)'
        End index should be 33
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text')
        self.assertEqual(entities[0].end_index, 33)

    def test_angle_brackets_original_text(self):
        """
        Text: '[example](<http://example.ca>)'
        Original text should be '[example](<http://example.ca>)'
        """
        entities = self.harvester.harvest('[example](<http://example.ca>)')
        self.assertEqual(entities[0].original_text, '[example](<http://example.ca>)')

    def test_angle_brackets_display_text(self):
        """
        Text: '[example](<http://example.ca>)'
        Display text should be 'example (http://example.ca)'
        """
        entities = self.harvester.harvest('[example](<http://example.ca>)')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')

    def test_angle_brackets_display_html(self):
        """
        Text: '[example](<http://example.ca>)'
        Display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        """
        entities = self.harvester.harvest('[example](<http://example.ca>)')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')

    def test_angle_brackets_start_index(self):
        """
        Text: '[example](<http://example.ca>)'
        Start index should be 0
        """
        entities = self.harvester.harvest('[example](<http://example.ca>)')
        self.assertEqual(entities[0].start_index, 0)

    def test_angle_brackets_end_index(self):
        """
        Text: '[example](<http://example.ca>)'
        End index should be 30
        """
        entities = self.harvester.harvest('[example](<http://example.ca>)')
        self.assertEqual(entities[0].end_index, 30)

    def test_title_original_text(self):
        """
        Text: '[example](http://example.ca "example title")'
        Original text should be '[example](http://example.ca "example title")'
        """
        entities = self.harvester.harvest('[example](http://example.ca "example title")')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca "example title")')

    def test_title_display_text(self):
        """
        Text: '[example](http://example.ca "example title")'
        Display text should be 'example (http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca "example title")')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')

    def test_title_display_html(self):
        """
        Text: '[example](http://example.ca "example title")'
        Display html should be '<a href="http://example.ca" rel="external nofollow" title="example title">example</a>'
        """
        entities = self.harvester.harvest('[example](http://example.ca "example title")')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow" title="example title">example</a>')

    def test_title_start_index(self):
        """
        Text: '[example](http://example.ca "example title")'
        Start index should be 0
        """
        entities = self.harvester.harvest('[example](http://example.ca "example title")')
        self.assertEqual(entities[0].start_index, 0)

    def test_title_end_index(self):
        """
        Text: '[example](http://example.ca "example title")'
        End index should be 44
        """
        entities = self.harvester.harvest('[example](http://example.ca "example title")')
        self.assertEqual(entities[0].end_index, 44)

    def test_multiple_entities(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca)'
        Should be two returned entities
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(len(entities), 2)

    def test_multiple_entities_original_text(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca)'
        First original text should be '[example](http://example.ca)'
        Second original text should be '[example2](http://example2.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')
        self.assertEqual(entities[1].original_text, '[example2](http://example2.ca)')

    def test_multiple_entities_display_text(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca)'
        First display text should be 'example (http://example.ca)'
        Second display text should be 'example2 (http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')
        self.assertEqual(entities[1].display_text, 'example2 (http://example2.ca)')

    def test_multiple_entities_display_html(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca)'
        First display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        Second display html should be '<a href="http://example2.ca" rel="external nofollow">example2</a>'
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')
        self.assertEqual(entities[1].display_html, '<a href="http://example2.ca" rel="external nofollow">example2</a>')

    def test_multiple_entities_start_index(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca)'
        First start index should be 0
        Second start index should be 28
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].start_index, 0)
        self.assertEqual(entities[1].start_index, 28)

    def test_multiple_entities_end_index(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca)'
        First end index should be 28
        Second end index should be 58
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].end_index, 28)
        self.assertEqual(entities[1].end_index, 58)

    def test_multiple_entities_text_before_original_text(self):
        """
        Text: 'text [example](http://example.ca)[example2](http://example2.ca)'
        First original text should be '[example](http://example.ca)'
        Second original text should be '[example2](http://example2.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')
        self.assertEqual(entities[1].original_text, '[example2](http://example2.ca)')

    def test_multiple_entities_text_before_display_text(self):
        """
        Text: 'text [example](http://example.ca)[example2](http://example2.ca)'
        First display text should be 'example (http://example.ca)'
        Second display text should be 'example2 (http://example.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')
        self.assertEqual(entities[1].display_text, 'example2 (http://example2.ca)')

    def test_multiple_entities_text_before_display_html(self):
        """
        Text: 'text [example](http://example.ca)[example2](http://example2.ca)'
        First display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        Second display html should be '<a href="http://example2.ca" rel="external nofollow">example2</a>'
        """
        entities = self.harvester.harvest('text [example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')
        self.assertEqual(entities[1].display_html, '<a href="http://example2.ca" rel="external nofollow">example2</a>')

    def test_multiple_entities_text_before_start_index(self):
        """
        Text: 'text [example](http://example.ca)[example2](http://example2.ca)'
        First start index should be 5
        Second start index should be 33
        """
        entities = self.harvester.harvest('text [example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].start_index, 5)
        self.assertEqual(entities[1].start_index, 33)

    def test_multiple_entities_text_before_end_index(self):
        """
        Text: 'text [example](http://example.ca)[example2](http://example2.ca)'
        First end index should be 33
        Second end index should be 63
        """
        entities = self.harvester.harvest('text [example](http://example.ca)[example2](http://example2.ca)')
        self.assertEqual(entities[0].end_index, 33)
        self.assertEqual(entities[1].end_index, 63)

    def test_multiple_entities_text_between_original_text(self):
        """
        Text: '[example](http://example.ca) text [example2](http://example2.ca)'
        First original text should be '[example](http://example.ca)'
        Second original text should be '[example2](http://example2.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca) text [example2](http://example2.ca)')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')
        self.assertEqual(entities[1].original_text, '[example2](http://example2.ca)')

    def test_multiple_entities_text_between_display_text(self):
        """
        Text: '[example](http://example.ca) text [example2](http://example2.ca)'
        First display text should be 'example (http://example.ca)'
        Second display text should be 'example2 (http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca) text [example2](http://example2.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')
        self.assertEqual(entities[1].display_text, 'example2 (http://example2.ca)')

    def test_multiple_entities_text_between_display_html(self):
        """
        Text: '[example](http://example.ca) text [example2](http://example2.ca)'
        First display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        Second display html should be '<a href="http://example2.ca" rel="external nofollow">example2</a>'
        """
        entities = self.harvester.harvest('[example](http://example.ca) text [example2](http://example2.ca)')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')
        self.assertEqual(entities[1].display_html, '<a href="http://example2.ca" rel="external nofollow">example2</a>')

    def test_multiple_entities_text_between_start_index(self):
        """
        Text: '[example](http://example.ca) text [example2](http://example2.ca)'
        First start index should be 5
        Second start index should be 33
        """
        entities = self.harvester.harvest('[example](http://example.ca) text [example2](http://example2.ca)')
        self.assertEqual(entities[0].start_index, 0)
        self.assertEqual(entities[1].start_index, 34)

    def test_multiple_entities_text_between_end_index(self):
        """
        Text: '[example](http://example.ca) text [example2](http://example2.ca)'
        First end index should be 33
        Second end index should be 63
        """
        entities = self.harvester.harvest('[example](http://example.ca) text [example2](http://example2.ca)')
        self.assertEqual(entities[0].end_index, 28)
        self.assertEqual(entities[1].end_index, 64)

    def test_multiple_entities_text_after_original_text(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca) text'
        First original text should be '[example](http://example.ca)'
        Second original text should be '[example2](http://example2.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca) text')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')
        self.assertEqual(entities[1].original_text, '[example2](http://example2.ca)')

    def test_multiple_entities_text_after_display_text(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca) text'
        First display text should be 'example (http://example.ca)'
        Second display text should be 'example2 (http://example.ca)'
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca) text')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')
        self.assertEqual(entities[1].display_text, 'example2 (http://example2.ca)')

    def test_multiple_entities_text_after_display_html(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca) text'
        First display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        Second display html should be '<a href="http://example2.ca" rel="external nofollow">example2</a>'
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca) text')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')
        self.assertEqual(entities[1].display_html, '<a href="http://example2.ca" rel="external nofollow">example2</a>')

    def test_multiple_entities_text_after_start_index(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca) text'
        First start index should be 0
        Second start index should be 28
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca) text')
        self.assertEqual(entities[0].start_index, 0)
        self.assertEqual(entities[1].start_index, 28)

    def test_multiple_entities_text_after_end_index(self):
        """
        Text: '[example](http://example.ca)[example2](http://example2.ca) text'
        First end index should be 28
        Second end index should be 58
        """
        entities = self.harvester.harvest('[example](http://example.ca)[example2](http://example2.ca) text')
        self.assertEqual(entities[0].end_index, 28)
        self.assertEqual(entities[1].end_index, 58)

    def test_multiple_entities_text_everywhere_original_text(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca) text'
        First original text should be '[example](http://example.ca)'
        Second original text should be '[example2](http://example2.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca) text')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')
        self.assertEqual(entities[1].original_text, '[example2](http://example2.ca)')

    def test_multiple_entities_text_everywhere_display_text(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca) text'
        First display text should be 'example (http://example.ca)'
        Second display text should be 'example2 (http://example.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca) text')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')
        self.assertEqual(entities[1].display_text, 'example2 (http://example2.ca)')

    def test_multiple_entities_text_everywhere_display_html(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca) text'
        First display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        Second display html should be '<a href="http://example2.ca" rel="external nofollow">example2</a>'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca) text')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')
        self.assertEqual(entities[1].display_html, '<a href="http://example2.ca" rel="external nofollow">example2</a>')

    def test_multiple_entities_text_everywhere_start_index(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca) text'
        First start index should be 5
        Second start index should be 39
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca) text')
        self.assertEqual(entities[0].start_index, 5)
        self.assertEqual(entities[1].start_index, 39)

    def test_multiple_entities_text_everywhere_end_index(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca) text'
        First end index should be 33
        Second end index should be 69
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca) text')
        self.assertEqual(entities[0].end_index, 33)
        self.assertEqual(entities[1].end_index, 69)

    def test_multiple_entities_mixed_patterns_original_text(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca "title") text'
        First original text should be '[example](http://example.ca)'
        Second original text should be '[example2](http://example2.ca "title")'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca "title") text')
        self.assertEqual(entities[0].original_text, '[example](http://example.ca)')
        self.assertEqual(entities[1].original_text, '[example2](http://example2.ca "title")')

    def test_multiple_entities_mixed_patterns_display_text(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca "title") text'
        First display text should be 'example (http://example.ca)'
        Second display text should be 'example2 (http://example.ca)'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca "title") text')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')
        self.assertEqual(entities[1].display_text, 'example2 (http://example2.ca)')

    def test_multiple_entities_mixed_patterns_display_html(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca "title") text'
        First display html should be '<a href="http://example.ca" rel="external nofollow">example</a>'
        Second display html should be '<a href="http://example2.ca" rel="external nofollow" title="title">example2</a>'
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca "title") text')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')
        self.assertEqual(entities[1].display_html, '<a href="http://example2.ca" rel="external nofollow" title="title">example2</a>')

    def test_multiple_entities_mixed_patterns_start_index(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca "title") text'
        First start index should be 5
        Second start index should be 39
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca "title") text')
        self.assertEqual(entities[0].start_index, 5)
        self.assertEqual(entities[1].start_index, 39)

    def test_multiple_entities_mixed_patterns_end_index(self):
        """
        Text: 'text [example](http://example.ca) text [example2](http://example2.ca "title") text'
        First end index should be 33
        Second end index should be 77
        """
        entities = self.harvester.harvest('text [example](http://example.ca) text [example2](http://example2.ca "title") text')
        self.assertEqual(entities[0].end_index, 33)
        self.assertEqual(entities[1].end_index, 77)

    def test_missing_angle_bracket(self):
        """
        Text: '[example](<http://example.ca)'
        """
        entities = self.harvester.harvest('[example](<http://example.ca)')
        self.assertEqual(entities, [])

    def test_missing_other_angle_bracket(self):
        """
        Text: '[example](http://example.ca>)'
        """
        entities = self.harvester.harvest('[example](http://example.ca>)')
        self.assertEqual(entities, [])

    def test_fake_protocol(self):
        """
        Text: '[example](fake://example.ca)'
        Should only match valid link protocols
        """
        entities = self.harvester.harvest('[example](fake://example.ca)')
        self.assertEqual(len(entities), 0)

    def test_malformed_protocol(self):
        """
        Text: '[example](http//example.ca)'
        Should only match valid link protocols
        """
        entities = self.harvester.harvest('[example](http//example.ca)')
        from harvest.utils import print_entity
        print_entity(entities[0])
        self.assertEqual(len(entities), 0)

    def test_malformed_protocol1(self):
        """
        Text: '[example](http:/example.ca)'
        Should only match valid link protocols
        """
        entities = self.harvester.harvest('[example](http:/example.ca)')
        self.assertEqual(len(entities), 0)

    def test_ftp_protocol(self):
        """
        Text: '[example](ftp://example.ca)'
        """
        entities = self.harvester.harvest('[example](ftp://example.ca)')
        self.assertEqual(len(entities), 1)

    def test_mailto_protocol(self):
        """
        Text: '[example](mailto://example.ca)'
        """
        entities = self.harvester.harvest('[example](mailto://example.ca)')
        self.assertEqual(len(entities), 1)

    def test_file_protocol(self):
        """
        Text: '[example](file://example.ca)'
        """
        entities = self.harvester.harvest('[example](file://example.ca)')
        self.assertEqual(len(entities), 1)

    def test_git_protocol(self):
        """
        Text: '[example](git://example.ca)'
        """
        entities = self.harvester.harvest('[example](git://example.ca)')
        self.assertEqual(len(entities), 1)

    def test_https_protocol(self):
        """
        Text: '[example](https://example.ca)'
        """
        entities = self.harvester.harvest('[example](https://example.ca)')
        self.assertEqual(len(entities), 1)

    def test_no_protocol(self):
        """
        Text: '[example](example.ca)'
        """
        entities = self.harvester.harvest('[example](example.ca)')
        self.assertEqual(len(entities), 1)

    def test_no_protocol_display_text(self):
        """
        Text: '[example](example.ca)'
        Need to prepend http:// to any link that doesn't have a protocol
        """
        entities = self.harvester.harvest('[example](example.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://example.ca)')

    def test_no_protocol_display_html(self):
        """
        Text: '[example](example.ca)'
        Need to prepend http:// to any link that doesn't have a protocol
        """
        entities = self.harvester.harvest('[example](example.ca)')
        self.assertEqual(entities[0].display_html, '<a href="http://example.ca" rel="external nofollow">example</a>')

    def test_www(self):
        """
        Text: '[example](www.example.ca)'
        """
        entities = self.harvester.harvest('[example](www.example.ca)')
        self.assertEqual(len(entities), 1)

    def test_www_display_text(self):
        """
        Text: '[example](www.example.ca)'
        """
        entities = self.harvester.harvest('[example](www.example.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://www.example.ca)')

    def test_subdomain(self):
        """
        Text: '[example](example.example.ca)'
        """
        entities = self.harvester.harvest('[example](example.example.ca)')
        self.assertEqual(len(entities), 1)

    def test_subdomain_display_text(self):
        """
        Text: '[example](example.example.ca)'
        """
        entities = self.harvester.harvest('[example](example.example.ca)')
        self.assertEqual(entities[0].display_text, 'example (http://example.example.ca)')

    def test_params(self):
        """
        Text: 'text [example](http://example.com/#search?q=iphone%20-filter%3Alinks)'
        """
        entities = self.harvester.harvest('text [example](http://example.com/#search?q=iphone%20-filter%3Alinks)')
        self.assertEqual(len(entities), 1)

    def test_params_display_text(self):
        """
        Text: 'text [example](http://example.com/#search?q=iphone%20-filter%3Alinks)'
        """
        entities = self.harvester.harvest('text [example](http://example.com/#search?q=iphone%20-filter%3Alinks)')
        self.assertEqual(entities[0].display_text, 'example (http://example.com/#search?q=iphone%20-filter%3Alinks)')

    def test_port_number(self):
        """
        Text: '[example](http://example.com:3000)'
        """
        entities = self.harvester.harvest('[example](http://example.com:3000)')
        self.assertEqual(len(entities), 1)

    def test_port_number_display_text(self):
        """
        Text: '[example](http://example.com:3000)'
        """
        entities = self.harvester.harvest('[example](http://example.com:3000)')
        self.assertEqual(entities[0].display_text, 'example (http://example.com:3000)')

    def test_circle_brackets_in_url(self):
        """
        Text: '[example](http://en.wikipedia.org/wiki/Primer_(film))'
        """
        entities = self.harvester.harvest('[example](http://en.wikipedia.org/wiki/Primer_(film))')
        self.assertEqual(len(entities), 1)

    def test_circle_brackets_in_url_display_text(self):
        """
        Text: '[example](http://en.wikipedia.org/wiki/Primer_(film))'
        Close circle bracket in wikipedia link should work
        """
        entities = self.harvester.harvest('[example](http://en.wikipedia.org/wiki/Primer_(film))')
        self.assertEqual(entities[0].display_text, 'example (http://en.wikipedia.org/wiki/Primer_(film))')
