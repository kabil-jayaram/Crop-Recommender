import numpy as np
import pandas as pd
import PySimpleGUI as sg
import pyttsx3
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from openpyxl import load_workbook

                                                    
ch=input("Do you want to enter new data into the dataset?(Y/N): ").lower()
if ch == 'y':
	layout = [[sg.Text('        		         Dataset Modification Assistant', font=("Helvetica", 30), text_color = 'yellow', justification="center")],  
			[sg.Text('')],
			[sg.Text('Please enter the following details:-', font=("Helvetica", 20))],                                                                                          
			[sg.Text('Enter the ratio of Nitrogen in the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica",20), size = (20,1) )],
			[sg.Text('Enter the ratio of Phosphorous in the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1))],
			[sg.Text('Enter the ratio of Potassium in the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1))],
			[sg.Text('Enter the average Temperature value around the field: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1))], 
			[sg.Text('Enter the average percentage of Humidity around the field: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1))], 
			[sg.Text('Enter the ph value of the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1))], 
			[sg.Text('Enter the average amount of Rainfall around the field: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1))],
			[sg.Text('Enter the Crop: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1))],
			[sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT11-' )],
			[sg.Button('Submit', font=("Helvetica", 20)),sg.Button('Quit', font=("Helvetica", 20))]]
	window1 = sg.Window('Crop Recommendation Assistant', layout, resizable=True, finalize=True) 
	window1.Maximize()
	while True:
		event, values = window1.read()
		if event == 'Submit':
			nitrogen_content = int(values[0])                                                                                                        
			phosphorus_content = int(values[1])                                                                                                        
			potassium_content = int(values[2])                                                                                                        
			temperature_content = float(values[3])                                                                                                       
			humidity_content = float(values[4])                                                                                                       
			ph_content = float(values[5])                                                                                                       
			rainfall = float(values[6])    
			crop_name = values[7]
			predict1 = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall,crop_name])  
			print(predict1)    
			wb = load_workbook('crop.xlsx')
			page = wb.active      
			page.append([nitrogen_content,phosphorus_content,potassium_content,temperature_content,humidity_content,ph_content,rainfall,crop_name])
			wb.save('crop.xlsx')
			print("Data Appended Successfully")
			window1['-OUTPUT11-'].update('Data Appended Successfully')
		ch = 'n'
		if event == sg.WINDOW_CLOSED or event == 'Quit':
			window1.close()
			break
if ch == 'n':
	excel = pd.read_excel('Crop.xlsx', header = 0)                            
	print(excel)                                                              
	print(excel.shape) 

	
	le = preprocessing.LabelEncoder()                                         
	crop = le.fit_transform(list(excel["CROP"]))                              

														
	NITROGEN = list(excel["NITROGEN"])                                        
	PHOSPHORUS = list(excel["PHOSPHORUS"])                                     
	POTASSIUM = list(excel["POTASSIUM"])                                      
	TEMPERATURE = list(excel["TEMPERATURE"])                                  
	HUMIDITY = list(excel["HUMIDITY"])                                        
	PH = list(excel["PH"])                                                    
	RAINFALL = list(excel["RAINFALL"])                                        


	features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))                     
	features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL])                     

	features = features.transpose()                                                                                
	print(features.shape)                                                                                          

	model = KNeighborsClassifier(n_neighbors=3)                                                                    
	model.fit(features, crop)                                                                                      

	layout = [[sg.Text('        		         Crop Recommendation Assistant', font=("Helvetica", 30), text_color = 'yellow', justification="center")],  
		[sg.Text('')],
		[sg.Text('Please enter the following details:-', font=("Helvetica", 20))],                                                                                          
		[sg.Text('Enter the ratio of Nitrogen in the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica",20), size = (20,1) ),sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'red', key='-OUTPUT2-' )],
		[sg.Text('Enter the ratio of Phosphorous in the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'red', key='-OUTPUT3-' )],
		[sg.Text('Enter the ratio of Potassium in the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'red', key='-OUTPUT4-' )],
		[sg.Text('Enter the average Temperature value around the field: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('°C', font=("Helvetica", 20))], 
		[sg.Text('Enter the average percentage of Humidity around the field: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('%', font=("Helvetica", 20))], 
		[sg.Text('Enter the ph value of the soil: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'red', key='-OUTPUT5-' )], 
		[sg.Text('Enter the average amount of Rainfall around the field: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1)),sg.Text('mm', font=("Helvetica", 20))],
		[sg.Text('Enter the size of the field: ', font=("Helvetica", 20),size = (45,1)), sg.Input(font=("Helvetica", 20),size = (20,1)), sg.Text('Hectare', font=("Helvetica", 20))],
		[sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT1-' )],
		[sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT6-' )],
		[sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT8-' )],
		[sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT7-' )],
		[sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT9-' )],
		[sg.Text(size=(50,1),font=("Helvetica",20) , text_color = 'yellow', key='-OUTPUT10-' )],
		[sg.Button('Submit', font=("Helvetica", 20)),sg.Button('Quit', font=("Helvetica", 20))]]
	window = sg.Window('Crop Recommendation Assistant', layout, resizable=True, finalize=True) 
	window.Maximize()
	while True:
		event, values = window.read() 
		if event == sg.WINDOW_CLOSED or event == 'Quit':                                                                                          
			break
		nitrogen_content = int(values[0])                                                                                                        
		phosphorus_content = int(values[1])                                                                                                        
		potassium_content = int(values[2])                                                                                                        
		temperature_content = int(values[3])                                                                                                       
		humidity_content = int(values[4])                                                                                                       
		ph_content = float(values[5])                                                                                                       
		rainfall = int(values[6])   
		size = int(values[7])                                                                                                    
		predict1 = np.array([nitrogen_content,phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content, rainfall])  
		print(predict1)                                                                                                                             
		predict1 = predict1.reshape(1,-1)                                                                              
		print(predict1)                                                                                                
		predict1 = model.predict(predict1)                                                                             
		print(predict1)                                                                                                
		crop_name = str()
		match predict1:  
			case 0:                                                                                            
				crop_name = 'Apple'
				seed_rate = 12
				maturity = '8 years'
				rotation = 'Clover'
				cost = size * 26305
				yild = '11 tonnes/hectare'
			case 1:
				crop_name = 'Banana'
				seed_rate = 9.4
				maturity = '15 months'
				rotation = 'Sweet potato'
				cost = size * 44206
				yild = '100 tonnes/hectare'
			case 2:
				crop_name = 'Blackgram'
				seed_rate = 20
				maturity = '95 days'
				rotation = 'Maghi Jowar'
				cost = size * 6125
				yild = '1,100 kg/hectare'
			case 3:
				crop_name = 'Chickpea'
				seed_rate = 74.7
				maturity = '120 days'
				rotation = 'Maize'
				cost = size * 4553
				yild = '30 quintals/hectare'
			case 4:
				crop_name = 'Coconut'
				seed_rate = 10
				maturity = '10 years'
				rotation = 'Banana'
				cost = size * 10684
				yild = '14,000 nuts/hectare'
			case 5:
				crop_name = 'Coffee'
				seed_rate = 6
				maturity = '5 years'
				rotation = 'Potato'
				cost = size * 71384
				yild = '750 kg/hectare'
			case 6:
				crop_name = 'Cotton'
				seed_rate = 13.5
				maturity = '160 days'
				rotation = 'Mungbean'
				cost = size * 60559
				yild = '60 quintals/hectare'
			case 7:
				crop_name = 'Grapes'
				seed_rate = 10
				maturity = '3 years'
				rotation = 'Blackberries'
				cost = size * 114658
				yild = '55 tonnes/hectare'
			case 8:
				crop_name = 'Jute'
				seed_rate = 9
				maturity = '150 days'
				rotation = 'African nightshade'
				cost = size * 50052
				yild = '50 tonnes/hectare'
			case 9:
				crop_name = 'Kidneybeans'
				seed_rate = 45
				maturity = '140 days'
				rotation = 'Potato'
				cost = size * 36542
				yild = '50 quintals/hectare'
			case 10:
				crop_name = 'Lentil'
				seed_rate = 40
				maturity = '140 days'
				rotation = 'African nightshade'
				cost = size * 6404
				yild = '8 quintals/hectare'
			case 11:
				crop_name = 'Maize'
				seed_rate = 22.5
				maturity = '95 days'
				rotation = 'Melons'
				cost = size * 6151
				yild = '3 tonnes/hectare'
			case 12:
				crop_name = 'Mango'
				seed_rate = 54
				maturity = '15 weeks'
				rotation = 'Turmeric'
				cost = size * 45477
				yild = '7 tonnes/hectare'
			case 13:
				crop_name = 'Mothbeans'
				seed_rate = 15
				maturity = '90 days'
				rotation = 'Garlic'
				cost = size * 25228
				yild = '25 quintals/hectare'
			case 14:
				crop_name = 'Mungbeans'
				seed_rate = 20
				maturity = '90 days'
				rotation = 'Broccoli'
				cost = size * 5576
				yild = '8 quintals/hectare'
			case 15:
				crop_name = 'Muskmelon'
				seed_rate = 3.5
				maturity = '110 days'
				rotation = 'Chamomile'
				cost = size * 12141
				yild = '150 quintals/hectare'
			case 16:
				crop_name = 'Orange'
				seed_rate = 23
				maturity = '8 months'
				rotation = 'Nasturtium'
				cost = size * 24686
				yild = '50 tonnes/hectare'
			case 17:
				crop_name = 'Papaya'
				seed_rate = 14.3
				maturity = '14 months'
				rotation = 'Banana'
				cost = size * 84984
				yild = '200 kg/hectare'
			case 18:
				crop_name = 'Pigeonpeas'
				seed_rate = 13.5
				maturity = '145 days'
				rotation = 'Pepper'
				cost = size * 39436
				yild = '700 kg/hectare'
			case 19:
				crop_name = 'Pomegranate'
				seed_rate = 34
				maturity = '5 years'
				rotation = 'Coriander'
				cost = size * 105623
				yild = '50 tonnes/hectare'
			case 20:
				crop_name = 'Rice'
				seed_rate = 13.5
				maturity = '60 days'
				rotation = 'Potato'
				cost = size * 83683
				yild = '2.5 tonnes/hectare'
			case 21:
				crop_name = 'Watermelon'
				seed_rate = 4.25
				maturity = '90 days'
				rotation = 'Radish'
				cost = size * 24281
				yild = '30 tonnes/hectare'

		if humidity_content >=1 and humidity_content<= 33:                                                
			humidity_level = 'Low humid'
		elif humidity_content >=34 and humidity_content <= 66:
			humidity_level = 'Medium humid'
		else:
			humidity_level = 'High humid'

		if temperature_content >= 0 and temperature_content<= 6:                                           
			temperature_level = 'Cool'
		elif temperature_content >=7 and temperature_content <= 25:
			temperature_level = 'Warm'
		else:
			temperature_level= 'Hot' 

		if rainfall >=1 and rainfall <= 100:                                                              
			rainfall_level = 'Less'
		elif rainfall >= 101 and rainfall <=200:
			rainfall_level = 'Moderate'
		elif rainfall >=201:
			rainfall_level = 'Heavy rain'

		if nitrogen_content >= 1 and nitrogen_content <= 50:                                             
			nitrogen_level = 'Less'
			window['-OUTPUT2-'].update('Less nitrogen content in soil!!!')        
		elif nitrogen_content >=51 and nitrogen_content <=100:
			nitrogen_level = 'Not too Less but also not too High'
			window['-OUTPUT2-'].update(' ')  
		elif nitrogen_content >=101:
			nitrogen_level = 'High'
			window['-OUTPUT2-'].update('High nitrogen content in soil!!!')        

		if phosphorus_content >= 1 and phosphorus_content <= 50:                                         
			phosphorus_level = 'Less'
			window['-OUTPUT3-'].update('Less phosphorus content in soil!!!')        
		elif phosphorus_content >= 51 and phosphorus_content <=100:
			phosphorus_level = 'Not too Less but also not too High'
			window['-OUTPUT3-'].update(' ')  
		elif phosphorus_content >=101:
			phosphorus_level = 'High'
			window['-OUTPUT3-'].update('High phosphrous content in soil!!!')        

		if potassium_content >= 1 and potassium_content <=50:                                           
			potassium_level = 'Less'
			window['-OUTPUT4-'].update('Less potassium content in soil!!!')        
		elif potassium_content >= 51 and potassium_content <= 100:
			potassium_level = 'Not too Less but also not too High'
			window['-OUTPUT4-'].update(' ')  
		elif potassium_content >=101:
			potassium_level = 'High'
			window['-OUTPUT4-'].update('High potassium content in soil!!!')        

		phlevel=''
		if int(ph_content) >=0 and int(ph_content) <=5:                                                        
			phlevel = 'Acidic'         
		elif int(ph_content) >= 6 and int(ph_content) <= 8:
			phlevel = 'Neutral'
		elif int(ph_content) >= 9 and int(ph_content) <= 14:
			phlevel = 'Alkaline'
		
		if phlevel != 'Neutral':
			window['-OUTPUT5-'].update('Soil is '+phlevel+'!!!')   
		else:
			window['-OUTPUT5-'].update(' ')       
		
		print("Crop Name: "+crop_name)
		print("Humidity: "+humidity_level)
		print("Temperature: "+temperature_level)
		print("Rainfall: "+rainfall_level)
		print("Nitrogen: "+nitrogen_level)
		print("Phosphorus: "+phosphorus_level)
		print("Potassium: "+potassium_level)
		print("ph: "+phlevel)
		print("Seed Rate: "+str(seed_rate)+" kg/ha")
		print("Maturity Period: "+maturity)
		print("Crop for rotation: "+rotation)
		print("Cost: ₹"+str(cost))
		print("Yield: "+yild)
		
		window['-OUTPUT1-'].update('The best crop that you can grow: '+crop_name)        
		window['-OUTPUT6-'].update('Amount of seed: '+str(seed_rate)+ ' kg/ha')    
		window['-OUTPUT7-'].update('Crop for rotation: '+rotation) 
		window['-OUTPUT8-'].update('Maturity Period: '+maturity) 
		window['-OUTPUT9-'].update('Cost for '+str(size)+' hectare: ₹'+str(cost))
		window['-OUTPUT10-'].update('Yield: '+yild)      

	window.close() 