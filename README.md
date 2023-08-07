# samplepytest

Python API test using pytest & Pytest BDD

Test Automation framework is designed based on behavioral-driven development(BDD). BDD approach is implemented using the Pytest-BDD plugin. i.e pytest-bdd implements a subset of the Gherkin language to enable automating project requirements testing and to facilitate behavioral-driven development.

This is a 3 Layer Framework with :
   -  Step Definitions
   - Request Classes
   - Payload classes

How to use?

- Clone the repo
- Install Python 3.10 ( if a different version update it in pipfile)
- Install pipenv ( _pip install pipenv_ )
  - Once you’ve done that, you can effectively forget about pip since Pipenv essentially acts as a replacement. It also introduces two new files, the Pipfile (which is meant to replace requirements.txt) and the Pipfile.lock (which enables deterministic builds).
- Then Create a virtual environment for the project (_pipenv shell_)
  - This will create a virtual environment if one doesn’t already exist. Pipenv creates all your virtual environments in a default location (eg in mac: /Users/{user_name}/.local/share/virtualenvs)
  - _pipenv sync_ is an optional command. If you still failed to point the virtual environment then you can install packages exactly as specified in Pipfile.lock using the sync command
- Generate the pipfile.lock (_pipenv lock_)
- Install the dependencies from pipenv lock (pipenv install)


Notes:
Test Data Management:
Test data can be passed as inline parameters in a feature file (eg: _When user pass location as "London"_ )
This can be done without having quotes around the parameter from  bdd==6.0.1 onwards
Also Test data can be passed by using Examples & Scenario Outline.  (eg: _When user pass location as <Location>_)

Examples:

| Location            |

|          London    |

|          Manchester  |

