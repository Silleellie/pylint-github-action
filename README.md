# PyLint with badge - GitHub Action

GitHub action that lets you *easily* lint **one** or **multiple** packages of your project and adds a **dynamic badge**
to your `README.md` that lets you display the obtained score!

Each time the action is run, packages specified will be linted and a badge in the `README.md` is updated dynamically
following one of the below rules:

|      Range PyLint score       |                                                          Badge                                                          |
|:-----------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
|     *PyLint score* $< 5$      |  ![pylint-red](https://user-images.githubusercontent.com/26851363/220145659-833c833a-bad1-4251-a88f-75bee908ae40.svg)   |
| $5 \le$ *PyLint score* $< 8$  | ![pylint-orange](https://user-images.githubusercontent.com/26851363/220145963-d4e252e6-c75f-4baf-82ed-b279aba27cfe.svg) |
| $8 \le$ *PyLint score* $< 10$ | ![pylint-yellow](https://user-images.githubusercontent.com/26851363/220146291-f7537aa4-2125-4b5c-b020-3edb0b460e27.svg) |
|     *PyLint score* $= 10$     | ![pylint-green](https://user-images.githubusercontent.com/26851363/220146426-b0250427-0854-402a-9ac8-abe6088a0fdb.svg)  |


The action can be triggered by a **`Pull request`**, a **`Push`** or manually with **`workflow_dispatch`**. 
If the score is changed, the `github_action` bot will change your badge with an automatic commit

* **IMPORTANT!** Follow the ['Preliminary steps' section](#preliminary-steps) in order to allow the bot to update your 
README.md with the pylint badge!


A quick example on how you would typically use this *action* (more examples in [scenario section](#scenario))
```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: src  # lint src package
    python-version: 3.9  # python version which will lint the package
```

## Preliminary steps

To use this action you should perform two simple **first-time-only** operations:

1. In order to have a dynamic updated badge, before using for the first time this action, you should put a ***placeholder
badge*** in your `README.md` which will be substituted by the actual one as soon as you run this action.\
The placeholder badge should be in one of the following formats:
<p align="center"><b><code>![pylint]()</code></b> or <b><code>[![pylint]()](https://redirect/link)</code></b></p>

2. Be sure to set ***write permissions*** to GitHub actions in your repo settings!
You can change it in `Settings > Actions > General`, then go to subsection **Workflow Permissions** and thick the
***Read and write permission*** option

## Usage

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    
    # Path of the package(s) or python file(s) to lint, relative to the repository root. 
    # If more than one package (or python file) should be linted, simply specify all of them 
    # with the multi-line notation like so:
    # lint-path: |
    #   src
    #   other_src
    #   main.py
    #   ...
    # 
    # Required
    lint-path: src
    
    # Version of the Python interpreter which will install all requirements of your project 
    # and lint the package(s) specified with the `package-path` argument
    #
    # Required
    python-version: 3.9

    # Path of the requirements of your project, relative to the repository root. 
    # This can be easily changed in case you have `requirements-dev.txt`
    #
    # Optional, Default: requirements.txt
    requirements-path: requirements.txt
    
    # Path of the README.md to update with the pylint badge, relative to the repository root.
    #
    # Optional, Default: README.md
    readme-path: README.md
```

## Scenario

* [Single package to lint](#single-package-to-lint)
* [Single python file to lint](#single-python-file-to-lint)
* [Multiple packages to lint](#multiple-packages-to-lint)
* [Multiple python files to lint](#multiple-python-files-to-lint)
* [Mix packages and python files to lint](#mix-packages-and-python-files-to-lint)
* [Different path for requirements file](#different-path-for-requirements-file)
* [Different path for README.md file](#different-path-for-readmemd-file)

### Single package to lint

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: src
    python-version: 3.11
```

### Single python file to lint

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: main.py
    python-version: 3.11
```

### Multiple packages to lint

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: |
      src
      app
      other_src/inner_src
    python-version: 3.11
```

### Multiple python files to lint

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: |
      file1.py
      file2.py
      other_src/file3.py
    python-version: 3.11
```

### Mix packages and python files to lint

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: |
      src
      app
      main.py
    python-version: 3.11
```

### Different path for requirements file

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: src
    python-version: 3.11
    requirements-path: requirements/requirements-dev.txt
```

### Different path for README.md file

```yaml
- uses: Silleellie/pylint-github-action@v2
  with:
    lint-path: src
    python-version: 3.11
    readme-path: models/README.md
```

## Credits

This is a composite GitHub action which uses the following godly working actions:

* [actions/checkout](https://github.com/actions/checkout)
* [actions/setup-python](https://github.com/actions/setup-python)
* [EndBug/add-and-commit](https://github.com/EndBug/add-and-commit)

Massive thanks to [shields.io](https://shields.io/), which is used to create the badge!
