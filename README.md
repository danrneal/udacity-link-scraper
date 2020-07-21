# Udacity Link Scraper

A script that uses selenium to get all Udacity links from a given lesson. In the main script file, scraper.py, declare an array of urls each representing a single lesson, and selenium will open all the concepts in that lesson and extract the links that contain the word "Udacity" and output them to the terminal.

## Set-up

Set-up a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

You should see (env) before your command prompt now. (You can type `deactivate` to exit the virtual environment any time.)

Install the requirements:

```bash
pip install -U pip
pip install -r requirements.txt
```

You will also need [ChromeDriver](https://chromedriver.chromium.org/) in your path. Alternatively, on Ubuntu:

```bash
sudo apt install chromium-chromedriver
```

Set up the global `URLS` array in `scraper.py` with one url per lesson.

Set up your environment variables:

```bash
touch .env
echo UDACITY_EMAIL="XXX" >> .env
echo UDACITY_PASSWORD="XXX" >> .env
```

## Usage

Make sure you are in the virtual environment (you should see (env) before your command prompt). If not `source /env/bin/activate` to enter it.

Make sure .env variables are set:

```bash
set -a; source .env; set +a
```

Then run the script:

```bash
Usage: scraper.py
```

## License

Udacity Link Scraper is licensed under the [MIT license](https://github.com/danrneal/udacity-link-scraper/blob/master/LICENSE).
