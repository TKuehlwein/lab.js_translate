How to use

1. Make sure all scripts are in the same folder
2. Adjust variables in "translation_GPT_API.py" or "translation_DeepL_API.py" depending on preference
3. Add all .json files to be translated into one working directory
4. Ensure that you have a copy of all .json files, as they will be overwritten
5. Run "translation_GPT_API.py" or "translation_DeepL_API.py"


Knows issues: 

- does not work on fully canvas based experiments
- radio buttons in "HTML Page" are not translated
- contens of .csv files within the experiment will not be translated
- for <img> displays sometimes adds extra space which needs to be removed
  - only when image is in local file storage of experiment, not when on server and .csv file
  
- We overall reccomend having images on your server and reading them in via a .csv file
to be displayed as <img>,this is less prone to errors and reduces the size of your experiment