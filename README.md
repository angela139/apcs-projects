# AP Computer Science Projects Bot (original version with API)
##### This is a repository for a bot that can get links from student submissions on Google Classroom for my AP Computer Science teacher to post student projects on a Markdown file in Github. 
1. The user needs authorization to use the Google Classroom API. Here is a [Google tutorial](https://developers.google.com/classroom/quickstart/python) to help get started with the process.
2. The program will look through all courses in the user's Google Classroom to find a course with "APCS" in the name.
3. It will retrieve all student names from those classes to be used later for the Markdown file.
4. It looks for the "Starfield" assignment and scrapes the submission link from each student
5. Lastly, it will add all the links along with the student's name to "work.md". 
##### This bot was abandoned, because my school district doesn't allow for teachers to use Google Cloud Platform which is necessary for accessing APIs. The alternative version that bypasses this requirement with Selenium is located in a separate repository, [apcs-gc-bot](https://github.com/angela139/apcs-gc-bot). 

#### This project was made entirely in Python using the Google Classroom API.
