import os

def get_files_info(working_directory, directory=None):
    try:
      abs_working_dir = os.path.abspath(working_directory)
      full_path = os.path.abspath(os.path.join(working_directory, directory))

      if not full_path.startswith(abs_working_dir):
          return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

      if not os.path.isdir(full_path):
          return f'Error: "{directory}" is not a directory'

      result = []
      for file in os.listdir(full_path):
        file_path = os.path.join(full_path, file)
        if os.path.isdir(file_path):
          size = get_dir_size(file_path)
          result.append(f'- {file}: file_size={size} bytes, is_dir=True')
        else:
          result.append(f'- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir=False')
      return '\n'.join(result)
    except Exception as e:
      return f'Error: {e}'

def get_file_content(working_directory, file_path):
    try:
      abs_working_dir = os.path.abspath(working_directory)
      full_path = os.path.abspath(os.path.join(working_directory, file_path))
      if not os.path.commonpath([full_path, abs_working_dir]) == abs_working_dir:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

      if not os.path.isfile(full_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')

      with open(full_path, 'r') as file:
        content = file.read()
        print(len(content))
        if len(content) > 10000:
          file_content_string = content[:10000]
          return f'{file_content_string} [...File "{file_path}" truncated at 10000 characters]'
        else:
          return content
    except Exception as e:
      return f'Error: {e} '

def write_file(working_directory, file_path, content):
  try:
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.commonpath([full_path, abs_working_dir]) == abs_working_dir:
      print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    if not os.path.exists(full_path):
      #create the file
      f = open(full_path, 'x')
      f.write(content)
    else:
      #overwrite the file
      f = open(full_path, 'w')
      f.write(content)
      f.close()

    return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
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



