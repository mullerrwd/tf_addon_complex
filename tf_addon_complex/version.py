__MAJOR__ = "0"
__MINOR__ = "0"
__PATCH__ = "0"

__SUFFIX__ = "dev"


__version__ = "{}.{}.{}".format(__MAJOR__, __MINOR__, __PATCH__)


if __SUFFIX__:
    __version__ = "{}_{}".format(__version__, __SUFFIX__)

