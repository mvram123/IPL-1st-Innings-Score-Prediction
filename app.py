# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'first-innings-score-lasso-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    
    overs = float(request.form['overs'])
    runs = int(request.form['runs'])
    wickets = int(request.form['wickets'])
    runs_in_prev_5 = int(request.form['runs_in_prev_5'])
    wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
    
    
        
        
    temp_array = temp_array + [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5]
    
    if request.method == 'POST':
        
        venue = request.form['venue']
        if venue == 'Dubai International Cricket Stadium':
            temp_array = temp_array + [float(171.539)]
        elif venue == 'Eden Gardens':
            temp_array = temp_array + [float(194.000)]
        elif venue == 'Feroz Shah Kotla Stadium':
            temp_array = temp_array + [float(156.286)]
        elif venue == 'M Chinnaswamy Stadium':
            temp_array = temp_array + [float(163.000)]
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array + [float(144.125)]
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [float(171.000)]
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array + [float(171.500)]
        elif venue == 'Sawai Mansingh Stadium':
            temp_array = temp_array + [float(163.429)]
        elif venue == 'Sharjah Cricket Stadium':
            temp_array = temp_array + [float(177.500)]
        elif venue == 'Sheikh Zayed Stadium':
            temp_array = temp_array + [float(162.500)]
        elif venue == 'Wankhede Stadium	':
            temp_array = temp_array + [float(176.143)]
            
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,1]
        
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,1]
            
        
        venue = request.form['venue']
        if venue == 'Dubai International Cricket Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0] 
        elif venue == 'Eden Gardens':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0] 
        elif venue == 'Feroz Shah Kotla Stadium':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0] 
        elif venue == 'M Chinnaswamy Stadium':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0] 
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0] 
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0] 
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0] 
        elif venue == 'Sawai Mansingh Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0] 
        elif venue == 'Sharjah Cricket Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0] 
        elif venue == 'Sheikh Zayed Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0] 
        elif venue == 'Wankhede Stadium	':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1] 
            
            
       
        
        data = np.array([temp_array])
        print(data)
        my_prediction = int(regressor.predict(data))
              
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)



if __name__ == '__main__':
	app.run(debug=True)