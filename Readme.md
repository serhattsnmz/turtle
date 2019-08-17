## Turtle (Instagram Photo Downloader)

- It is for downloading your friend's photos and videos with your account.
- Your username and your password won't be stored.
- Whether or not you have two factor authentication in your Instagram account or not, this will still work.
- It uses `Selenium` and three different browsers which are `Chrome`, `Firefox` and `PhantomJS`
    - The driver is being asked at the beginning of the program.
    - If you want to see what happens -> use `Chrome` or `Firefox`
    - If you want to view the process in the background -> use `PhantomJs`

## Requirements

- Python 3.6+
- Selenium
- PhantomJS
- Chrome Driver for Selenium
- Gecko Driver for Selenium

## How to install and run

1. Download the source from Github
    - `git clone https://github.com/serhattsnmz/turtle.git`
    - `cd turtle`
2. Install requirements
	- `pip install -r requirements.txt`
3. Download at least one of following drivers.
    - Download and install `PhantomJs` (Opsional)
        - For Linux
            - Do not use apt-get for downloading PhantomJs!
            - Wget the latest phantomjs (as per [PhatomJs Download Page](http://phantomjs.org/download.html "PhatomJs Download Page"))
                - `wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2`
            - Untar it
                - `tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2`
            - Moved the phantomjs executable to /usr/bin/ (may need sudo)
                - `sudo cp /path/to/phantom/untar/bin/phantomjs /usr/bin/`
        - For Windows
            - Download the `PhantomJS` with link below :
                - [PhatomJs Download Page](http://phantomjs.org/download.html "PhatomJs Download Page")
            - Copy `path\phantomjs-2.1.1-windows\bin\phantomjs.exe` file to `C:\Program Files (x86)\Python36-32\Scripts`
    - Download and install `ChromeDriver` (Opsional)
        - For Linux
            - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) 
            - Moved the ChromeDriver executable to /usr/bin/ (may need sudo)
        - For Windows
            - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) 
            - Copy `path\chromedriver.exe` file to `C:\Program Files (x86)\Python36-32\Scripts`
    - Download and install `GeckoDriver` for Firefox (Opsional)
        - For Linux
            - Wget the lasted GeckoDriver (as per [GeckoDriver Download Page](https://github.com/mozilla/geckodriver/releases))
                - `wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz`
            - Untar it
                - `tar -xvzf geckodriver*`
            - Make it executable
                - `chmod +x geckodriver`
            - Moved the geckoDriver executable to /usr/bin/ (may need sudo)
                - `sudo cp /path/to/geckoDriver /usr/bin/`
        - For Windows
            - Download the `GeckoDriver` with link below :
                - [GeckoDriver Download Page](https://github.com/mozilla/geckodriver/releases)
            - Copy `path\geckodriver.exe` file to `C:\Program Files (x86)\Python36-32\Scripts`
4. Run python file with Python 3
	- `python3 turtle_console.py`

## Usage

Simply call `python turtle_console.py`

First you have to choose a driver, PhantomJs, Firefox or Chrome.

It will ask for your Instagram username and password for logging in (If you did not define them in config.js). Then it will ask for a username which user's photo you want to download.

You can download:
- All user's photos
- Just the last stories you do not have
- Number of photos

## Advanced Usage

```
usage: turtle_console.py [-h] [-u] [-p] [-d] [-P] [-l] [-D] [-v]

Fetch all the lectures for a Instagram

optional arguments:
  -h, --help        show this help message and exit
  -u , --username   User username
  -p , --password   User password
  -d , --driver     Choosen Driver. [1]PantomJS [2]Chrome [3]Firefox
  -P , --path       The path for saving photos.
  -l , --list       List of Usernames
  -D , --download   Download choice. [1]Update(Default for list) [2]Full
  -v , --video      Download videos or not. [True]Download [False] Do Not
                    Download(Default)
```

## Config.Json File

This file can be used for saving login data and path for photos. Nothing is saved automatically to here even if you change the file.
- *driver*   : (*int*) Driver you want to use as default (*1* or *2* or *3*)
- *username* : (*string*) User's username
- *password* : (*string*) User's pass
- *path*     : (*string*) The path for saving photos. Default value is `photos`
    - Exp : `path/photos` or `../path/photos`
