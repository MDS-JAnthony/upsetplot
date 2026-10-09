#!/usr/bin/env python

import os
import sys

from setuptools import setup


def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    try:
        os.environ["__IN-SETUP"] = "1"  # ensures only version is imported
        from upsetplot import __version__ as version

        # See also setup.cfg
        setup(
            name="UpSetPlot",
            version=version,
            packages=["upsetplot"],
            license="BSD-3-Clause",
            extras_require={"testing": ["pytest>=2.7", "pytest-cov"]},
            # TODO: check versions
            install_requires=["pandas>=3.0.0", "matplotlib>=3.0.0"],
        )
    finally:
        del sys.path[0]
        os.chdir(old_path)
    return


if __name__ == "__main__":
    setup_package()
