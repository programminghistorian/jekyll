This document describes how to make _technical_ contributions to _The Programming Historian_ that modify the code that generates the site itself.

If you are interested in making a _content_ contribution like a new lesson, please see our [pages on contributing as an author or an editor](http://programminghistorian.org/contribute).

## Anti-harassment Policy

The *Programming Historian* is dedicated to providing an open scholarly environment that offers community participants the freedom to thoroughly scrutinize ideas, to ask questions, make suggestions, or to requests for clarification, but also provides a harassment-free space for all contributors to the project, regardless of gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age or religion, or technical experience. We do not tolerate harassment or ad hominem attacks of community participants in any form. Participants violating these rules may be expelled from the community at the discretion of the editorial board. If anyone witnesses or feels they have been the victim of the above described activity, please contact our ombudspeople (Ian Milligan and Amanda Visconti - <http://programminghistorian.org/project-team>). Thank you for helping us to create a safe space.

## Setting up a GitHub pages development environment

This site is built via Jekyll, using GitHub Pages as a hosting service. This means that all code in this GitHub repo is processed by GitHub servers to produce the HTML pages that readers see. If you want to preview what this generated site looks like on your own computer, you need to make sure you are using the same versions of Jekyll and its dependencies that GitHub does.

Note: these instructions assume that you hare familiar with using the command line and git.

1. [Set up Jekyll dependencies.](http://programminghistorian.org/lessons/building-static-sites-with-jekyll-github-pages#section2)
2. Clone the programming historian repository
3. Ensure you have the [bundler gem]() installed:
```
gem install bundler
```
4. `cd` into your clone of the PH repository, and install all the necessary dependencies with the command `bundle install`

## 