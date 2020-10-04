from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/')
def hello():
    return "welcome to first flask App testing"

@app.route('/query-example')
def query_example():
	language = request.args.get('language') #if key doesn't exist, returns None
	return '''<h1>The language value is: {}</h1>'''.format(language)
    # return 'Todo from query-example...'

@app.route('/form-example',methods=['POST','GET'])
def formexample():
	if request.method == 'POST': #this block is only entered when the form is submitted
	    lang = request.form.get('language')
	    frame_work = request.form.get('framework')#request.form['framework'] makes view function to fail if it is not provided
	    from_ = request.form.get('from_date')
	    to_ = request.form.get('to_date')
	    return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>
                  <h1>from_date is: {}</h1>
                  <h1>to_date is: {}</h1>'''.format(lang, frame_work,from_,to_)

	return '''<form method="POST">
                  Language: <input id="lang" type="text" name="language"><br>
                  Framework: <input id="framWork" type="text" name="framework"><br>
                  From:<input id="fromDate" type="date" name="from_date"><br>
                  To:<input id="toDate" type="date" name="to_date"><br>
                  <input type="submit" value="View"><br>
              </form>'''

@app.route('/json-example',methods=['POST','GET'])
def jsonexample():
	if request.method=='POST':
		req_data = request.get_json()

		language = req_data['language']
		framework = req_data['framework']
		python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
		example = req_data['examples'][0] #an index is needed because of the array
		boolean_test = req_data['boolean_test']

		return '''
		       The language value is: {}
		       The framework value is: {}
		       The Python version is: {}
		       The item at index 0 in the example list is: {}
		       The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
	return 'Todo from json-example...'

if __name__ == '__main__':
    app.run(debug=True, port=5000)