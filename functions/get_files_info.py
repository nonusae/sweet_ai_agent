import os

def get_files_info(working_directory, directory=None):
  try:
    # Convert to absolute paths and resolve any .. or . components
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    # Security check: ensure the resolved path is within the working directory
    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    # Build string represent content of dir with this format Filname: file_size= , is_dir=
    result = []
    for file in os.listdir(full_path):
      # Skip special directory entries
      # if file in ['.', '..']:
      #   continue
      file_path = os.path.join(full_path, file)
      if os.path.isdir(file_path):
        # print (f'File: {file}#')
        size = get_dir_size(file_path)
        result.append(f'- {file}: file_size={size} bytes, is_dir=True')
      else:
        # print (f'File: {file}')
        result.append(f'- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir=False')
    return '\n'.join(result)
  except Exception as e:
    return f'Error: {e}'


def get_dir_size(dir_path):
  total_size = 0
  for file in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file)
    if os.path.isdir(file_path):
      total_size += get_dir_size(file_path)
    else:
      total_size += os.path.getsize(file_path)
  return total_size



