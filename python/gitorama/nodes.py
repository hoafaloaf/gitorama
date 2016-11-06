"""Nodes used by the worker class to store Git commit data."""

import pygit2

from gitorama import discover_repository

__all__ = ("CommitNode", "InfoNode", "RepositoryNode")

###############################################################################
# CLASS: BaseNode


class BaseNode(object):
    """Base node for git commit-related data."""

    _TYPE = "base"

    def __init__(self, parent=None):
        """Initialise the instance."""
        self.children = list()
        self.parent = parent

        self._repo = None

    @property
    def child_dict(self):
        """Return dictionary of children, indexed by name."""
        return dict((x.name, x) for x in self.children)

    @property
    def node_type(self):
        """Return the type of the node."""
        return self._TYPE

    @property
    def repository(self):
        """Return the repository associated with the node."""
        return self._repo

    def add_child(self, child):
        """Add a child node to the instance."""
        self.children.append(child)
        child.parent = self


###############################################################################
# CLASS: RepositoryNode


class RepositoryNode(BaseNode):
    """Node representing an individual Git commit."""

    _TYPE = "repository"

    def __init__(self, repo=None, parent=None):
        """Initialise the instance."""
        super(RepositoryNode, self).__init__(parent=parent)
        self.repository = repo

    @property
    def repository(self):
        """Return the repository associated with the node."""
        return self._repo

    @repository.setter
    def repository(self, val):
        self._repo = val
        if isinstance(val, pygit2.Repository):
            self._repo = val
        else:
            self._repo = discover_repository(val)


###############################################################################
# CLASS: CommitNode


class CommitNode(BaseNode):
    """Node representing an individual Git commit."""

    _TYPE = "commit"

    def __init__(self, parent=None):
        """Initialise the instance."""
        super(CommitNode, self).__init__(parent=parent)

    @property
    def repository(self):
        """Return the repository associated with the node."""
        if self.parent:
            return self.parent.repository
        return self._repo


###############################################################################
# CLASS: InfoNode


class InfoNode(BaseNode):
    """Node representing an individual Git commit's details."""

    _TYPE = "info"

    def __init__(self, parent=None):
        """Initialise the instance."""
        super(InfoNode, self).__init__(parent=parent)
