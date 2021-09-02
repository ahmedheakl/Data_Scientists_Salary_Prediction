# Data Scientists Salary PredictionL: Project Overview
* Created a tool that can predict the salary of data scientists(mean_absolute_error ~ $11K) to negotiate job offers.
* Used selenium to scrape over 1000 jobs from glassdoor website.
* Done features engineering to extract important values (eg. extracting jobs skills like python, aws ... etc. from Job Description).
* Tried Lasso, LinearRegession, Randomforrest models and optimized them using GridSearchCV library.
* Built a client facing API using Flask.

# Resources
* **How I set up the webscraping?:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
* **How I set up the flaskAPI?:**  https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
* **How I wrote this README file?:** https://www.markdownguide.org/cheat-sheet/

# Code and Packages
* **Python Version:** 3.9.6
* **Packages:** Selenium, Pandas, Sk-learn, Numpy, Flask, Requests, Pickle, Matplotlib
* **for Web Framwork Requirements:** In the FlaskAPI directorty run ```pip install -r requirements.txt```

## Web Scraping
I modified the github repo(above), since it wasn't up-to-date, to get over 1000 jobs. For each job, I got acquired the following info:





