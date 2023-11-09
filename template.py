import os
import logging
from pathlib import Path

#logging.basicConfig(format='%(asctime)s %(message)s', encoding='utf-8', level=logging.INFO)
#logging.basicConfig(format='%(asctime)s: %(message)s', encoding='utf-8', level=logging.INFO)
logging.basicConfig(   
        level = logging.INFO,  
       format = '%(levelname)s:%(asctime)s:%(message)s')
projectname = 'CementStrength'
files = ['.github/workflows.gitkeep',
        
         f'src/{projectname}/__init__.py',
         f'src/{projectname}/components/__init__.py',
         f'src/{projectname}/utils/__init__.py',
         f'src/{projectname}/config/__init__.py',
         f'src/{projectname}/pipelines/__init__.py',
         f'src/{projectname}/constants/__init__.py',
         f"src/{projectname}/entity/__init__.py",
         'config/config.yml',
         'requirements.txt',
         'params.yml',
         'setup.py',
         'reasearch/trials.ipynb'


         ]
for filepath in files:
    filepath = Path(filepath)
    dir_name,filename = os.path.split(filepath)

    if dir_name != "":
        os.makedirs(dir_name,exist_ok=True)
        logging.info(f'Firectory created: {dir_name} for file: {filename}')
    if (not os.path.exists(filepath)) or os.path.getsize(filepath)==0:
        with open(filepath,'w') as f:
            pass
            logging.info(f'emplty file created: {filename}')
    else:
        logging.info(f'file {filename} already existed')    