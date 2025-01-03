from block_markdown import markdown_to_html_node

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


def generate_page(from_path, template_path, dest_path):
    # Print a message like "Generating page from from_path to dest_path using template_path".
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read the markdown file at from_path and store the contents in a variable.
    if os.path.exists(from_path):
        with open(from_path, 'r') as file:
            markdown = file.read()
    else:
        raise Exception(f"From path does not exist: {from_path}")
    # Read the template file at template_path and store the contents in a variable.
    if os.path.exists(template_path):
        with open(template_path, 'r') as file:
            template = file.read()
    else:
        raise Exception(f"From path does not exist: {template_path}")
    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    html_string = markdown_to_html_node(markdown).to_html()
    # Use the extract_title function to grab the title of the page.
    title = extract_title(markdown)
    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    update_title = template.replace("{{ Title }}", title)
    updated_with_content = update_title.replace("{{ Content }}", html_string)

    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    dirs = os.path.dirname(dest_path)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print(f"Made directory: {dirs}")
    with open(dest_path, 'w') as f:
        f.write(updated_with_content)
        print(f"File written to {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Create a generate_pages_recursive(dir_path_content, template_path, dest_dir_path) function. It should:
    # Crawl every entry in the content directory
    content_dir = os.listdir(dir_path_content)

    for file in content_dir:
        content_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(content_path):
            if content_path[-3:] == ".md":
                dest_path = dest_path[:-3] + ".html"
                generate_page(content_path, template_path, dest_path)
        else: # file is a dir
            os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path)
    # For each markdown file found, generate a new .html file using the same template.html.
    # The generated pages should be written to the public directory in the same directory structure.


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


