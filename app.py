from flask import Flask
from flask import render_template
from datetime import time
import csv

app = Flask(__name__)

legend = 'Date and Time'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/jarl")
def JarlChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Jarl":
                labels.append(str(row[2]))
                values.append(row[0])

    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Jarl")

@app.route("/hurricane_jack")
def HurricaneChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Hurricane Jack":
                labels.append(str(row[2]))
                values.append(row[0])
    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Hurricane Jack")

@app.route("/mills_and_hills")
def MillsChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Mills and Hills":
                labels.append(str(row[2]))
                values.append(row[0])
    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Mills and Hills")

@app.route("/highlander")
def HighChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Highlander":
                labels.append(str(row[2]))
                values.append(row[0])
    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Highlander")

@app.route("/vital_spark")
def VitalChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Vital Spark":
                labels.append(str(row[2]))
                values.append(row[0])
    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Vital Spark")

@app.route("/sanda_blonde")
def SandaChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Sanda Blonde":
                labels.append(str(row[2]))
                values.append(row[0])
    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Sanda Blonde")

@app.route("/ragnarok")
def RagChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Ragnarok":
                labels.append(str(row[2]))
                values.append(row[0])
    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Ragnarok")

@app.route("/avalanche")
def AvaChart():
    labels = []
    values = []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if row[3] == "Avalanche":
                labels.append(str(row[2]))
                values.append(row[0])
    return render_template('chart.html', values=values, labels=labels, legend=legend, title="Avalanche")


if __name__ == "__main__":
    app.run(debug=True)
