# autocorrect

## what this is
A CLI-based tool for making bulk changes to files via Python, partly achieved through syntax trees (for .py files, using [redbaron](https://github.com/PyCQA/redbaron)) and partly through regular expressions.

It was made as part of a refactoring effort for a specific project (the NHM data portal).

It currently only contains methods for refactoring Python files but it is intended to be extensible.

## what this isn't
A tool that will fix all your syntax problems. It's not pulling from any set of code standards, and any new refactorings have to be defined via new methods in `Corrector` classes.

## installation
```sh
pip install git+git://github.com/alycejenni/autocorrect.git#egg=autocorrect
```

Make a config file (by default autocorrect looks in `~/.config/autocorrect/autocorrect.json` but you can specify a different json file using the `--config` option). An example `autocorrect.json` can be found in the `data` folder.

## usage
Options:
```sh
--config /path/to/config
--name "My Project" # for inserting into the header if a {} token is present; can also be defined in the config
```

### `stats` subcommand
Basic usage:
```sh
autocorrect [--config /path/to/config] [--name "My Project"] [/path/to/dir] stats [filetypes]
```

Show statistics for all files:
```sh
autocorrect /path/to/dir stats
```

Stats for just (e.g.) `txt` and `md` files:
```sh
autocorrect /path/to/dir stats txt md
```

### `fix` subcommand
Basic usage:
```sh
autocorrect [--config /path/to/config] [--name "My Project"] [/path/to/dir] fix [filetype] [fix(es)]
```

Run all fixes for `.py` files:
```sh
autocorrect /path/to/dir fix py all
```

Run the _literal string quote_ and _docstring quote_ fixes for `.py` files:
```sh
autocorrect /path/to/dir fix py literal docstring
```

## contributing
Please feel free to fork, submit pull requests, etc.!
