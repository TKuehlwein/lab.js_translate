# lab.js_translate

Python scripts for automatic translation of lab.js `.json` files.

These scripts use a translation API or LLM API to translate `.json` files created with lab.js into a target language. Only front-facing text will be translated. CSS, HTML, and JavaScript code will not be changed.

<b>Note that, in our experience, the OpenAI API produces better results than the DeepL API. The DeepL script is included for completeness.</b>

As the translation is performed using a translation API or LLM, the results may not always be perfect. Please make sure that someone fluent in the target language checks the translated files for possible errors.

Please read `instruction.md` for an explanation of how to use the scripts.

Please note that fully canvas-based experiments may not work properly, as canvas screens are not translated into JavaScript.

## Installation and preparation

1. Clone the repository.
2. Install Python.
3. Set up your translation API or LLM API key.

   * Follow the steps provided by DeepL or OpenAI.
4. Download all lab.js experiments you want to translate as `.json` files using the browser-based builder and the “save” function.
5. Read `instruction.md`.

## Citation

Cite as:

Kühlwein, T., etc.

Correspondence concerning this GitHub repository should be addressed to Tobias Kühlwein,
UniDistance Suisse, Schinerstrasse 18, 3900 Brig, Switzerland.
E-mail: [kuehlweintobias@gmail.com](mailto:kuehlweintobias@gmail.com)
