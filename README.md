# Archimedes

> An opinionated, extensible Static Site Generator for Polymaths.

# Features

None so far 😢.

# Installation

Eventually:

```bash
pip install archimedes  # Note Python3.9 required
```

# Getting started

See [Documentation](...)

# Opinions

Archimedes is _opinionated_, and a set of __core opinions__ are fundamental to the way it is structured.

## \#1 Tiny foundation, small core, fully extensible

__Foundation__: Archimedes is based on a tiny set of fundamental functionality. This is the functionality that makes up Archimedes and is responsible for outlining and executing the structure of an Archimedes site.

__Core__: The core functionality of Archimedes is located in `archimedes.core` and is made using the same API that any 1st or 3rd party plugin would be made in.
The core functionality is small, but provides the basic tools needed to setup a basic static site.

__1st Party Plugins__: Archimedes provides first party plugins that provide good, well-documented functionality that can easily be enabled, but should not be included in the core. These are located in `archimedes.plugins`.

__3rd Party Plugins__: Archimedes has first-class support for 3rd party extensions that have all the same functionality made available to them as `archimedes.core` and `archimedes.plugins` have. These can replace or augment existing functionality, even core functionality, or they may introduce new functionality.


| Pros ➕ | Cons ➖ |
| --- | --- |
| Can easily be adapted to users needs | Some tinkering may be required |
| Infinitely extensible | Basic programming/`Python` experience needed |
| Forces good documentation | |
| Insures that core and commonly used functionality is maintained and officially supported | |
| Small core and strict set of 1st party plugins ensures community uses largely compatible/comparable setups

## \#2 Modern

Archimedes is progressive and modern, and does not value backwards compatibility as highly as some other frameworks.

* Even latest stable release may only support the latest Python release (See: [PEP 0602](https://www.python.org/dev/peps/pep-0602/))
* The `master` branch of the source may even require pre-releases of Python (e.g. `3.10` currently)

| Pros ➕ | Cons ➖ |
| --- | --- |
| Your site is always cutting-edge | Latest Python interpreter may not be available in all package managers


## \#3 Opinionated codebase

Archimedes codebase abides by the following set of strict and opinionated rules:

* `isort` import sorting
* `black` code formatting
* `mypy --strict` typing
* `flake8` code style

The end user does not need to be aware of these, but can rest assured that Archimedes maintains a high standard of code.


# Comparison with other frameworks

| | Archimedes | Hugo | Jekyll | Gatsby | Pelican | Nikola |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Programming Language | Python | Go | Ruby | JavaScript | Python | Python |
| Plugin support | ✔ | ❌ | ✔ | ✔ | ✔ | ✔ |
| Theme support | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Native ToC trees | ✔ | ✔ | ❌ | ❌ | ❌ | ❌ |
| Native Markdown support | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Native Jupyter Notebook suport | ✔ | ❌ | ❌ | ❌ | ❌ | ✔ |
| Native reStructuredText support | ❌ | ✔ | ❌ | ✔ | ✔ | ✔ |
| Templating framework | Mako | Go Templates | Liquid | React | Jinja2 | Jinja2, Mako |

# Comparison of Python frameworks
| | Archimedes | Pelican | Nikola |
| --- | :---: | :---: | :---: |
| Typed | ✔ | ❌ | ❌ |


# Why/why not `...`?

Here are some more or less well-reasoned arguments for why to choose Archimedes over other frameworks.

## Hugo

### Why not?

* Hugo is not easily extensible
* Speed does not matter for a Static Site Generator
* Does not have Jupyter Notebook support

### Why?

* Very established
* Large number of beautiful themes available
* Has a more 'just works' approach

---

## Jekyll

### Why not?

### Why?

---

## Gatsby

### Why not?

### Why?

---

## Pelican

### Why not?

### Why?

---

## Nikola

### Why not?

### Why?

# Shoulders of giants

Archimedes uses the following libraries and frameworks behind the scenes:

| Framework/library | Functionality |
| --- | --- |
| Mako | Core templating engine
| Doit | Task execution
