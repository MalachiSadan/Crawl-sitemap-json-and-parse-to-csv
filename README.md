# Crawl sitemap json
[Python 3.6 recommended]

[urllib3 required]

For this project, I chose to crawl the roku marketplace json.
I added a .txt file of all the channels(May not be updated), and started crawling.

## Parse to CSV
Running that may cuase an error.
You can see at line 18, there's a wired sentence:
```
if '//","k' in sv:
    sv = sv.replace('//","k', '","k')
```
That means that if there's a string: //","k in the JSON it will replace it with: ","k , replacing the //. I replaced it becuase i had a lot of parsing errors with //",
That for some reason showd a lot in the JSON files description. Now i had errors becuase i deleted the " thing where that // was in the end of the file.  I know there's a "kewords" sentence at the end of the value, so i added a k and removed the // so it wont detect it and replace it (in the line
```
if '//"' in sv:
    sv = sv.replace('//"', "//")
```
). Afterwards, there's theres a sentence with h instead of k, becuase h stands for hdPosterUrl.


### Important changes in the files

In all of the
```
with open(f"ROKU_SITEMAP_JSON\\{readlin[59:-24]}.json"
```
's, you need to create a folder to save the JSON files, and change the index of the ID that you need.
Don't forget to update the sitemap.txt if you want to crawl roku, or use something else.

##### If you have any problems, please open an issue. I will try to help.
