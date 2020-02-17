# Udacity Link Scraper

A script that uses selenium to get all Udacity links from a given lesson. In
the main script file, scraper.py, declare an array of urls each representing a
single lesson, and selenium will open all the concepts in that lesson and
extract the links that contain the word "Udacity" and output them to the
terminal.

## Set-up

Set-up a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```
You should see (venv) before your command prompt now. (You can type `deactivate`
to exit the virtual environment any time.)

Install the requirements:
```
pip install -r requirements.txt
```

You will also need [ChromeDriver](https://chromedriver.chromium.org/) in your
path. Alternatively, on Ubuntu:
```
sudo apt install chromium-chromedriver
```

Set up your environment variables:
```
touch .env
echo UDACITY_EMAIL="XXX" >> .env
echo UDACITY_PASSWORD="XXX" >> .env
```

## Usage

Make sure you are in the virtual environment (you should see (venv) before your
command prompt). If not `source /venv/bin/activate` to enter it.

Make sure .env variables are set:
```
set -a; source .env; set +a
```
Then add one url per lesson to the global URLS array in scraper.py
```
Usage: scraper.py
```

## License

Udacity Link Scraper is licensed under the [MIT license](https://github.com/danrneal/udacity-link-scraper/blob/master/LICENSE).
