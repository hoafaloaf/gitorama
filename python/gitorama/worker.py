"""Worker class for all git-related queries."""

from gitorama import discover_repository
from gitorama.nodes import RepositoryNode

__all__ = ("Gitorama",)

###############################################################################
# CLASS: Gitorama


class Gitorama(object):
    """Worker class used to query Git repositories."""

    def __init__(self, repository=None):
        """Initialise the instance."""
        self._initialise()

        self.set_repository(repository)

    def _initialise(self):
        """Initialise basic properties and attributes on the instance."""
        self._root = None

    @property
    def repository(self):
        """Return the current repository."""
        return self.root.repository

    @repository.setter
    def repository(self, val):
        self.set_repository(val)

    @property
    def root(self):
        """The root node of the git repository's data structure."""
        return self._root

    def set_repository(self, repo):
        """
        Add a repository to the worker.

        This will zero out all existing data.
        """
        repo = discover_repository(repo)
        self._root = None
        if repo:
            self._root = RepositoryNode(repo)

        return self._root


###############################################################################
# INTERNAL METHODS


def _get_commit_count_cmd():
    """Return command used to count commits in a repository."""
    return "git rev-list --all --count"
