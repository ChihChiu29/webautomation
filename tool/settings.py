"""Global settings and related helper functions."""

from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_boolean(
    'run', None,
    'The URL of the Google slides, in presentation mode.')


def RunInDocker() -> bool:
    """If the current program runs in a Docker container."""
    return os.path.exists('/.dockerenv')
