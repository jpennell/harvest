DEFAULT_HARVESTERS = ['MarkdownUrlHarvester,harvest.harvesters']


def harvest(text, harvesters=DEFAULT_HARVESTERS):
    instances = [load_class(namespace) for namespace in harvesters]

    for instance in instances:
        entities = instance.harvest(text)
        for entity in entities:
            print entity


def load_class(namespace):
    module = __import__(namespace.split(',')[1])
    return getattr(module, namespace.split(',')[0])()
