from flask import Flask, request, render_template
import pickle

app=Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        MALE = float(request.form['male'])
        AGE = float(request.form['age'])
        EDUCATION = float(request.form['education'])
        CURRENTSMOKER = float(request.form['currentSmoker'])
        CIGSPERDAY = float(request.form['cigsPerDay'])
        BPMEDS = float(request.form['BPMeds'])
        PREVALENTSTROKE = float(request.form['prevalentStroke'])
        PREVALENTHYP = float(request.form['prevalentHyp'])
        DIABETES = float(request.form['diabetes'])
        TOTCHOL = float(request.form['totChol'])
        SYSBP = float(request.form['sysBP'])
        DIABP = float(request.form['diaBP'])
        BMI = float(request.form['BMI'])
        HEARTRATE = float(request.form['heartRate'])
        GLUCOSE = float(request.form['glucose'])

        vars = [[MALE, AGE, EDUCATION, CURRENTSMOKER, CIGSPERDAY,
                BPMEDS, PREVALENTSTROKE, PREVALENTHYP, DIABETES,
                TOTCHOL, SYSBP, DIABP, BMI, HEARTRATE, GLUCOSE]]
        
        result = model.predict(vars)[0]

        if result==1:
            output = "Prone to TenYearCHD"
        else:
            output = "Not prone to TenYearCHD"

        return render_template("index.html", anticipation = output)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


