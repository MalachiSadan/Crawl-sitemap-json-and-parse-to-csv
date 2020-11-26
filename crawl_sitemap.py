import urllib3

with open("roku.sitemap.txt", "r") as sitemap_txt:  # the url file may not be updated. please update it.
    http = urllib3.PoolManager()
    cnt_da_lp = 0  # count how much times the loop runs. just for debugging
    while True:
        readlin = sitemap_txt.readline()    # get the app marketplace url
        cnt_da_lp += 1
        print(cnt_da_lp)  # print every time the loop runs. you can know what line has a problem.
        if readlin == "":
            break  # end the loop when reaches end of file

        with open(f"ROKU_SITEMAP_JSON/{readlin[59:-24]}.json", "x") as sitemap:
            # ^ create a JSON file with app id from the url(change the index for getting app id's in other websites) ^
            reqst = http.request("GET", readlin, preload_content=False)  # GET request the url
            data = str(reqst.read())[2:-1]  # read the data without apostrophes
            sitemap.write(data)  # load the data into the file
            sitemap.close()
    sitemap_txt.close()
