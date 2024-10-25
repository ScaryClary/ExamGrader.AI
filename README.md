# ExamGrader.AI

## Welcome! 
This is the AI exam grader created by Dr. Grant Clary.
The intention for this project is to use AI to assist grading student essay exams.
Below are instructions for installing and running this application.
Basic python knowledge may be required.

## How to use this application
If you need assistance with any of these instructions, please ask an LLM model for help
- ensure you have the latest version of python installed. I'm running 3.14
- clone this repository to your computer, and open it via VS Code
- create a .env file to store your API key
- update the promptOpening.py file with your expectations of how you want your student responses graded
- 
- 
- 
- 

## Preparing student responses
This repository is set up in a way that requires your data to be structured in a certain format.
The expected format is below:
| n | question | answer |
|----------|----------|----------|
| 1 | Question: (question text here) | Answer: (student answer here) |
| 2 | Question: (question text here) | Answer: (student answer here) |
| 3 | Question: (question text here) | Answer: (student answer here) |

In the example above, each row consists of one question, and one answer.
If a student has been given multiple questions (e.g., 5 essay questions on the exam), the student's answer will be spread across several rows (e.g., first 5 rows are student 1).
Column n allows for student annonymity. In a seperate (university provided) computer, a table should have student data to connect each response back to the correct student.
pdf in folder for more clear demonstration.

