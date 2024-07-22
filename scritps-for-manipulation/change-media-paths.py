import os

def replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    new_content = content.replace('![](../', '![](')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def replace_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing markdown files: ")
    replace_in_folder(folder_path)
    print("Replacement complete.")
