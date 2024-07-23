from flask import Flask, render_template, redirect, url_for, request
import webbrowser
app = Flask(__name__)

@app.route('/')
def launch_page():
    return render_template('launch.html')

@app.route('/age', methods=['GET', 'POST'])
def age_page():
    if request.method == 'POST':
        age = request.form.get('age')
        if age is None:
            error_message = 'Please select an age range.'
            return render_template('age.html', error=error_message)
        elif age == '18+':
            return redirect(url_for('bnf_page'))
        else:
            return redirect(url_for('bnfc_page'))
    return render_template('age.html')

@app.route('/bnf', methods=['GET', 'POST'])
def bnf_page():
    return render_template('bnf.html')

@app.route('/pallergy', methods=['GET', 'POST'])
def pallergy_page():
    if request.method == 'POST':
        pallergy = request.form.get('pallergy')
        if pallergy == 'yes':
            return redirect(url_for('erythromycin_page'))
        else:
            return redirect(url_for('amoxycillin_page'))
    return render_template('pallergy.html')

@app.route('/erythromycin', methods=['GET', 'POST'])
def erythromycin_page():
    return render_template('erythromycin.html')

@app.route('/amoxycillin', methods=['GET', 'POST'])
def amoxycillin_page():
    return render_template('amoxycillin.html')

@app.route('/gender', methods=['GET', 'POST'])
def gender_page():
    if request.method == 'POST':
        gender = request.form.get('gender')
        if gender == 'male':
            return redirect(url_for('doxy_page'))
        elif gender is None:
            error_message = 'Please select an option.'
            return render_template('gender.html', error=error_message)
        else:
            return redirect(url_for('pregnant_page'))
    return render_template('gender.html')

@app.route('/pregnant_page', methods=['GET', 'POST'])
def pregnant_page():
    if request.method == 'POST':
        value = request.form.get('pregnant')
        if value == 'yes':
            return redirect(url_for('pallergy_page'))
        elif value is None:
            error_message = 'Please select an option.'
            return render_template('pregnant.html', error=error_message)
        else:
            return redirect(url_for('pp_page'))
    return render_template('pregnant.html')

@app.route('/pp_page', methods=['GET', 'POST'])
def pp_page():
    if request.method == 'POST':
        value = request.form['pp']
        if value == 'yes':
            return redirect(url_for('pallergy_page'))
        else:
            return redirect(url_for('ec_page'))
    return render_template('pp.html')

@app.route('/ec_page', methods=['GET', 'POST'])
def ec_page():
    if request.method == 'POST':
        ec = request.form['ec']
        if ec == 'yes':
            return redirect(url_for('doxy_page'))
        else:
            return redirect(url_for('pallergy_page'))
    return render_template('ec.html')

@app.route('/doxy_page', methods=['GET', 'POST'])
def doxy_page():
    if request.method == 'POST':
        doxy = request.form['doxy']
        if doxy == 'yes':
            return redirect(url_for('doxycycline_page'))
        else:
            return redirect(url_for('clarithromycin_page'))
    return render_template('doxy.html')

@app.route('/doxycycline', methods=['GET', 'POST'])
def doxycycline_page():
    return render_template('doxycycline.html')

@app.route('/clarithromycin', methods=['GET', 'POST'])
def clarithromycin_page():
    return render_template('clarithromycin.html')

##part - 2###################################################

@app.route('/bnfc', methods=['GET', 'POST'])
def bnfc_page():
    return render_template('bnfc.html')


@app.route('/pallergy1', methods=['GET', 'POST'])
def pallergy1_page():
    if request.method == 'POST':
        pallergy1 = request.form['pallergy1']
        if pallergy1 == 'yes':
            return redirect(url_for('gender1_page'))
        else:
            return redirect(url_for('ww1_page'))
    return render_template('pallergy1.html')

@app.route('/gender1', methods=['GET', 'POST'])
def gender1_page():
    if request.method == 'POST':
        gender1 = request.form['gender1']
        if gender1 == 'male':
            return redirect(url_for('age1_page'))
        else:
            return redirect(url_for('pregnant1_page'))
    return render_template('gender1.html')

