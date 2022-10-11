from setuptools import setup

setup(
    use_scm_version={
        "root": "..",
        "relative_to": __file__,
        "version_scheme": "no-guess-dev",
    }
)
