"""Interfaces for the Gitorama commit viewer."""

# from functools import partial

import os

from PySide import QtCore, QtGui

from gitorama.gui.ui import gitorama_ui
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

        self.setup_main_interface()
        self.set_repository(repository or ".")

    def _initialise(self):
        """Initialize properties and settings for the class."""
        self.gg = Gitorama()

    def setup_main_interface(self):
        """Setup the interface, connect signals/slots."""
        pixmap = QtGui.QPixmap(":/icons/folder_black.png")
        icon = QtGui.QIcon()
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.browserButton.setIcon(icon)
        self.browserButton.setIconSize(QtCore.QSize(24, 24))
        self.browserButton.clicked.connect(self.launch_file_browser)

        self.repositoryLineEdit.editingFinished.connect(self.set_repository)

        self.progress_bar = QtGui.QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)

        self.status_bar = QtGui.QStatusBar(self)
        self.status_bar.addPermanentWidget(self.progress_bar)
        self.mainLayout.addWidget(self.status_bar)

    ###########################################################################
    # CALLBACKS

    def launch_file_browser(self):
        """Launch file browser for git repository selection."""
        current_path = "."
        if self.gg.repository:
            current_path = os.path.dirname(
                os.path.normpath(self.gg.repository.path))

        dialog = QtGui.QFileDialog(self, directory=current_path)
        dialog.setFileMode(dialog.DirectoryOnly)
        repo_path = str(dialog.getExistingDirectory(self, "Select Directory"))

        return self.set_repository(repo_path or current_path)

    def set_repository(self, file_path=None):
        """Set the interface's repository."""
        if file_path is None:
            file_path = str(self.repositoryLineEdit.text())

        file_path = str(file_path)
        if not os.path.isdir(file_path):
            file_path = os.path.dirname(file_path)

        repo = self.gg.set_repository(file_path)
        if repo:
            file_path = os.path.dirname(os.path.normpath(repo.path))

        self.repositoryLineEdit.blockSignals(True)
        self.repositoryLineEdit.setText(file_path)
        self.repositoryLineEdit.blockSignals(False)

        return repo


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
        layout.setSpacing(4)
        layout.addWidget(self.gitoramaWidget)
        self.setCentralWidget(self.centralWidget)

        self.gitoramaWidget.cancelButton.clicked.connect(self.close)