@app.route('/age1', methods=['GET', 'POST'])
def age1_page():
    if request.method == 'POST':
        age1 = request.form['age1']
        if age1 == '12+':
            return redirect(url_for('antibiotics_page'))
        else:
            return redirect(url_for('ww3_page'))
    return render_template('age1.html')

@app.route('/antibiotics', methods=['GET', 'POST'])
def antibiotics_page():
    if request.method == 'POST':
        antibiotics = request.form['antibiotics']
        if antibiotics == 'yes':
            return redirect(url_for('clarithromycin1_page'))
        else:
            return redirect(url_for('doxycycline_page'))
    return render_template('antibiotics.html')

@app.route('/pregnant1', methods=['GET', 'POST'])
def pregnant1_page():
    if request.method == 'POST':
        value = request.form['pregnant1']
        if value == 'yes':
            return redirect(url_for('erythromycin_page'))
        else:
            return redirect(url_for('pp1_page'))
    return render_template('pregnant1.html')

@app.route('/clarithromycin1', methods=['GET', 'POST'])
def clarithromycin1_page():
    return render_template('clarithromycin1.html')

@app.route('/pp1', methods=['GET', 'POST'])
def pp1_page():
    if request.method == 'POST':
        value = request.form['pp1']
        if value == 'yes':
            return redirect(url_for('ww2_page'))
        else:
            return redirect(url_for('ec1_page'))
    return render_template('pp1.html')

@app.route('/ec1', methods=['GET', 'POST'])
def ec1_page():
    if request.method == 'POST':
        value = request.form['ec1']
        if value == 'yes':
            return redirect(url_for('age1_page'))
        else:
            return redirect(url_for('ww2_page'))
    return render_template('ec1.html')

@app.route('/ww1', methods=['GET', 'POST'])
def ww1_page():
    if request.method == 'POST':
        value = request.form['ww1']
        if value == '11under':
            return redirect(url_for('a1_page'))
        elif value == '1over':
            return redirect(url_for('a2_page'))
        else:
            return redirect(url_for('amoxycillin_page'))
    return render_template('ww1.html')

@app.route('/ww2', methods=['GET', 'POST'])
def ww2_page():
    if request.method == 'POST':
        value = request.form['ww2']
        if value == '1under':
            return redirect(url_for('erythromycin1_page'))
        elif value == '2over':
            return redirect(url_for('erythromycin2_page'))
        else:
            return redirect(url_for('erythromycin_page'))
    return render_template('ww2.html')

@app.route('/erythromycin1', methods=['GET', 'POST'])
def erythromycin1_page():
    return render_template('erythromycin1.html')

@app.route('/erythromycin2', methods=['GET', 'POST'])
def erythromycin2_page():
    return render_template('erythromycin2.html')


@app.route('/ww3', methods=['GET', 'POST'])
def ww3_page():
    if request.method == 'POST':
        value = request.form['ww3']
        if value == '8under':
            return redirect(url_for('clarithromycin2_page'))
        elif value == '8over':
            return redirect(url_for('clarithromycin3_page'))
        elif value == '12over':
            return redirect(url_for('clarithromycin4_page'))
        elif value == '20over':
            return redirect(url_for('clarithromycin5_page'))
        else:
            return redirect(url_for('clarithromycin1_page'))
    return render_template('ww3.html')

@app.route('/clarithromycin5', methods=['GET', 'POST'])
def clarithromycin5_page():
    return render_template('clarithromycin5.html')

@app.route('/clarithromycin4', methods=['GET', 'POST'])
def clarithromycin4_page():
    return render_template('clarithromycin4.html')

@app.route('/clarithromycin3', methods=['GET', 'POST'])
def clarithromycin3_page():
    return render_template('clarithromycin3.html')

@app.route('/clarithromycin2', methods=['GET', 'POST'])
def clarithromycin2_page():
    return render_template('clarithromycin2.html')

@app.route('/a2', methods=['GET', 'POST'])
def a2_page():
    return render_template('a2.html')

@app.route('/a1', methods=['GET', 'POST'])
def a1_page():
    return render_template('a1.html')

if __name__ == '__main__':
    app.run(debug=True)

