# imports
from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import Entry1Form, WindForm, TimeForm
from app.data import APDataFrame

# assign default search method
search_method = 'time'

# definition homepage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Air Partners Madlibs')

# definition for first form of search parameters
@app.route('/entry1', methods=['GET', 'POST'])
def entry1():

    # initialize first form
    form = Entry1Form()

    if form.validate_on_submit():

        # flash which parameter was requested
        flash('Search {} requested'.format(
            form.entry1.data))

        # log search method
        session['search_method'] = form.entry1.data

        # redirect to second form
        return redirect(url_for('entry2'))

    # render first form template
    return render_template('entry1.html', title='Air Partners Madlibs Search', form=form)

# definition for second form of search parameters
@app.route('/entry2', methods=['GET', 'POST'])
def entry2():

    # grab search_method form session log
    search_method = session.get('search_method', None)

    # iinitialize second form based on search_method
    if search_method == 'wind':
        form = WindForm()
    else:
        form = TimeForm()

    if form.validate_on_submit():

        # flash parameters chosen
        flash('Search for {} pollutant when the {} is {}'.format(
            form.pollutant.data, search_method, form.entry2.data))

        # log responses
        session['pollutant'] = form.pollutant.data
        session['parameter'] = form.entry2.data

        # redirect to homepage
        return redirect(url_for('results'))

    # render second form template
    return render_template('entry2.html', title='Air Partners Madlibs Search', form=form, search_method=search_method)

@app.route('/results', methods=['GET', 'POST'])
def results():

    # grab logged responses
    pollutant = session.get('pollutant', None)
    param = session.get('parameter', None)


    data = APDataFrame()
    data.load_data()
    data.sort_by_dir(param)
    data.sort_by_pollutant(pollutant)
    print(data.df)
    #flash(data.df)
    return render_template('results.html',  tables=[data.df[:200].to_html(classes='data')], titles=data.df.columns.values)


