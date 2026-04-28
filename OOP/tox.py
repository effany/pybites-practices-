import configparser

cookiecutter = """[tox]
envlist = py27, py34, py35, py36, pypy, flake8


[testenv]
passenv = LC_ALL, LANG, HOME
commands = pytest --cov=cookiecutter {posargs:tests}
deps = -rtest_requirements.txt

[testenv:flake8]
deps =
    flake8==3.5.0
commands =
    flake8 cookiecutter tests setup.py

[testenv:cov-report]
commands = pytest --cov=cookiecutter --cov-report=term --cov-report=html"""

class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        # self.ini_file = self.config.read_string(ini_file)
        self.ini_file = self.config.read(ini_file)
        self.sections = self.config.sections()


    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/articles/property-decorator
        """
        sections = self.config.sections()
        return len(sections)

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        env_raw = self.config.get("tox", "envlist")
        parts = env_raw.replace("\n", ",").split(",")
        return [p.strip() for p in parts if p.strip()]

    @property
    def base_python_versions(self):
        versions = []
        for sec in self.config.sections():
            if self.config.has_option(sec, "basepython"):
                versions.append(self.config.get(sec, "basepython").strip())
        return sorted(set(versions))

parser = ToxIniParser(cookiecutter)
print(parser.number_of_sections)
print(parser.environments)
print(parser.base_python_versions)