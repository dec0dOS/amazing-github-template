# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
{% if cookiecutter.include_code_of_conduct == 'y' -%}
Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.
{% endif %}
## Development environment setup

> **[?]**
> Proceed to describe how to setup local development environment.
> e.g:

To set up a development environment, please follow these steps:

1. Clone the repo

   ```sh
   git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}
   ```

2. TODO

## Issues and feature requests

You've found a bug in the source code, a mistake in the documentation or maybe you'd like a new feature? You can help us by submitting an issue to our [GitHub Repository](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues). Before you create an issue, make sure you search the archive, maybe your question was already answered.
{% if cookiecutter.use_github_discussions == 'y' -%}
Also please check out [GitHub discussions](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/discussions) before submitting an issue. 
{% endif %}
Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

Even better: You could submit a pull request with a fix or new feature!

## Pull request process

1. Search our repository for open or closed
[pull requests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/pulls)
that relates to your submission. You don't want to duplicate effort.
2. Fork the project
3. Create your feature branch (`git checkout -b feat/amazing_feature`)
4. Commit your changes (`git commit -m 'feat: add amazing_feature'`)
5. Push to the branch (`git push origin feat/amazing_feature`)
6. Open a pull request

{% if cookiecutter.use_conventional_commits == 'y' -%}
{{cookiecutter.project_name}} uses [conventional commits](https://www.conventionalcommits.org), so please follow the specification.
{% endif %}