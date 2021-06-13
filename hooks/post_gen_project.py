#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove(filepath):
    fullpath = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.isfile(fullpath):
        os.remove(fullpath)
    else:
        shutil.rmtree(fullpath, ignore_errors=True)


if __name__ == "__main__":
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove(".github/workflows/codeql.yml")  # codeql is available for free only for OSS
        remove("LICENSE")

    if "{{ cookiecutter.include_logo }}" != "y":
        remove("docs/images/logo.svg")

    if "{{ cookiecutter.include_screenshots }}" != "y":
        remove("docs/images/screenshot.png")

    if "{{ cookiecutter.include_security }}" != "y":
        remove("docs/SECURITY.md")

    if "{{ cookiecutter.include_code_of_conduct }}" != "y":
        remove("docs/CODE_OF_CONDUCT.md")

    if "{{ cookiecutter.include_workflows }}" != "y":
        remove(".github/workflows")
        remove(".github/labels.yml")

    if "{{ cookiecutter.use_github_discussions }}" == "y":
        remove(".github/ISSUE_TEMPLATE/04_SUPPORT_QUESTION.md")

    if "{{ cookiecutter.use_codeql }}" != "y":
        remove(".github/workflows/codeql.yml")