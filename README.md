![Zyte logo](zyte.png)

# Trial Project: Product spider #

### Goal ###

* Identify data quality issues
* Identify the causes of the issues for the results of a spider

While the spider itself is written in Python, you are free to use any programming language to complete the trial. Use the language you are most comfortable with.

The complete results are included in this repository in two formats for your convenience:

* items_uk.farnell.com.csv
* items_uk.farnell.com.json

Note, these files contain data which was scraped in the past. You might find different issues than in these files if you decide to execute the spider yourself and check the latest data.

### Data specification ###

The spider should scrape all items in the Electrical, Engineering Software, and Wireless Modules & Adapters categories on http://uk.farnell.com/.

Some of these fields might not be present in every product in the page.

Fields:

* url: (string) Url of the product being scraped
* brand: (string) Product brand name
* title (string) The name of the product, excluding the part number
* unit_price: (int) The price in pence
* stock_count: (int) The number in stock
* overview: (string) Product Overview description, usually has advertising copy
* information: (array) Array of dictionaries of specification paris in the format {name: specname, value: specvalue}
* manufacturer: (string) Manufacturer
* manufacturer_part: (string) Manufacturer part number
* tariff_number (string): Tariff code/number
* origin_country (string): Origin country
* files: (string list) String array of "Technical Docs" filenames (usually PDF or URL titles)
* file_urls: (string list) String array of "Technical Docs" URLs
* image_urls: (string list) String Array of additional image urls
* primary_image_url: (string) URL of the main product image
* associated_parts: (array) A list of associated part numbers
* trail: (string list) Ordered string array (highest level category first) of categories

### Deliverable ###

* Create a text file in the repository called `issues.txt` with a list of data problems you found. Please be explicit referring to the number of affected items, the severity, etc.
* The source code which you used to validate the data and find issues (could be a Jupyter notebook)
    * It should be well commented.
    * It should make it clear the approaches you took to validate data and why.
    * It should be reusable enough so that it can validate any spider (not just the Farnell spider).
    * It should include an instruction on how to execute the code, if it's not trivial.
    * The output of executed code (this can be logs or Jupyter notebook)
* Optional/Bonus points: Fix the issues in the spider where you are able.

>Note: If you are familiar with Scrapy Cloud, you can deploy and execute the spider, and then use the Scrapy Cloud API to assist in your data validation and analysis.

>Documentation on the API can be found here: https://docs.zyte.com/scrapy-cloud.html and documentation on its Python interface can be found here: https://github.com/scrapinghub/python-scrapinghub


Commit everything and push to this bitbucket repository in **your** branch. Create a pull request from **your** branch to master. Reply to the trial project invitation email to let us know when you are done.


### Time limit ###

The time limit for this project is 8 working hours, you must deliver the project finished or not when you have spent 8 hours working on in.

### Deadlines ###

This project doesn't have a deadline. Just submit the results as soon as you have them ready (but no sooner) including the spent time report. The sooner you submit, the sooner we will move to the next step.

### Confidentiality ###

Please don't share code or specifications about this project with anyone outside Zyte.
