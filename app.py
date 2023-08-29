import streamlit as st
import joblib
from PIL import Image
model=joblib.load('car-price-predictor')

st.title("Welcome to car price predictor")
st.header("This is a header")
st.text("This is used to display simple text")

#st.success("This is used to display Success messages in a green box")
#st.warning("This is used to display Warning message in orange box")
#st.error("This is used to display Error messages in red box")
#st.info("This is used to display Information in a blue box")


fuel_type= st.radio("Fuel Type", ('Diesel','Gas'))
if fuel_type=='Diesel':
    fuel_type_encode=0  
else:
    fuel_type_encode=1

aspiration= st.radio("Aspiration", ('Standard','Turbo'))
if aspiration=='Turbo':
    aspiration_encode=0  
else:
    aspiration_encode=1

door_number= st.radio("Number of doors", ('Two','Four'))
if door_number=='Four':
    door_number_encode=0  
else:
    door_number_encode=1

car_body= st.radio("Car Type", ('Convertible','Hard Top','Hatch Back','Sedan','Wagon'))
if car_body=='Convertible':
    car_body_encode=0  
elif car_body=='Hard Top':
    car_body_encode=1
elif car_body=='Hatch Back':
    car_body_encode=2
elif car_body=='Sedan':
    car_body_encode=3
else:
    car_body_encode=4

drive_wheel= st.radio("Drive Wheel", ('Rear Wheel Drive','Front Wheel Drive','Four Wheel Drive'))
if drive_wheel=='Rear Wheel Drive':
    drive_wheel_encode=2
elif drive_wheel=='Front Wheel Drive':
    drive_wheel_encode=1
else:
    drive_wheel_encode=0

engine_location= st.radio("Engine Location", ('Front','Rear'))
if engine_location=='Front':
    engine_location_encode=0  
else:
    engine_location_encode=1

engine_type= st.radio("Engine Type", ('DOHC','OHCV','OHC','L','Rotor','OHCF','DOHCV'))
engine_dict={'DOHC':0, 'OHCV':5, 'OHC':3, 'L':2, 'Rotor':6, 'OHCF':4, 'DOHCV':1}
engine_type_encode=engine_dict[engine_type]

cylinder_number= st.radio("Number of cylinders", ('4 Cylinders','6 Cylinders','5 Cylinders','3 Cylinders','12 Cylinders','2 Cylinders','8 Cylinders'))
cylinder_dict={'4 Cylinders':2, '6 Cylinders':3,'5 Cylinders':1,'3 Cylinders':4,'12 Cylinders':5,'2 Cylinders':6,'8 Cylinders':0}
cylinder_number_encode=cylinder_dict[cylinder_number]

fuel_system= st.radio("Fuel System", ('MPFI','2BBL','MFI','1BBL','SPFI','4BBL','ID','SPDI'))
fuel_dict={'1BBL':0,'2BBL':1,'4BBL':2,'ID':3,'MFI':4,'MPFI':5,'SPDI':6,'SPFI':7}
fuel_system_encode=fuel_dict[fuel_system]

compression_ratio=st.number_input(label='Enter Compression Ratio',min_value=7.00,max_value=23.00,value=7.00,step=1.,format="%.2f")
horse_power=st.number_input(label='Enter Horse Power',min_value=48,max_value=288,value=48)
peak_rpm=st.number_input(label='Enter Peak rpm',min_value=4150,max_value=6600,value=4150)
city_mpg=st.number_input(label='Enter City Mileage',min_value=13,max_value=49,value=13)
highway_mpg=st.number_input(label='Enter Highway Mileage',min_value=16,max_value=54,value=16)




#gender=st.selectbox('Select Gender',['Male','Female'])
submit_btn =st.button("Show Expected Price of vehicle")

if submit_btn==True:
    intake=[[fuel_type_encode,aspiration_encode,door_number_encode,car_body_encode,drive_wheel_encode,engine_location_encode,engine_type_encode,cylinder_number_encode,fuel_system_encode,compression_ratio,horse_power,peak_rpm,city_mpg,highway_mpg]]
    result=model.predict(intake)[0]
    result=result*80
    st.write("The predicted price is ",result)