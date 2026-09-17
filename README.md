<div align="center">
    <h1 align="center">collective.tinymceplugins.icons</h1>
</div>
<div align="center">

[![PyPI](https://img.shields.io/pypi/v/collective.tinymceplugins.icons)](https://pypi.org/project/collective.tinymceplugins.icons/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/collective.tinymceplugins.icons)](https://pypi.org/project/collective.tinymceplugins.icons/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/collective.tinymceplugins.icons)](https://pypi.org/project/collective.tinymceplugins.icons/)
[![PyPI - License](https://img.shields.io/pypi/l/collective.tinymceplugins.icons)](https://pypi.org/project/collective.tinymceplugins.icons/)
[![PyPI - Status](https://img.shields.io/pypi/status/collective.tinymceplugins.icons)](https://pypi.org/project/collective.tinymceplugins.icons/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/collective.tinymceplugins.icons)](https://pypi.org/project/collective.tinymceplugins.icons/)

[![CI](https://github.com/collective/collective.tinymceplugins.icons/actions/workflows/main.yml/badge.svg)](https://github.com/collective/collective.tinymceplugins.icons/actions/workflows/main.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/collective/collective.tinymceplugins.icons)](https://github.com/collective/collective.tinymceplugins.icons)
[![GitHub Repo stars](https://img.shields.io/github/stars/collective/collective.tinymceplugins.icons?style=social)](https://github.com/collective/collective.tinymceplugins.icons)

</div>

A TinyMCE plugin that lets the end-user insert icons registered in Plone as part of the text

## Features

- **TinyMCE Plugin**: A native TinyMCE plugin to browse and insert icons.
- **Icon Discovery**: Automatically discovers icons registered in the Plone registry (`plone.icon.*`).
- **Searchable Grid**: Search and live-filter icons in a visual grid within the editor dialog.
- **Live Preview**: Icons are inserted as `<img>` tags pointing to `@@iconresolver`, providing an immediate visual representation while editing.
- **Inline SVGs**: A global `plone.outputfilter` automatically transforms the placeholders into high-quality inline SVGs in the final page rendering.
- **HTML Filter Support**: Automatically configures the Plone HTML filter to allow SVG tags and attributes.
- **Easy Installation**: Self-configuring TinyMCE settings via a setuphandler, including automatic toolbar registration.
- **Clean Uninstall**: Complete uninstall profile that reverts all registry and TinyMCE changes.

## Installation

Install collective.tinymceplugins.icons with `pip`:

```shell
pip install collective.tinymceplugins.icons
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/collective/collective.tinymceplugins.icons/issues)
- [Source code](https://github.com/collective/collective.tinymceplugins.icons/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/collective.tinymceplugins.icons.git
    cd collective.tinymceplugins.icons
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (2.0.0)](https://github.com/plone/cookieplone) and [cookieplone-templates (4d90eb9)](https://github.com/plone/cookieplone-templates/commit/4d90eb9e774e500c643a0aabb140b3a158437a25) on 2026-09-17 13:49:01.525715. A special thanks to all contributors and supporters!
