import glassdoor_scraper as sp

df = sp.get_jobs('data scientist', 1000, False)

# Saving the data into a csv file for later use
df.to_csv('./csv_saved/mydata.csv')
