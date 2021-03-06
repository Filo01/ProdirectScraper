# ProdirectScraper

## Instalation

Installing Scrapy inside a virtual environment on all platforms.

Python packages can be installed either globally (a.k.a system wide), or in user-space. We do not recommend installing scrapy system wide.

Instead, we recommend that you install scrapy within a so-called “virtual environment” (virtualenv).

Virtualenvs allow you to not conflict with already-installed Python system packages (which could break some of your system tools and scripts), and still install packages normally with pip (without sudo and the likes).

To install it globally (having it globally installed actually helps here), it should be a matter of running:

```
$ [sudo] pip install virtualenv
```

Inside virtual env install ProdirectScraper dependencies:

```
pip install -r requirements.txt
```

## Config Settings
These are the basic options:
```
# available currency EUR,USD,GBP
currency =
# Number of pieces to display in the email
pp =

# mailer configuration options
smtp_host =
mail_from =
mail_to =
smtp_user =
smtp_pass =
smtp_port =
smtp_tls =
smtp_ssl =
```

After that edit the configuration specific to the category of product you would like to scrape.

For trainers:
```
#available sizes are from 4 to 12, e.g 4 or 4,5,10
size =

```

For men's clothing:
```
# available options:  One size, ONE-SIZE, S/M, L/XL, S, M, L, XL, XXL
size =
```


## Runing the Spiders

To put our spider to work, go to the project’s top level directory and run:

```
scrapy crawl SCRAPER
```
where "SCRAPER" must be one of the following:
- trainers
- mensclothing
- womensclothing

This command runs the spider with name trainers , that will crawl http://www.prodirectselect.com/ website and send mail with lowest prices, model description and link to trainers, which size is specified in configuration.ini 
