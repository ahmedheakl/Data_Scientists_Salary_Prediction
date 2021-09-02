from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd


def get_jobs(keyword, num_jobs, verbose, path='chromedriver.exe'):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    # Initializing the webdriver
    options = webdriver.ChromeOptions()

    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

    # Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=" + \
        keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    jobs = []

    time.sleep(1)
    driver.find_element_by_xpath(
        './/li[@class="react-job-listing css-7x0jr eigr9kq3"]').click()

    time.sleep(1)
    try:
        # clicking to the X.
        driver.find_element_by_css_selector('[alt="Close"]').click()
        print(' x out worked')
    except NoSuchElementException:
        print(' x out failed')
        pass

    # If true, should be still looking for new jobs.
    while len(jobs) < num_jobs:

        # Going through each job in this page
        # jl for Job Listing. These are the buttons we're going to click.
        job_buttons = driver.find_elements_by_xpath(
            ".//*[@class='react-job-listing css-7x0jr eigr9kq3']")

        for job_button in job_buttons:

            print("Progress: {}".format(
                "" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  # You might
            time.sleep(3)

            collected_successfully = False

            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath(
                        './/div[@class="css-87uc0g e1tk4kwz1"]').text
                    location = driver.find_element_by_xpath(
                        './/div[@class="css-56kyx5 e1tk4kwz5"]').text
                    job_title = driver.find_element_by_xpath(
                        './/div[contains(@class, "css-1vg6q84 e1tk4kwz4")]').text
                    job_description = driver.find_element_by_xpath(
                        './/div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    time.sleep(2)

            try:
                salary_estimate = driver.find_element_by_xpath(
                    './/span[@class="css-0 e1wijj240"]').text
            except NoSuchElementException:
                salary_estimate = -1  # You need to set a "not found value. It's important."

            try:
                rating = driver.find_element_by_xpath(
                    './/span[@class="css-1m5m32b e1tk4kwz2"]').text
            except NoSuchElementException:
                rating = -1  # You need to set a "not found value. It's important."

            # Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            # Going to the Company tab...
            # clicking on this:
            # <div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element_by_xpath(
                    './/div[@data-test="overview"]').click()

                time.sleep(2)

                try:
                    size = driver.find_element_by_xpath(
                        './/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]//span[text()="Size"]//following-sibling::*').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath(
                        './/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]//span[text()="Founded"]//following-sibling::*').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath(
                        './/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]//span[text()="Type"]//following-sibling::*').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath(
                        './/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]//span[text()="Industry"]//following-sibling::*').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath(
                        './/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]//span[text()="Sector"]//following-sibling::*').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath(
                        './/div[@class="d-flex justify-content-start css-rmzuhb e1pvx6aw0"]//span[text()="Revenue"]//following-sibling::*').text
                except NoSuchElementException:
                    revenue = -1

            # Rarely, some job postings do not have the "Company" tab.
            except NoSuchElementException:
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1

            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title": job_title,
                         "Salary Estimate": salary_estimate,
                         "Job Description": job_description,
                         "Rating": rating,
                         "Company Name": company_name,
                         "Location": location,
                         "Size": size,
                         "Founded": founded,
                         "Type of ownership": type_of_ownership,
                         "Industry": industry,
                         "Sector": sector,
                         "Revenue": revenue})
            # add job to jobs

        # Clicking on the "next page" button
        try:
            driver.find_element_by_xpath(
                './/li[@class="css-114lpwu e1gri00l4"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(
                num_jobs, len(jobs)))
            break

    # This line converts the dictionary object into a pandas DataFrame.
    return pd.DataFrame(jobs)
