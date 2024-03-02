# Browser Automation with SeleniumBase
A page object model (POM) example using SeleniumBase (a Python Framework utilizing Pytest) for the page - https://www.saucedemo.com/

## Pre Requisites
Install the following needed applications
- [Python (3.11)](https://www.python.org/downloads/) - Language
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) or [Visual Studio](https://code.visualstudio.com/download) - IDE


  ### Plugins
  API, Framework, and minimum plugins or libraries to install

  | Title | Description        | Installation                             | Notes |
  |--------|------------------------------------------|-------------------------------|---|
  | [seleniumbase](https://seleniumbase.io/) | API | ```pip install seleniumbase```           |
  | [autopep8](https://pypi.org/project/autopep8/) | plugin | ```pip install autopep8 ```              | Automatically formats Python code to conform to PEP 8 style guide|
  | [flake8](https://pypi.org/project/flake8/) | plugin | ```pip install flake8 ```                | Tests your code for errors against the PEP 8 style guide|


## Running Test

- Open Terminal and run pytest from project directory:
C:\sbase-pom-sample> pytest .tests\<testcase1_name> .tests\<testcase2_name> <...>
OR
python -m pytest .tests\
- Html report will be generated under the reports folder

## References
- [SeleniumBase GitHub](https://github.com/seleniumbase/SeleniumBase)
- [Selenium with Python](https://selenium-python.readthedocs.io/page-objects.html)
- [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)
- [Best Selenium Practice Websites in 2023](https://bugbug.io/blog/software-testing/best-selenium-practice-websites/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

