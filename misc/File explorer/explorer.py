import os
dictionary_files = {}
stack_folders = []

# ls -d */ ||only folders
# ls -p | grep -v / ||files only

def get_sub_folders(current_dir):
    data = ""
    folders = os.popen("ls -d */").read()

    list_folders = folders.split('\n')
    for folder in list_folders:
        # print(folder,",")
        stack_folders.append(folder)
    return list_folders

def show_files(current_dir):
    pwd = os.popen('pwd').read()
    pwd = pwd.split('/')
    print(pwd[-1])
    print(current_dir,"-----")

    if(pwd[-1]!=current_dir):
        change = "cd "+current_dir
        aa = os.popen(change).read()
        print(os.popen('pwd').read(),"++++")
    
    files = os.popen("ls -p | grep -v /").read()

    list_files = files.split('\n')
    list_files.pop()
    for file in list_files:
        if '.' not in file:
            stack_folders.append(file)
    dictionary_files[current_dir] = list_files

# show_files('main')
# print(dictionary_files)

def call_all_folders(current_dir):

    get_sub_folders(current_dir)
    
    while(stack_folders):
        show_files(stack_folders[-1])
        stack_folders.pop()

call_all_folders('main')        
print(dictionary_files)
