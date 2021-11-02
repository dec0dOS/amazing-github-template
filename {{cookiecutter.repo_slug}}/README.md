{%- if cookiecutter.modern_header == 'y' -%}
{%- if cookiecutter.include_logo == 'y' -%}
<h1 align="center">
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}">
    <!-- Please provide path to your logo here -->
    <img src="docs/images/logo.svg" alt="Logo" width="100" height="100">
  </a>
</h1>
{% endif %}
<div align="center">
  {{cookiecutter.project_name}}
  <br />
  <a href="#about">
  {%- if cookiecutter.include_screenshots == 'y' -%}
  <strong>Explore the screenshots »</strong>
  {%- else -%}
  <strong>Explore the docs »</strong>
  {%- endif -%}
  </a>
  <br />
  <br />
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  {%- if cookiecutter.use_github_discussions == 'y' -%}
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/discussions">Ask a Question</a>
  {%- elif cookiecutter.use_github_discussions != 'y' %}
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
  {%- endif %}
</div>
{%- else -%}
# {{cookiecutter.project_name}}

> **[?]** 
> Provide short description for your project here.

{%- endif %}
{% if cookiecutter.include_badges == 'y' -%}
{%- if cookiecutter.modern_header == 'y' %}
<div align="center">
{%- endif %}
<br />

[![Project license](https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by {{cookiecutter.github_username}}](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-{{cookiecutter.github_username}}-ff1414.svg?style=flat-square)](https://github.com/{{cookiecutter.github_username}})

{% if cookiecutter.modern_header == 'y' -%}
</div>
{%- endif %}
{% endif %}
{% if cookiecutter.include_toc == 'y' -%}
<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
{%- if cookiecutter.include_project_assistance == 'y' %}
- [Project assistance](#project-assistance)
{%- endif %}
- [Contributing](#contributing)
{%- if cookiecutter.include_authors == 'y' %}
- [Authors & contributors](#authors--contributors)
{%- endif %}
{%- if cookiecutter.include_security == 'y' %}
- [Security](#security)
{%- endif %}
{%- if cookiecutter.open_source_license != 'Not open source' %}
- [License](#license)
{%- endif %}
{%- if cookiecutter.include_acknowledgements == 'y' %}
- [Acknowledgements](#acknowledgements)
{%- endif %}

</details>
{%- endif %}

---

## About
{% if cookiecutter.table_in_about == 'y' %}
<table><tr><td>
{% endif %}
> **[?]**
> Provide general information about your project here.
> What problem does it (intend to) solve?
> What is the purpose of your project?
> Why did you undertake it?
> You don't have to answer all the questions -- just the ones relevant to your project.

{% if cookiecutter.include_screenshots == 'y' -%}
<details>
<summary>Screenshots</summary>
<br>

> **[?]**
> Please provide your screenshots here.

|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>
{%- endif %}
{% if cookiecutter.table_in_about == 'y' %}
</td></tr></table>
{% endif %}
### Built With

> **[?]**
> Please provide the technologies that are used in the project.

## Getting Started

### Prerequisites

> **[?]**
> What are the project requirements/dependencies?

### Installation

> **[?]**
> Describe how to install and get started with the project.

## Usage

> **[?]**
> How does one go about using it?
> Provide various use cases and code examples here.

## Roadmap

See the [open issues](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

> **[?]**
> Provide additional ways to contact the project maintainer/maintainers.

Reach out to the maintainer at one of the following places:

{% if cookiecutter.use_github_discussions == 'y' -%}
- [GitHub Discussions](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/discussions)
{%- elif cookiecutter.use_github_discussions != 'y' -%}
- [GitHub issues](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
{%- endif %}
- Contact options listed on [this GitHub profile](https://github.com/{{cookiecutter.github_username}})

{% if cookiecutter.include_project_assistance == 'y' -%}
## Project assistance

If you want to say **thank you** or/and support active development of {{cookiecutter.project_name}}:

- Add a [GitHub Star](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}) to the project.
- Tweet about the {{cookiecutter.project_name}}.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make {{cookiecutter.project_name}} **better**!
{% endif %}
## Contributing

{% if cookiecutter.open_source_license != 'Not open source' -%}
First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.
{% endif %}

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

{% if cookiecutter.include_authors == 'y' -%}
## Authors & contributors

The original setup of this repository is by [{{cookiecutter.full_name}}](https://github.com/{{cookiecutter.github_username}}).

For a full list of all authors and contributors, see [the contributors page](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_slug}}/contributors).
{% endif %}
{% if cookiecutter.include_security == 'y' -%}
## Security

{{cookiecutter.project_name}} follows good practices of security, but 100% security cannot be assured.
{{cookiecutter.project_name}} is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._
{% endif %}
{% if cookiecutter.open_source_license != 'Not open source' -%}
## License

This project is licensed under the **{{cookiecutter.open_source_license}}**.

See [LICENSE](LICENSE) for more information.
{% endif %}
{% if cookiecutter.include_acknowledgements == 'y' -%}
## Acknowledgements

> **[?]**
> If your work was funded by any organization or institution, acknowledge their support here.
> In addition, if your work relies on other software libraries, or was inspired by looking at other work, it is appropriate to acknowledge this intellectual debt too.
{% endif %}