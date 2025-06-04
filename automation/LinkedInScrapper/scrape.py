import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters

### for editing the csv file
from csv import writer

### name of the local csv file where we will store the scrapped data,
### currently we will just append the scrapped data to the file
### for now, this file has columns as:
### data.title, data.company, data.company_link, data.place, data.date, data.link, data.description, data.description_html, data.insights
filename = 'data.csv'

### Edit the limit value from here:
limitValue = 10

### Edit the search locations from here
locationsList = ['India', 'Ireland', 'United Kingdom']

### a function to save the scrapped data to a local csv file, 
### this is highly inefficient for now, since we are saving one record each time it is scrapped....to many file write calls
### yet let's follow this approach for a good safe start
def saveData(rowData):
    ### basic thing taken from GfG: https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/
    with open(filename, 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(rowData)
    
        # Close the file object
        f_object.close()


# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

# Fired once for each successfully processed job
def on_data(data: EventData):
### again the file is stored with columns like this, please follow the same order or change it at both the places, 
### you may change fields in the file as well as the row data list below 
### data.title, data.company, data.company_link, data.place, data.date, data.link, data.description, data.description_html, data.insights
    rowData = [data.title, data.company, data.company_link, data.place, data.date, data.link, data.description, data.description_html, data.insights]
    saveData(rowData)
    print('[ON_DATA]', data.title, data.company, data.company_link, data.place, data.date, data.link, data.description, data.description_html, data.insights, len(data.description))

# Fired once for each page (25 jobs)
def on_metrics(metrics: EventMetrics):
  print('[ON_METRICS]', str(metrics))

def on_error(error):
    print('[ON_ERROR]', error)

def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path=None, # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=2.5,  # Slow down the scraper to avoid 'Too many requests 429' errors (in seconds)
    page_load_timeout=20  # Page load timeout (in seconds)    
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        options=QueryOptions(            
            limit=1  # Limit the number of jobs to scrape.            
        )
    ),Query(
        query='HR Analyst',
        options=QueryOptions(
            locations=locationsList,            
            # apply_link = True,  # Try to extract apply link (easy applies are skipped). Default to False.
            limit=limitValue,
            # filters=QueryFilters(              
            #     company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000',  # Filter by companies.
            #     relevance=RelevanceFilters.RECENT,
            #     # time=TimeFilters.MONTH,
            #     # type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
            #     # experience=None,                
            # )
        )
    ),
    Query(
        query='HR Analytics',
        options=QueryOptions(
            locations=locationsList,            
            # apply_link = True,  # Try to extract apply link (easy applies are skipped). Default to False.
            limit=limitValue,
            # filters=QueryFilters(              
            #     company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000',  # Filter by companies.
            #     relevance=RelevanceFilters.RECENT,
            #     # time=TimeFilters.MONTH,
            #     # type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
            #     # experience=None,                
            # )
        )
    ),
    Query(
        query='HR Consultant',
        options=QueryOptions(
            locations=locationsList,            
            # apply_link = True,  # Try to extract apply link (easy applies are skipped). Default to False.
            limit=limitValue,
            # filters=QueryFilters(              
            #     company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000',  # Filter by companies.
            #     relevance=RelevanceFilters.RECENT,
            #     # time=TimeFilters.MONTH,
            #     # type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
            #     # experience=None,                
            # )
        )
    ),
]

scraper.run(queries)