import redbaron


def isdocumentable(node):
    return isinstance(node, (
        redbaron.DefNode, redbaron.ClassNode, redbaron.RedBaron))


def isroot(node):
    return isinstance(node, redbaron.RedBaron)


def isforbidden(import_name, config):
    exclude = config['imports']['exclude']
    conditional_exclude = config['imports']['conditional_exclude']
    conditional_include = config['imports']['conditional_include']
    if any([x in import_name for x in exclude]):
        return True
    parts = import_name.split('.', 1)
    if parts[0] in conditional_exclude.keys():
        if any([x == parts[1] for x in conditional_exclude.get(parts[0])]):
            return True
    if parts[0] in conditional_include.keys():
        if all([x != parts[1] for x in conditional_include.get(parts[0])]):
            return True
    return False
