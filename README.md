
A simple quiz translator of the worpdress plugin Tutor LMS
=======

# Tutor LMS Quiz Translator

This script helps everyone who manage courses using Tutor LMS plugin on WordPress sites.
Whenever you have the need to translate an exported quiz, you have to make sure not change the default csv structure. 
Personally i tried any online services that provides a .csv and .xlsx translation but without success because the original structure changed even if the words themselves were sucessfully translated.
When you are using this script, it will help you translate each word of each questions, only that without touching the quiz csv, in addition it will be created a new csv file translated as the final result (a copy from the original one) ready for the import in your LMS.


## Installation 

It requires Python 3.6+ installed on your Operating System.

Without virtual enviroment

```bash
  git clone https://mygithubrepo.com
  cd translate-tutor-lms-quiz
  pip install -r requirements.txt
```

With virtual enviroment

```bash
  git clone https://mygithubrepo.com
  cd translate-tutor-lms-quiz
  python -m venv quizTranslate
```   

Activate virtual enviroment

```bash
  cd quizTranslate/Scripts
  source activate && cd ../..
  pip install -r requirements.txt628485
```   
## Usage/Examples

You need only to drag and drop your csv file you desire translate file into your CLI when you are using this tool.

Example:

```bash
  python quiz_translate.py "C:\Users\yourusername\Desktop\tutor-quiz-Sample Quiz.csv"
```
It's done you will see a new csv translated file in the same directory of the cloned project.
Now you only need to import/upload the new translated quiz into your tutor lms course and that's pretty much it. 


## Screenshots

[Screenshot]('https://raw.githubusercontent.com/francesco-fortini/tutor-lms-quiz-translator/master/screenshots/original-csv.png')

[Screenshot]('https://raw.githubusercontent.com/francesco-fortini/tutor-lms-quiz-translator/master/screenshots/command-line-interface.png')

[Screenshot]('https://raw.githubusercontent.com/francesco-fortini/tutor-lms-quiz-translator/master/screenshots/translated-csv.png')


