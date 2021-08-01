from flask import Flask,render_template,request,url_for,redirect
import requests,json

app = Flask(__name__ )

result=requests.get('https://334de7e5-ad66-42ad-af50-748483750c28.mock.pstmn.io//mock_data')
if(result.status_code==200):
    if(result.status_code==200):
        result=result.json()
        mock_data=result
        result=dict((result[i]["name"],result[i]["password"]) for i in range(0,len(result)))


@app.route('/')
@app.route('/grootan_mock_application/')
def mainpage():
   return render_template('mainpage.html')

@app.route('/grootan_mock_application/userlists/',methods=['GET','POST'])
def userlists():
   if request.method == 'POST':
        name = request.form["user"]
        password = request.form["pass"]
        if((name not in result.keys()) or result[name]!=password):
            return  "error"   
   return render_template('userlists.html',d=mock_data)      

@app.route('/grootan_mock_application/register/',methods=['POST'])
def register():
   data=dict()
   if request.method == 'POST':
        data["_id"]=len(result.keys())
        data["name"]=request.form["user"]
        data["age"]=request.form["age"]
        data["email_id"]=request.form["mail"]
        data["contact_no"]=request.form["contact"]
        data["password"]=request.form["pass"]
        data=json.dumps(data) 
        mock_data.append(data) 
        print(mock_data)
        result=requests.post('https://334de7e5-ad66-42ad-af50-748483750c28.mock.pstmn.io//mock_data',data=mock_data)
   return render_template('mainpage.html')

'''
@app.route('/grootan_mock_application/pre/')
def pre():
   pass
   


@app.route('/grootan_mock_application/next/')
def next():
   pass

@app.route('/grootan_mock_application/<string:name>')
def user_name(name):
   if(name ):
   return render_template('user.html' ,name = name)
'''
if __name__ == "__main__":
    app.run(debug=True)