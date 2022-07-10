from flask import render_template, request

from src import app
from src.utilities import MasterProphet


@app.after_request
def add_header(response):
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.route("/")  # When to call this function
@app.route("/home")  # @ is a decorator which is used to call this function
def index():
    """ Renders the home page """
    return render_template(
        "index.html"
    )

# Flask by default supports only get method, so we need to add post inside the method's parameter
@app.route("/predict", methods=["POST", "GET"])
def predict():
    # var ticker = go to the current request, into the form, and get the parameter called ticker
    ticker = request.form["ticker"]
    master_prophet = MasterProphet(ticker)

    forecast = master_prophet.forecast()

    actual_forecast = round(forecast.yhat[0], 2)
    lower_bound = round(forecast.yhat_lower[0], 2)
    upper_bound = round(forecast.yhat_upper[0], 2)
    bound = round(((upper_bound - actual_forecast) +
                  (actual_forecast - lower_bound) / 2), 2)

    summary = master_prophet.info["summary"]
    country = master_prophet.info["country"]
    sector = master_prophet.info["sector"]
    website = master_prophet.info["website"]
    min_date = master_prophet.info["min_date"]
    max_date = master_prophet.info["max_date"]

    forecast_date = master_prophet.forecast_date.date()

	# Can take more than 1 argument, if it takes another arg, you can pass in the name of any variable you want.
	# LHS = RHS; LHS is the name of a var I want to give to the template, RHS is the value of that var.
    return render_template(
        "predict.html",
        ticker=ticker.upper(),
        sector=sector,
        country=country,
        website=website,
        summary=summary,
        min_date=min_date,
        max_date=max_date,
        forecast_date=forecast_date,
        forecast=actual_forecast,
        bound=bound
    )
