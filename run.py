from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.template_filter()
def year_filter(value, format='%Y'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['year_filter'] = year_filter

@app.route("/")
def template_test():
    return render_template('home.html', my_string="Wheeeee!", 
        my_list=[0,1,2,3,4,5], title="Affirmalytics", current_time=datetime.datetime.now())

@app.route("/home")
def home():
    return render_template('home.html', my_string="Foo", 
        my_list=[6,7,8,9,10,11], title="Affirmalytics", current_time=datetime.datetime.now())

@app.route("/demo")
def demo():
    return render_template('demo.html', my_string="Demo", 
        my_list=[12,13,14,15,16,17], title="Demo", current_time=datetime.datetime.now())

@app.route("/about")
def about():
    return render_template('about.html', my_string="Bar", 
        my_list=[18,19,20,21,22,23], title="About", current_time=datetime.datetime.now())

@app.route("/contact")
def contact():
    return render_template('template.html', my_string="FooBar"
        , my_list=[24,25,26,27,28,29], title="Contact Us", current_time=datetime.datetime.now())


if __name__ == '__main__':
    app.run(debug=True)