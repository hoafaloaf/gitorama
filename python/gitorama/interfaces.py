"""Interfaces for the Gitorama commit viewer."""

import os

from PyQt4 import QtGui

from gitorama.ui import gitorama_ui
from gitorama.worker import Gitorama

__all__ = ("GitoramaWidget", "GitoramaWindow")

###############################################################################
# CLASS: GitoramaWidget


class GitoramaWidget(QtGui.QWidget, gitorama_ui.Ui_gitorama):
    """The Gitorama commit viewer in a widget form."""

    def __init__(self, repository=None):
        """Initialise the instance."""
        super(GitoramaWidget, self).__init__()

        self._initialise()
        self.setupUi(self)

        self.gg.set_repository(repository or ".")

    def _initialise(self):
        """Initialize properties and settings for the class."""
        self.gg = Gitorama()

###############################################################################
# CLASS: GitoramaWindow


class GitoramaWindow(QtGui.QMainWindow):
    """The Gitorama commit viewer in the form of a MainWindow."""

    def __init__(self, repository=None):
        """Initialise the instance."""
        super(GitoramaWindow, self).__init__()

        self.resize(800, 600)
        self.centralWidget = QtGui.QWidget(self)
        self.gitoramaWidget = GitoramaWidget(repository)

        layout = QtGui.QVBoxLayout(self.centralWidget)
        layout.setMargin(4)
        layout.setSpacing(4)
        layout.addWidget(self.gitoramaWidget)
        self.setCentralWidget(self.centralWidget)
