"""Worker class for all git-related queries."""

import os

__all__ = ("Gitorama")

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
        self._repo = None
        self._root = None

    @property
    def root(self):
        """The root node of the git repository's data structure."""
        return self._root

    def set_repository(self, repo):
        """
        Add a repository to the worker.

        This will zero out all existing data.
        """
        if not repo:
            return

        if not (isinstance(repo, basestring) and os.path.isdir(repo)):
            print "WARNING: Supplied repository isn't actually one: %s" % repo
            return

        bits = os.path.split(repo)
        if bits[1] == ".git" and os.path.isdir(bits[1]):
            self._repo = bits[0]
            return None

        if ".git" not in os.listdir(repo):
            print "WARNING: Supplied repository isn't actually one: %s" % repo
            return None

        self._repo = repo
        return repo

    def query_repository(self):
        """Query the current Git repository."""
        pass
