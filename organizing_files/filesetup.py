import os
import sys
import shutil

operator_name = input('Operator name: ')
print(os.getcwd())
import_data = ''
import_violations = ''
print(os.path.exists('.'))
print(os.path.dirname(os.getcwd()))
migration_repo = os.path.dirname(os.getcwd())



# TODO get operator id and info

# TODO create directory, put everything in it
os.makedirs(f'{os.getcwd()}/temp_{operator_name}/setup')
# TODO make import directories and files

# TODO move files from temp dir into new ones, erase

# TODO create git repo 
# set branch to develop
# checkout new branch
# commit assets
# push
# return git repo mr