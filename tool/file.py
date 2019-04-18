"""Read/write data files."""
import array
import os
import typing

from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string(
  'data_folder_name', 'data',
  'What folder name to use to save data.')


def GetProjectRootPath() -> str:
  return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def GetCacheDirPath(cache_type_id: str) -> str:
  return os.path.join(GetProjectRootPath(), 'cache', cache_type_id)


def GetDataDirPath(sub_dir: str = '') -> str:
  return os.path.join(GetProjectRootPath(), FLAGS.data_folder_name, sub_dir)


def Read(filepath: str) -> str:
  """Reads a data file."""
  filepath_full = os.path.join(GetDataDirPath(), filepath)
  return open(filepath_full).read()


def Write(
    filepath: str,
    content: typing.Union[str, bytes, array.ArrayType]) -> None:
  """Writes to a data file.

  Args:
    filepath: the relative path of the file. Subdirectories will be created.
    content: the content to write to the file.
  """
  if isinstance(content, str):
    mode = 'w'
  elif isinstance(content, bytes) or isinstance(content, array.ArrayType):
    mode = 'wb'
  else:
    raise RuntimeError('unknown content type: %s', type(content))
  filepath_full = os.path.join(GetDataDirPath(), filepath)
  directory = os.path.dirname(filepath_full)
  os.makedirs(directory, exist_ok=True)
  open(filepath_full, mode).write(content)
