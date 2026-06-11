How to use

1. Make sure all scripts are in the same folder.
2. Adjust the variables in "translation_GPT_API.py" or "translation_DeepL_API.py", depending on your preference.
3. Adjust all sections in the script marked with # TODO.
4. Add all .json files to be translated to one working directory.
5. Ensure that you have a copy of all .json files, as they will be overwritten.
6. Run "translation_GPT_API.py" or "translation_DeepL_API.py".


Known issues

- The script does not work on fully canvas-based experiments.
- Radio buttons in "HTML Page" are not translated.
- Contents of .csv files within the experiment will not be translated.
- For "<img>" displays, the script sometimes adds extra spaces that need to be removed manually.
  - This only occurs when the image is stored in the experiment's local file storage, not when the image is stored on a server and referenced via a .csv file.

- Overall, we recommend storing images on your server and referencing them via a .csv file to be displayed as "<img>". This is less prone to errors and reduces the size of your experiment.