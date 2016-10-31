"""Gitorama: A little tool for visualizing Git commits."""

import sys

__all__ = ("get_widget", "get_window")

##############################################################################
# EXPORTED METHODS


def get_widget(repository=None):
    """Return an initialised GitoramaWidget instance."""
    from interfaces import GitoramaWidget
    return GitoramaWidget(repository)


def get_window(repository):
    """Return an initialised GitoramaWindow."""
    from interfaces import GitoramaWindow
    return GitoramaWindow(repository)
