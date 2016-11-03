"""Gitorama: A little tool for visualizing Git commits."""

import pygit2
import os

__all__ = ("discover_repository", "get_widget", "get_window")

##############################################################################
# EXPORTED METHODS


def discover_repository(repo):
    """Return repository (if any) at the provided location."""
    if not repo:
        return None

    if not (isinstance(repo, basestring) and os.path.isdir(repo)):
        print "WARNING: Supplied repository isn't actually one: %s" % repo
        return

    try:
        repo = pygit2.discover_repository(repo)
    except:
        return None

    return pygit2.Repository(repo)


def get_widget(repository=None):
    """Return an initialised GitoramaWidget instance."""
    from gui.interfaces import GitoramaWidget
    return GitoramaWidget(repository)


def get_window(repository):
    """Return an initialised GitoramaWindow."""
    from gui.interfaces import GitoramaWindow
    return GitoramaWindow(repository)
