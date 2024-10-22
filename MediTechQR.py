import streamlit as st
import qrcode
from io import BytesIO

st.title('Hello Dear User',"\U0001F642")
st.header('Welcome to MEDITECH')
name=st.text_input('Full name')
age=st.number_input('Age', min_value=1,step=1)
DOB=st.text_input("DOB(DD-MM-YYYY)")
blood=st.text_input('Blood Group')
gender=st.selectbox("Gender",("Male","Female"),)
Insurance=st.text_input('Insurance number')
cn=st.text_input('Your contact number')
Address=st.text_area('Address')
en1=st.text_input('Family contact number 1')
enn1=st.text_input('Name of The contact person')
enr1=st.text_input('Relation to the person')
en2=st.text_input('Family contact number 2')
enn2=st.text_input('Name of The 2-contact person')
enr2=st.text_input('Relation to the 2-person')
allergies=st.text_area('Any allergies')
medical=st.text_area("Past medical history")
medicine=st.text_area('Current medications')
famhis=st.text_area('Family medical history')
con = st.checkbox('Consent to release your medical information to relevant healthcare providers?')
if st.button('Generate QR Code'):
    combined_input = (f"Name: {name}\n"
                      f"Age: {age}\n"
                      f"DOB: {DOB}\n"
                      f"Blood Group: {blood}\n"
                      f"Gender: {gender}\n"
                      f"Insurance Number: {Insurance}\n"
                      f"Contact Number: {cn}\n"
                      f"Address: {Address}\n"
                      f"Emergency Contact 1: {en1}, Name: {enn1}, Relation: {enr1}\n"
                      f"Emergency Contact 2: {en2}, Name: {enn2}, Relation: {enr2}\n"
                      f"Allergies: {allergies}\n"
                      f"Past Medical History: {medical}\n"
                      f"Current Medications: {medicine}\n"
                      f"Family Medical History: {famhis}\n")

    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data(combined_input)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    st.image(img_byte_arr)

    st.download_button(label="Download QR Code", data=img_byte_arr, file_name="qrcode.png", mime="image/png")