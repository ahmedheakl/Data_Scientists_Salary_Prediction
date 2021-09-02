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
  *	Job title
  *	Salary Estimate
  *	Job Description
  *	Rating
  *	Company 
  *	Location
  *	Company Headquarters 
  *	Company Size
  *	Company Founded Date
  *	Type of Ownership 
  *	Industry
  *	Sector
  *	Revenue
  *	Competitors 

## Data Cleaning
After scraping, the data had to be ready for the model usages. Hence, I made the following changes: 
  * Dropped the rows with no job salaries
  * Parsed the salary by getting rid of "Glassdoor est.", the dollar sign, and the 'K' letter.
  * Extracted *per_hour* and *employer provided* columns from *Salary Estimate* column
  * Extracted the *min_salary*, *max_salary*, and *avg_salary*, which will be our target column.
  * Parsed *Company Names* to get rid of the rating, to a new *company_txt* column.
  * Parsed *Location* to include only the two letter code for the city, to *job_state* column
  * Checked whether the *Location* is the same as the *Headquarters*, to a new *same_state* column
  * Extracted *age* column (years since the country was founded till now) from *Founded* column
  * Made columns for if different skills were listed in the *Job Description*:
    * Python  
    * Tableau  
    * Excel  
    * AWS  
    * Spark 
  *	Column for simplified job title and Seniority 
  *	Column for description length
## Exploratory Data Analysis
I looked at the distribution to have an idea how the data are organized and how they are distributed to take hint of what model would be suitable. Below are a few highlights:


![alt text](https://github.com/ahmedheakl/Data_Scientists_salary_prediction/blob/main/salary_by_job_title.PNG "Salary by Position")
![alt text](https://github.com/ahmedheakl/Data_Scientists_salary_prediction/blob/main/positions_by_state.png "Job Opportunities by State")
<p align="center">
![alt text](https://github.com/ahmedheakl/Data_Scientists_salary_prediction/blob/main/correlation_heatmap.png "Correlations")
<img align="center" width="250" height="500" src="https://github.com/ahmedheakl/Data_Scientists_salary_prediction/blob/main/Words.png">
 </p>
<!--![alt text](https://github.com/ahmedheakl/Data_Scientists_salary_prediction/blob/main/Words.png "Common Words in Description")-->





