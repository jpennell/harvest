from utils import escape, repeat_to_length

DEFAULT_HARVESTERS = ['MarkdownUrlHarvester,harvest.harvesters']


def harvest(text, harvesters=DEFAULT_HARVESTERS):
    instances = [load_class(namespace) for namespace in harvesters]

    display_text = ''
    display_html = ''

    entities = []

    current_text = text

    for instance in instances:
        e = instance.harvest(current_text)

        current_position = 0
        for entity in e:
            entities.append(entity)
            current_position = entity.start_index
            l = len(entity.original_text)
            replacement = repeat_to_length(' ', l)
            current_text = current_text[:current_position] + \
            replacement + current_text[current_position + l:]

    current_index = 0
    for entity in entities:
        display_html = display_html + escape(text[current_index:entity.start_index]) + entity.display_html
        display_text = display_text + escape(text[current_index:entity.start_index]) + entity.display_text
        current_index = entity.end_index

    display_text = display_text + escape(text[current_index:])
    display_html = display_html + escape(text[current_index:])

    return {
        'display_text': display_text,
        'display_html': display_html,
    }


def load_class(namespace):
    module = __import__(namespace.split(',')[1])
    return getattr(module, namespace.split(',')[0])()
