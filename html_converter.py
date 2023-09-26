import os
os.chdir(r'/Users/guille/GitHub/guillevzn.github.io')
os.system('Jupyter nbconvert cv.ipynb --to html --HTMLExporter.theme=light --no-input --no-prompt')