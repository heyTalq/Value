from flask import Flask, render_template, flash, request
from wtforms import Form, DecimalField, TextAreaField, validators, StringField, SubmitField
import MLalgo as ml
import numpy as np
 
# App config.
DEBUG = True
app = Flask(__name__)
#app._static_folder = templates/static
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):

#	zipcode = DecimalField('Zipcode:', validators=[validators.required()])
#	sfLiving = DecimalField('Square feet living:', validators=[validators.required()])
#	sfLot = DecimalField('Square feet lot:', validators=[validators.required()])
#	numBed = DecimalField('Number of bedrooms:', validators=[validators.required()])
#	numBath = DecimalField('Number of bathrooms:', validators=[validators.required()])
#	floors = DecimalField('Number of floors:', validators=[validators.required()])
#	water = DecimalField('Waterfront:', validators=[validators.required()])
#	year = DecimalField('Year built:', validators=[validators.required()])

	zipcode = DecimalField('Zipcode:', validators=[validators.InputRequired()])
	sfLiving = DecimalField('Square feet living:', validators=[validators.InputRequired()])
	sfLot = DecimalField('Square feet lot:', validators=[validators.InputRequired()])
	numBed = DecimalField('Number of bedrooms:', validators=[validators.InputRequired()])
	numBath = DecimalField('Number of bathrooms:', validators=[validators.InputRequired()])
	floors = DecimalField('Number of floors:', validators=[validators.InputRequired()])
	water = DecimalField('Waterfront:', validators=[validators.InputRequired()])
	year = DecimalField('Year built:', validators=[validators.InputRequired()])

 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        zipcode=request.form['zipcode']
        sfLiving = request.form['sfLiving']
        sfLot = request.form['sfLot']
        numBed = request.form['numBed']
        numBath = request.form['numBath']
        floors = request.form['floors']
        water = request.form['water']
        year = request.form['year']
        print( zipcode, " ", sfLiving, " ", sfLot, numBed, " ", numBath, " ", floors, water, " ", year)
 
        if form.validate():
            userParam = [float(zipcode),float(sfLiving),float(sfLot),float(numBed),float(numBath),float(floors),float(water),float(year)]
            valuation = ml.MLthingy(np.asmatrix(userParam))

            #valuation = ml.MLthingy([zipcode,sfLiving,sfLot,numBed,numBath,floors,water,year])
		 # Save the comment here.
            flash('Your property is valued at $'+ str( valuation[0]) + " with a range between $" + str(valuation[1]) + " and $" + str(valuation[2]))
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5000, debug=True)
