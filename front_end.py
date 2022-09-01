from flask import Flask, render_template, redirect, url_for
from frontend.forms import ScraperForm
from frontend.scraper import ScraperManager, Scraper

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asödjfq324234kjnden3'

sm = ScraperManager.load_from_disk()

@app.route('/')
def index():
    return render_template("index.html", num_scraper=len(sm.active_scrapers))

@app.route('/add_scraper', methods=["GET", "POST"])
def add_scraper():
    form = ScraperForm()

    if form.validate_on_submit():
        scraper = Scraper(form.url.data, form.element.data, form.price_limit.data)
        sm.add_scraper(form.name.data, scraper)
        return redirect(url_for('index'))

    return render_template("new_scraper.html", form = form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)