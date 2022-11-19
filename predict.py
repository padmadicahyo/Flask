from flask import Flask, render_template, request,redirect
import pickle 
app = Flask(__name__)

#load model
model = pickle.load(open('model/model_classifier_svm.pkl', 'rb'))

lokasi = {'Albury': 2,'BadgerysCreek': 4,'Cobar': 10,'CoffsHarbour': 11,'Moree': 21,'Newcastle': 24,'NorahHead': 26,
'NorfolkIsland': 27,'Penrith': 30,'Richmond': 34,'Sydney': 37,'SydneyAirport': 38,'WaggaWagga': 42,'Williamtown': 45,
'Wollongong': 47,'Canberra': 9,'Tuggeranong': 40,'MountGinini': 23,'Ballarat': 5,'Bendigo': 6,'Sale': 35,'MelbourneAirport': 19,
'Melbourne': 18,'Mildura': 20,'Nhil': 25,'Portland': 33,'Watsonia': 44,'Dartmoor': 12,'Brisbane': 7,'Cairns': 8,'GoldCoast': 14,
'Townsville': 39,'Adelaide': 0,'MountGambier': 22,'Nuriootpa': 28,'Woomera': 48,'Albany': 1,'Witchcliffe': 46,
'PearceRAAF': 29,'PerthAirport': 32,'Perth': 31,'SalmonGums': 36,'Walpole': 43,'Hobart': 15,'Launceston': 17,
'AliceSprings': 3,'Darwin': 13,'Katherine': 16,'Uluru': 41}

arah = {'W': 13,'NNW': 6,'SE': 9,'ENE': 1,'SW': 12,'SSE': 10,'S': 8,'NE': 4,'N': 3,'SSW': 11,
'WSW': 15,'ESE': 2,'E': 0,'NW': 7,'WNW': 14,'NNE': 5}
            
# routes-----------------------------------------------------------------------
@app.route('/home', methods=['GET'])
def prediksi():
    return render_template('prediksi.html')


        
@app.route('/prediksi', methods=['POST'])
def prepredict():
        list_predict = []
#request from Hari----------------------+
        if request.form['Hari'] == "Ya":
            list_predict.append(1)
        else:
            list_predict.append(0)
#request from Lokasi----------------------+
        for i in (list(lokasi.keys())):
            if request.form['Lokasi'] == i:
                list_predict.append(lokasi[i])
            else:
                pass
#request from Arah angin----------------------+
        for j in (list(arah.keys())):
            if request.form['Arah'] == j:
                list_predict.append(arah[j])
            else:
                pass
#request from Jam Cerah----------------------+
        list_predict.append(float(request.form['jam']))
#request from Awan 3 sore----------------------+
        list_predict.append(float(request.form['awan']))
#request from Kelembaban 3 sore----------------------+
        list_predict.append(float(request.form['kelembaban']))
#predicting---------------------------------------+
        prediction = model.predict([list_predict])
        
        output = {
            0:"Not Raining",
            1:"Hujan"
        }
        return render_template('prediksi.html', prediksi=output[prediction[0]]) 

if __name__ == '__main__':    
	# Run Flask di localhost 
    app.run(host="localhost", port=5000, debug=True)