# imdbcrawler (DEPRECATED)
The idea of the program is to shape an Excel sheet which answers a question: 
'In which countries, years and genres was made 5 best movies?' (by imdb opinion)

To run 'parser.py' properly you need to have next libraries: requests, BeautifulSoup, pprint (but it isn't neccessary, you can
delete this one from code), re, pandas and collections (which is installed with python).

'parser.py' is a web-scraper for imdb.com, which creates an excel file 'report.xlsx'.
get_data(url) function converts url link to BeautifulSoup object
get_info(soup) function takes a link and gets all the required information (such as country, year, genre of film) from there
the for cycle is basically a web-crawler with an i variable just for you to know the number of the checked sites so far.
top variable measures how long is our table will be
with pandas library we create DataFrame, which then converts to the 'report.xlsx' file.

This soft was made 20.04.2021 at 16:46 by whatserface (https://github.com/whatserface).
