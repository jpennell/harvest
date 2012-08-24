def escape(text):
    """
    HTML escape a string

    escape('<  >  '  "  &')
    -> '&lt;  &gt;  &apos;  &quot;  &amp;'
    """
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
    }
    return "".join(html_escape_table.get(c, c) for c in text)


def repeat_to_length(string_to_expand, length):
    """
    Repeat a particular string to a length

    repeat_to_length('a', 10)
    -> 'aaaaaaaaaa'
    """
    return (string_to_expand * ((length / len(string_to_expand)) + 1))[:length]


def print_entity(entity):
    """
    Pretty print a harvester entity object
    """
    print 'entity.original_text:', entity.original_text
    print 'entity.display_text:', entity.display_text
    print 'entity.display_html:', entity.display_html
    print 'entity.start_index:', entity.start_index
    print 'entity.end_index:', entity.end_index
