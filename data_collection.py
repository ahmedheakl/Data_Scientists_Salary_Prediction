import glassdoor_scraper as sp

df = sp.get_jobs('data scientist', 1000, False)

df.to_csv('./csv_saved/mydata.csv')
