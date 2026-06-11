# lab.js_translate
Python scripts for automatic lab.js .json file translation.

These three scripts use a LLM API to translate .json scripts written in lab.js to the target language. Only frontfacing text will be translated. No CSS, HTLM, JS script will be changed

<b> Note that we personally have gotten better results using the OpenAI API compared to the DeepL API. DeepL script left in for completness </b>

Please read "instruction.md" for explanation on how to use the scripts. 

Please note that fully canvas based experiments might not work properly as canvas screens are not translated into JavaScript. 

## Installation and preperation
1. Clone the repository
2.	Install Python
4.	Set up your LLM API key
   
	•	Follow the steps explained by DeepL or OpenAI
5. Download all lab.js experiments you want to translate as .json files via the browser based builder and the "save" function
6. Read instruction.md



Cite as: 

Kühlwein, T, etc. 
