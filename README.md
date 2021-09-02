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

![alt text](https://github.com/ahmedheakl/Data_Scientists_salary_prediction/blob/main/correlation_heatmap.png "Correlations")
<img width="250" height="400" src="https://github.com/ahmedheakl/Data_Scientists_salary_prediction/blob/main/Words.png">

## Model Building
* I extract the most important features(22 feature), and then I got the dummy columns for the categorical features
* **Note**: In pulling out the *y* column, I converted it into a 1-d array because it is recommended.
* I split the data into train and test ```test_size=0.2```
* I used statsmodels OLS to get information on the relevant column of the data.
I tried three different models:
*	**Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 

*MAE: mean absolute error*
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. **SEE THE EXAMPLE FILE:** *API_request_example.ipynb* 













