# WallStreetAI - Stock Price Predictor

![GitHub](https://img.shields.io/github/license/Interstellarkai/WallStreetAI)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Interstellarkai/WallStreetAI)
![GitHub repo size](https://img.shields.io/github/repo-size/Interstellarkai/WallStreetAI)
![GitHub language count](https://img.shields.io/github/languages/count/Interstellarkai/WallStreetAI)
![GitHub last commit](https://img.shields.io/github/last-commit/Interstellarkai/WallStreetAI)

Stock market prediction is the act of trying to determine the future value of a company stock or other financial instrument traded on an exchange. The successful prediction of a stock's future price could yield significant profit. The efficient-market hypothesis suggests that stock prices reflect all currently available information and any price changes that are not based on newly revealed information thus are inherently unpredictable. Others disagree and those with this viewpoint possess myriad methods and technologies which purportedly allow them to gain future price information.

We make use of Facebook's Time Series forcasting algorithm Prophet to predict stock market price of US based companies in real time using multi-variate, single step forecasting strategy.

![Header](src/static/images/main_page.png)

## Getting Started

Download or clone project from github:
```
$ git clone https://github.com/Interstellarkai/WallStreetAI
```

Create a project environment (pipenv recommended):
```
$ pipenv install
```

Install prerequisites:
```
$ pip install -r REQUIREMENTS.txt
```

Run project:
```
$ cd WallStreetAI
$ pipenv shell (if virtual environment is used)
$ python3 runserver.py
```

## Model Validation Analysis

**Facebook (Stock: FB) Validation**
![FB_validation](src/static/images/fb_forecast_30_day_validation.png)

**Microsoft (Stock: MSFT) Validation**
![MSFT_validation](src/static/images/msft_forecast_30day_validation.png)

**Google (Stock: GOOGL) Validation**
![GOOGLE_validation](src/static/images/googl_forecast_30day_validation.png)

## Support

If you like the work I do, show your appreciation by 'FORK', 'STAR' and 'SHARE'.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
