from time import sleep
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
with st.sidebar:
    select = option_menu(menu_title="Main Menu"
                         ,options=["Home","Shoe Type and Design", "Payment Gateway", "Confirm"]
                         )
st.markdown("<h1 style='text-align: center; color: white;'>Hi, Welcome to Shoe Box</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;'>We will help you recreate your world of shoes...</h2>", unsafe_allow_html=True)

if select=='Home':
    st.markdown('<style>input[type="text"]{height: 35px; width: 700px; font-size: 16px; text-align: left; border : 2px solid white;}</style>', unsafe_allow_html=True)
    str1=st.text_input("Enter Your Name: ", "")
    if(str1!=""):
        st.markdown(f"""<h2 style="text-align: center; color:#ffffff;">Hi {str1}</h2>""", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: orange;'>SELECT THE SHOE TYPE FOR YOURSELF AND WE WILL HELP YOU DESIGN IT</h3>", unsafe_allow_html=True)
        
a=""
selection=False
if select=="Shoe Type and Design":
    shoe_type=st.selectbox('Which type of shoe do you want to reconstruct your shoe to?', ['Flip Flops', 'Trainers', 'Spikes', 'Studs', 'Sandals','Sneakers','Non Marking'])
    if(shoe_type=='Flip Flops'):
        image = Image.open('flip_flops.jpg')
        st.image(image,use_column_width=True)
    if(shoe_type=='Trainers'):
        image = Image.open('trainers.jpg') #ignore the error
        st.image(image,use_column_width=True)

    if(shoe_type=='Spikes'):
        image = Image.open('spikes.jpg')
        st.image(image,use_column_width=True)
    if(shoe_type=='Studs'):
        image = Image.open('studs.jpg')
        st.image(image,use_column_width=True)
    if(shoe_type=='Sandals'):
        image = Image.open('sandals.jpg')
        st.image(image,use_column_width=True)
    if(shoe_type=='Sneakers'):
        image = Image.open('sneakers.jpg')
        st.image(image,use_column_width=True)
    if(shoe_type=='Non Marking'):
        image = Image.open('non_marking.jpg')
        st.image(image,use_column_width=True)

    a=shoe_type
    b='No'
    if(st.button('Next')):
        st.markdown("<h3 style='text-align: center; color: orange;'>SELECT THE DESIGN FOR YOUR SHOE</h3>", unsafe_allow_html=True)
        if(a=='Flip Flops'):
            image1=Image.open('flip_flop_des_1.jpg')
            image2=Image.open('flip_flop_des_2.jpg')
            image3=Image.open('flip_flop_des_3.jpg')
            image4=Image.open('flip_flop_des_4.jpg')
            image5=Image.open('flip_flop_des_5.jpg')
            image6=Image.open('flip_flop_des_6.jpg')
            st.image(image1,use_column_width=True,caption='Design 1')
            st.image(image2,use_column_width=True,caption='Design 2')
            st.image(image3,use_column_width=True,caption='Design 3')
            st.image(image4,use_column_width=True,caption='Design 4')
            st.image(image5,use_column_width=True,caption='Design 5')
            st.image(image6,use_column_width=True,caption='Design 6')
            design=st.selectbox('Which design do you want to reconstruct your shoe to?',['Design 1','Design 2','Design 3','Design 4','Design 5','Design 6'])
            sleep(12)
            b=st.radio('Do you want to reconstruct your shoe to the design you have selected?',['No','Yes'])
        elif(a=='Trainers'):
            image1=Image.open('trainers_des1.jpg')
            image2=Image.open('trainers_des2.jpg')
            image3=Image.open('trainers_des3.jpg')
            image4=Image.open('trainers_des4.jpg')
            image5=Image.open('trainers_des5.jpg')
            image6=Image.open('trainers_des6.jpg')
            st.image(image1,use_column_width=True,caption='Design 1')
            st.image(image2,use_column_width=True,caption='Design 2')
            st.image(image3,use_column_width=True,caption='Design 3')
            st.image(image4,use_column_width=True,caption='Design 4')
            st.image(image5,use_column_width=True,caption='Design 5')
            st.image(image6,use_column_width=True,caption='Design 6')
            design=st.selectbox('Which design do you want to reconstruct your shoe to?',['Design 1','Design 2','Design 3','Design 4','Design 5','Design 6'])
            sleep(12)
            b=st.radio('Do you want to reconstruct your shoe to the design you have selected?',['No','Yes'])

        elif(a=='Spikes'):
            image1=Image.open('spikes_des1.jpg')
            image2=Image.open('spikes_des2.jpg')
            image3=Image.open('spikes_des3.jpg')
            image4=Image.open('spikes_des4.jpg')
            image5=Image.open('spikes_des5.jpg')
            image6=Image.open('spikes_des6.jpg')
            st.image(image1,use_column_width=True,caption='Design 1')
            st.image(image2,use_column_width=True,caption='Design 2')
            st.image(image3,use_column_width=True,caption='Design 3')
            st.image(image4,use_column_width=True,caption='Design 4')
            st.image(image5,use_column_width=True,caption='Design 5')
            st.image(image6,use_column_width=True,caption='Design 6')
            design=st.selectbox('Which design do you want to reconstruct your shoe to?',['Design 1','Design 2','Design 3','Design 4','Design 5','Design 6'])
            sleep(12)
            b=st.radio('Do you want to reconstruct your shoe to the design you have selected?',['No','Yes'])
            
        elif(a=='Studs'):
            image1=Image.open('studs_des1.jpg')
            image2=Image.open('studs_des2.jpg')
            image3=Image.open('studs_des3.jpg')
            image4=Image.open('studs_des4.jpg')
            image5=Image.open('studs_des5.jpg')
            image6=Image.open('studs_des6.jpg')
            st.image(image1,use_column_width=True,caption='Design 1')
            st.image(image2,use_column_width=True,caption='Design 2')
            st.image(image3,use_column_width=True,caption='Design 3')
            st.image(image4,use_column_width=True,caption='Design 4')
            st.image(image5,use_column_width=True,caption='Design 5')
            st.image(image6,use_column_width=True,caption='Design 6')
            design=st.selectbox('Which design do you want to reconstruct your shoe to?',['Design 1','Design 2','Design 3','Design 4','Design 5','Design 6'])
            sleep(12)
            b=st.radio('Do you want to reconstruct your shoe to the design you have selected?',['No','Yes'])
            
        elif(a=='Sandals'):
            image1=Image.open('sandals_des1.jpg')
            image2=Image.open('sandals_des2.jpg')
            image3=Image.open('sandals_des3.jpg')
            image4=Image.open('sandals_des4.jpg')
            image5=Image.open('sandals_des5.jpg')
            image6=Image.open('sandals_des6.jpg')
            st.image(image1,use_column_width=True,caption='Design 1')
            st.image(image2,use_column_width=True,caption='Design 2')
            st.image(image3,use_column_width=True,caption='Design 3')
            st.image(image4,use_column_width=True,caption='Design 4')
            st.image(image5,use_column_width=True,caption='Design 5')
            st.image(image6,use_column_width=True,caption='Design 6')
            design=st.selectbox('Which design do you want to reconstruct your shoe to?',['Design 1','Design 2','Design 3','Design 4','Design 5','Design 6'])
            sleep(12)
            b=st.radio('Do you want to reconstruct your shoe to the design you have selected?',['No','Yes'])
            
        elif(a=="Sneakers"):
            image1=Image.open('sneakers_des1.jpg')
            image2=Image.open('sneakers_des2.jpg')
            image3=Image.open('sneakers_des3.jpg')
            image4=Image.open('sneakers_des4.jpg')
            image5=Image.open('sneakers_des5.jpg')
            image6=Image.open('sneakers_des6.jpg')
            st.image(image1,use_column_width=True,caption='Design 1')
            st.image(image2,use_column_width=True,caption='Design 2')
            st.image(image3,use_column_width=True,caption='Design 3')
            st.image(image4,use_column_width=True,caption='Design 4')
            st.image(image5,use_column_width=True,caption='Design 5')
            st.image(image6,use_column_width=True,caption='Design 6')
            design=st.selectbox('Which design do you want to reconstruct your shoe to?',['Design 1','Design 2','Design 3','Design 4','Design 5','Design 6'])
            sleep(12)
            b=st.radio('Do you want to reconstruct your shoe to the design you have selected?',['No','Yes'])
            
        elif(a=="Non Marking"):
            image1=Image.open('nonmarking_des1.jpg')
            image2=Image.open('nonmarking_des2.jpg')
            image3=Image.open('nonmarking_des3.jpg')
            image4=Image.open('nonmarking_des4.jpg')
            image5=Image.open('nonmarking_des5.jpg')
            image6=Image.open('nonmarking_des6.jpg')
            st.image(image1,use_column_width=True,caption='Design 1')
            st.image(image2,use_column_width=True,caption='Design 2')
            st.image(image3,use_column_width=True,caption='Design 3')
            st.image(image4,use_column_width=True,caption='Design 4')
            st.image(image5,use_column_width=True,caption='Design 5')
            st.image(image6,use_column_width=True,caption='Design 6')
            design=st.selectbox('Which design do you want to reconstruct your shoe to?',['Design 1','Design 2','Design 3','Design 4','Design 5','Design 6'])
            sleep(12)
            b=st.radio('Do you want to reconstruct your shoe to the design you have selected?',['No','Yes'])
    
    sleep(3)
    if(b=='Yes'):
        sleep(1)
        st.markdown("<h3 style='text-align: center; color: orange;'>Your shoe will be reconstructed to the design and type that you have selected</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: orange;' em>Please proceed to Payment Gateway</h3>", unsafe_allow_html=True)
        selection=True

if(select=='Payment Gateway'):
    
    subs=st.radio('Are u a suscriber?',['No','Yes'])
    sleep(3)
    if(subs=='Yes'):
        num=st.text_input('Enter your suscriber number')
        sleep(10)
        sleep(1)
        fp=open('phone_numbers.txt','r')
        lines=fp.readlines()
        name=""
        for line in lines:
            group=line.split()
            if(num==group[0]):
                name=group[1]
                break
    sleep(1)
    if(subs=='Yes'):
        if(name==''):
            st.markdown("<h5 style='text-align: center; color: orange;'>You are not a subscriber</h5>", unsafe_allow_html=True)
            sleep(1)
            st.markdown("<h5 style='text-align: center; color: orange;'>You need to pay an amount of ₹1500</h5>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h5 style='text-align: center; color: orange;'>Welcome {name}</h5>", unsafe_allow_html=True)
            sleep(1)
            st.markdown("<h5 style='text-align: center; color: orange;'>You need to pay an amount of ₹1000</h5>", unsafe_allow_html=True)
    else:
        st.markdown("<h5 style='text-align: center; color: orange;'>You need to pay an amount of ₹1500</h5>", unsafe_allow_html=True)
    
    truth=False
    choice=option_menu(menu_title='Choose a Payment Gateway',
                       options=['Credit Card','Debit Card','UPI'])
    if(choice=='Credit Card'):
        # st.markdown("<h3 style='text-align: center; color: orange;'>Enter an amount of ₹1564</h3>", unsafe_allow_html=True)
        sleep(2)
        st.markdown("<h3 style='text-align: center; color: orange;'>Please enter your Credit Card Details</h3>", unsafe_allow_html=True)
        with st.form(key='Credit_Card_Details'):
            card_no=st.text_input('Card Number')
            cvv=st.text_input('CVV')
            name=st.text_input('Name on Card')
            expiry=st.text_input('Expiry Date')
            submit=st.form_submit_button(label='Submit')
            if(submit):
                st.markdown("<h3 style='text-align: center; color: orange;'>Payment Successful</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Your shoe will be ready in an hour</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Thank you for believing in us</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Please visit again</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Have a nice day</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Stay Safe</h3>", unsafe_allow_html=True)
                truth=True

    elif(choice=='Debit Card'):
        sleep(2)
        st.markdown("<h3 style='text-align: center; color: orange;'>Please enter your Debit Card Details</h3>", unsafe_allow_html=True)
        with st.form(key='Debit_Card_Details'):
            card_no=st.text_input('Card Number')
            cvv=st.text_input('CVV')
            name=st.text_input('Name on Card')
            expiry=st.text_input('Expiry Date')
            submit=st.form_submit_button(label='Submit')
            if(submit):
                st.markdown("<h3 style='text-align: center; color: orange;'>Payment Successful</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Your shoe will be ready in an hour</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Thank you for believing in us</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Please visit again</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Have a nice day</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Stay Safe</h3>", unsafe_allow_html=True)
                truth=True
               
    elif(choice=='UPI'):
        sleep(3)
        options=option_menu(menu_title='Choose a UPI App',
                            options=['Google Pay','Paytm'])
        sleep(3)
        if(options=='Google Pay'):
            image=Image.open('gpay.jpg')
            st.image(image,use_column_width=True)
            upi_id=st.text_input('Enter your UPI ID')
            sleep(1)
            amout=st.text_input('Enter the amount')
            sleep(1)
            pin=st.text_input('Enter your UPI PIN',type='password')
            confirm=st.button('Confirm')
            if(confirm):
                st.markdown("<h3 style='text-align: center; color: orange;'>Payment Successful</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Your shoe will be ready in an hour</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Thank you for believing in us</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Please visit again</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Have a nice day</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Stay Safe</h3>", unsafe_allow_html=True)
                truth=True

        if(options=='Paytm'):
            image=Image.open('paytm.jpg')
            st.image(image,use_column_width=True)
            upi_id=st.text_input('Enter your UPI ID')
            sleep(1)
            amout=st.text_input('Enter the amount')
            sleep(1)
            pin=st.text_input('Enter your UPI PIN',type='password')
            confirm=st.button('Confirm')
            if(confirm):
                st.markdown("<h3 style='text-align: center; color: orange;'>Payment Successful</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Your shoe will be ready in an hour</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Thank you for believing in us</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Please visit again</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Have a nice day</h3>", unsafe_allow_html=True)
                sleep(1)
                st.markdown("<h3 style='text-align: center; color: orange;'>Stay Safe</h3>", unsafe_allow_html=True)
                truth=True

        sleep(2)
        if(truth):
            if(st.button('Next')):
                sleep(3)
                st.markdown("<h3 style='text-align: center; color: orange;'>Please Proceed to confirmation tab</h3>", unsafe_allow_html=True)

        
if(select=='Confirm'):
    
    st.markdown("<h3 style='text-align: center; color: orange;'>Please Click the Below Confirm Button to start Building</h3>", unsafe_allow_html=True)
    if(st.button('Confirm')):
        sleep(2)
        st.markdown("<h3 style='text-align: center; color: orange;'>Your shoe is building</h3>", unsafe_allow_html=True)
        sleep(1)
        st.markdown("<h3 style='text-align: center; color: orange;'>Thanks for Your Patience</h3>", unsafe_allow_html=True)

              
