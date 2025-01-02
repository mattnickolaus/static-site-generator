import os
import shutil

def extract_title(markdown):
    # Pulls the `h1` header from the markdown file (the line that starts with a single `# `) and return it.
    #  - If there is no `h1` header, raise an exception.
    #  - `extract_title("# Hello")` should return `"Hello"`(strip the `#` and any leading or trailing whitespace)
    markdown_lines = markdown.split("\n")
    for line in markdown_lines:
        if line.startswith("# "):
            return line.strip("# ")
        else:
            raise Exception("Must include h1 or '# ' header")


def delete_and_copy_source_to_destination(source, destination):
    # 1. Delete all contents of destination dir
    if os.path.exists(destination) and os.listdir(destination):
        shutil.rmtree(destination)
        os.mkdir(destination) # rmtree deletes the dir so we remake it
    if not os.path.exists(destination):
        os.makedirs(destination)

    # 2. Recursively copy all files to destination (uses helper func)
    log_list = copy_source_to_destination(source, destination) # <- This runs the copying
    # 3. Logs out path of each copied file
    for log in log_list:
        print(log)

def copy_source_to_destination(source_path_in="", destination_path_in=""):
    current_dir = os.listdir(source_path_in)
    file_paths = []
    for file in current_dir:
        source_path = os.path.join(source_path_in, file)
        destination_path = os.path.join(destination_path_in, file)
        if not os.path.isdir(source_path):
            file_paths.append(f"{source_path}\nCopied to:\n{destination_path}\n---")
            shutil.copy(source_path, destination_path)
        else: # file is a dir
            os.mkdir(destination_path)
            file_paths.append(f"Directory:\n{source_path}\nCopied to:\n{destination_path}\n---")
            file_paths.extend(copy_source_to_destination(source_path, destination_path))
    return file_paths


