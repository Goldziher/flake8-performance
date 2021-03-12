"""Holds flake8 plugin class."""
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ast import Module
    from typing import Generator

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version  # pylint: disable=E0401


class Plugin:
    """Flake8 plugin."""

    name = "flake8-performance"
    version = version("flake8-performance")

    __slots__ = ("_tree",)

    def __init__(self, tree: "Module") -> None:
        self._tree = tree

    def run(self) -> "Generator":
        """Run performance checks and yield relevant errors."""
        # TODO: Replace yield with a call to our checker, or equivalent
        yield 1, 0, "error message", None
