from generate_static import delete_and_copy_source_to_destination,generate_page

dir_path_static = "../static"
dir_path_public = "../public"

def main():
    # delete_and_copy_source_to_destination(dir_path_static,dir_path_public)
    delete_and_copy_source_to_destination("/home/mattn/workspace/github.com/mattnickolaus/static-site-generator/static",
                                      "/home/mattn/workspace/github.com/mattnickolaus/static-site-generator/public")

    generate_page("/home/mattn/workspace/github.com/mattnickolaus/static-site-generator/content/index.md", "/home/mattn/workspace/github.com/mattnickolaus/static-site-generator/template.html", "/home/mattn/workspace/github.com/mattnickolaus/static-site-generator/public/index.html")

main()