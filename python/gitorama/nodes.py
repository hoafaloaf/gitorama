"""Nodes used by the worker class to store Git commit data."""

__all__ = ("CommitNode", "InfoNode", "RepositoryNode")

###############################################################################
# CLASS: BaseNode


class BaseNode(object):
    """Base node for git commit-related data."""

    _TYPE = "base"

    def __init__(self, parent=None):
        """Initialise the instance."""
        self.children = list()
        self.child_dict = dict()
        self.parent = parent

    @property
    def node_type(self):
        """Return the type of the node."""
        return self._TYPE

    def add_child(self, child):
        """Add a child node to the instance."""
        self.children.append(child)

###############################################################################
# CLASS: RepositoryNode


class RepositoryNode(BaseNode):
    """Node representing an individual Git commit."""

    _TYPE = "repository"

    def __init__(self, parent=None):
        """Initialise the instance."""
        super(RepositoryNode, self).__init__(parent=parent)

###############################################################################
# CLASS: CommitNode


class CommitNode(BaseNode):
    """Node representing an individual Git commit."""

    _TYPE = "commit"

    def __init__(self, parent=None):
        """Initialise the instance."""
        super(CommitNode, self).__init__(parent=parent)

###############################################################################
# CLASS: InfoNode


class InfoNode(BaseNode):
    """Node representing an individual Git commit's details."""

    _TYPE = "info"

    def __init__(self, parent=None):
        """Initialise the instance."""
        super(InfoNode, self).__init__(parent=parent)
