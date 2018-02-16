import redbaron

from autocorrect.helpers.bools import isdocumentable, isforbidden, isroot
from autocorrect.helpers.constants import typenames
from autocorrect.helpers.correctors import PyCorrector
from autocorrect.helpers.methods import get_dotproxy_names, nodes_stats, pretty


class FileItem(object):
    '''
    A generic file type.
    '''
    ext_ = None

    def __init__(self, meta):
        self.meta = meta

    def read(self):
        with open(self.meta.path, 'r') as f:
            return f.read()

    def correct(self, *methods):
        raise NotImplementedError('corrections not implemented for this filetype')

    @property
    def stats(self):
        return {}

    def __repr__(self):
        content = [item for sublist in [pretty(k, v, 0) for k, v in self.stats.items()]
                   for item in sublist]
        return '\n'.join([self.meta.path] + content) + '\n'


class Pyfile(FileItem):
    '''
    A python file.
    '''
    ext_ = 'py'

    def __init__(self, meta):
        super(Pyfile, self).__init__(meta)
        self.tree = redbaron.RedBaron(self.read())
        self._isequal = self.read().strip() == self.tree.dumps().strip()
        self._corrector = PyCorrector(meta.config)

    @property
    def documentable(self):
        return self.tree.find_all(isdocumentable)

    @property
    def docstrings(self):
        return self.tree.find_all(typenames.strings,
                                  lambda x: isdocumentable(x.parent))

    @property
    def header(self):
        return self.tree.find_all(typenames.strings + typenames.comment,
                                  lambda x: isroot(x.parent))

    @property
    def string_literals(self):
        return self.tree.find_all(typenames.strings,
                                  lambda x: not isdocumentable(x.parent))

    @property
    def ascii_literals(self):
        return self.tree.find_all(typenames.ascii,
                                  lambda x: not isdocumentable(x.parent))

    @property
    def imports(self):
        return list(set(['.'.join(get_dotproxy_names(n)[:3]) for n in
                         self.tree.find_all(typenames.imports)]))

    @property
    def forbidden_imports(self):
        return [i for i in self.imports if isforbidden(i, self.meta.config)]

    def correct(self, *methods):
        if 0 or 'all' in methods:
            methods = [0]
        funcs = self._corrector.get(methods)
        for m in funcs:
            m(self)
        self.save()

    def save(self):
        if not self._isequal:
            print(self.meta.path + ' was not equal')
            return
        else:
            with open(self.meta.path, 'w') as pyfile:
                pyfile.write(self.tree.dumps())

    @property
    def stats(self):
        return {
            'docs': {
                'documentable items': len(self.documentable),
                'strings': len(self.docstrings)
                },
            'literals': nodes_stats(self.string_literals),
            'imports': sorted(self.imports),
            'forbidden imports': sorted(self.forbidden_imports)
            }
