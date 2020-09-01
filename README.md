<div align="center">
<h1>djangoReact Template</h1>

[![GitHub issues](https://img.shields.io/github/issues/shubhank-saxena/djangoReact-template?logo=github)](https://github.com/shubhank-saxena/djangoReact-template/issues)
![Size](https://github-size-badge.herokuapp.com/shubhank-saxena/djangoReact-template.svg) ![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/shubhank-saxena/djangoReact-template)

[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/shubhank-saxena/djangoReact-template/blob/master/.pre-commit-config.yaml)
[![License](https://img.shields.io/github/license/shubhank-saxena/djangoReact-template)](https://github.com/shubhank-saxena/djangoReact-template/blob/master/LICENSE)

This is the most convenient starter template of Django+React code with Django serving React and containing all the dependencies required to create django-rest-api
</div>

## Contribution to the project

<div align="center">

[![GitHub issues](https://img.shields.io/github/issues/shubhank-saxena/djangoReact-template?logo=github)](https://github.com/shubhank-saxena/djangoReact-template/issues) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/shubhank-saxena/djangoReact-template?logo=git&logoColor=white)

</div>

### Git workflow

Please follow a systematic Git Workflow -

- Create a fork of this repo.
- Clone your fork of your repo on your pc.
- [Add Upstream to your clone](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)
- **Every change** that you do, it has to be on a branch. Commits on master would directly be closed.
- Make sure that before you create a new branch for new changes,[syncing with upstream](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) is neccesary.

### Commits

- Write clear meaningful git commit messages (Do read [this](http://chris.beams.io/posts/git-commit/)).
- Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check [this](https://github.com/blog/1506-closing-issues-via-pull-requests) for more info)
- When you make very very minor changes to a PR of yours (like for example fixing a failing Travis build or some small style corrections or minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at [here](https://davidwalsh.name/squash-commits-git))
- When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.


## Installation and Setup

### Prerequisites
- You should have NodeJS installed (12.x or above)
- pipenv should be installed in the system. It can be done using `sudo pip3 install pipenv`.
- Change the version of the python in `Pipfile` according to the python version available in your system


### Setup and running of project (Frontend + Backend)

- Fork the repo and clone it.
- Navigate to the cloned repo.
- Run `build_local.sh`. (Make sure it's in executable mode by `sudo chmod +x build_local.sh`)
- Then run `pipenv shell` to activate the environment.
- Start the backend server
  `python backend/app.py`
  
**This runs the backend server at default port `5000`.
  Open [http://localhost:5000](http://localhost:5000) to view it in the browser.**<br />

### Setup and running of project (Only Frontend)

- At your root directory run `yarn install` to install all the dependencies
- To start react dev server `yarn start`

This runs the app in the development mode.
**Open [http://localhost:3000](http://localhost:3000) to view it in the browser.**

The page will reload if you make edits.

## Production grade deployment
This project tried to follow the best practices and you can directly deploy the repo with the following points -

- Create an .env in your deployment environment(refer .env.example file for the same).
    - For django `SECRET_KEY` you can generate one from [here](https://djecrety.ir/)
    - Set DEBUG = 'False' when using in production/live deployment.
- Add the hostname/url(the one on which your deployed server is working) in the `settings.py` file (under allowed hosts array)
- Add your suitable `TIME_ZONE` and `LANGUAGE_CODE` in `settings.py` according to your zone and locale.

#### Note [Important]

- The `manage.py` file is moved out of the default django project. So everytime you run `manage.py startapp app`, it will create the required app in the root of the project. So you will have to move it in the backend folder and while registering the app in `settings.py`, you will have to mention `backend.app`.
- The `config` folder in the backend directory is the actual root project of the django project (one which has django settings and main app urls).
- There is a folder named `demo` in the backend folder. That's a demo api folder for reference.
- This project has pre-commit. So if you are using this project on which a lot of people are contributing, make sure you run `pre-commit install` in the project repo so that git hooks are enabled.
- Stuff you can delete (I added them just to refer)
    - `index.js` and related files in `./src/` and `app.js` and related files in `./src/components/`
    - `demo` folder from `./backend/` 

## Todo
- [ ] Create a CI/CD branch to automate testing (if any)
- [ ] Create a GCP Deployment (both engine and VM) branch
- [ ] Create a Azure deployment branch
- [ ] Create a AWS deployment branch