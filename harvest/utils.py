def escape(text):
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
    }
    return "".join(html_escape_table.get(c, c) for c in text)


def repeat_to_length(string_to_expand, length):
    return (string_to_expand * ((length / len(string_to_expand)) + 1))[:length]
