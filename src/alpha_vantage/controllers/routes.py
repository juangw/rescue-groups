from api_projects.app import app
from api_projects.log import log
from src.alpha_vantage.utils.call_alpha_vantage import api_get_req
from flask import render_template


@app.route("/stocks")
@app.route("/stocks/")
def stocks_home():
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "stocks.html"
    """
    log.info("Creating stocks page")
    results = api_get_req("GOOGL").json()
    return render_template("stocks.html", results=results)

