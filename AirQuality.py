from tkinter import *
import requests
import json
#test comment:
root = Tk()
root.geometry("600x50")

try:
    code = 10001
    # Put api link gnerated by you in link variable
    link = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={code}&distance=5&API_KEY=############"

    api_request = requests.get(link)
    api  = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
    if category == 'Good':
        cl = '#00a300'
    elif category == 'Moderate':
        cl = "#cccc00"
    elif category == ' Unhealthy for Sensitive Groups':
        cl = "#cc7a00"
    elif category == 'Unhealthy':
        cl = "#cc0000"
    elif category == 'Very Unhealthy':
        cl = "#7a0052"
    elif category == 'Hazardous ':
        cl = "#520000"
    root.configure(background=cl)

except Exception as e:
    api = "Error..."

myLabel = Label(root, text = city + " Air Quality "+ str(quality)+" "+ category, font =("Helvetica",20), background = cl)
myLabel.pack()
root.mainloop()
