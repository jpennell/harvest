HARVESTERS = ['MarkdownUrlHarvester,harvest.harvesters']


def harvest(text, harvesters=HARVESTERS):
    instances = [load_class(namespace) for namespace in harvesters]
    [instance.harvest(text) for instance in instances]


def load_class(namespace):
    module = __import__(namespace.split(',')[1])
    return getattr(module, namespace.split(',')[0])()
