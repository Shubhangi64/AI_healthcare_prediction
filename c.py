import os
import numpy as np
import pickle
import streamlit as st

from a import diabetes_prediction
from heart import heart_disease_prediction


from PIL import Image
from streamlit_option_menu import option_menu


import streamlit.components.v1 as components

working_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    if selected =="Login":
                    components.html("""<!-- partial:index.partial.html -->
            <section>
            <div class="form-box">
                <div class="form-value">
                <form action="">
                    <h2>Login</h2>
                    <div class="inputbox">
                    <ion-icon name="mail-outline"></ion-icon>
                    <input type="email" required>
                    <label for="">Email</label>
                    </div>
                    <div class="inputbox">
                    <ion-icon name="lock-closed-outline"></ion-icon>
                    <input type="password" required>
                    <label for="">Password</label>
                    </div>
                    <div class="forget">
                    <label>
                        <input type="checkbox"> Remember me
                    </label>
                    <label>
                        <a href="#">Forgot password?</a>
                    </label>
                    </div>
                    <button>Log in</button>
                    <div class="register">
                    <p>Don't have a account ? <a href="#">Register</a></p>
                    </div>
                </form>
                </div>
            </div>
            </section>
            <!-- partial -->
            <script src='https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js'></script>
            <script src='https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js'></script>""")
                        
    if selected=="Home":
      # bg = """
      # <style>
      # [data-testid="stAppBlockViewContainer"]
      # {
      # background-image: url("home.jpg");
      # background-image: cover;
      # }
      # </style>"""
      
      # st.markdown(bg,unsafe_allow_html=True)
      i=Image.open("images.png")
      st.image(i,width=100)
      
      st.header("WELCOME TO HEALTHIFY  :hospital:" ,
          divider="red")
      with st.container():
            c1,c2 = st.columns([1,2])
      st.subheader("What we do :")
      st.write("##")
      st.write(
            """
            - Detect diseases early by analyzing patient data.
            - Personalize treatment plans based on individual factors.
            - Optimize resource allocation in healthcare.
            - Promote preventive measures to improve health outcomes.
            - Accelerate medical research and innovation.
            - Reduce healthcare costs by addressing issues proactively.
            """)
      
    if selected=="About Us":
      
      im=Image.open("images.png")
      st.image(im,width=100)

      st.subheader("Welcome to Healthify")
      
      cl1, cl2 = st.columns(2)
      with cl1:
            st.write("We are transforming your traditional way of clinic into Al-based and healthy modern twist. Here we use modern ML algorithms to achieve the health-care goals.")
            st.write("##")
            st.write("""This application is based on Machine Learning and Deep Learning Intelligence to make things simple from pateint side as well as Doctor's side. This will help to minimize the efforts applied by doctors or somewhere reduce the dependencies on the doctors. Most
                  useful featues of our healthify is :
                  --An Intelligence Symptom checker.
                  --Diagnosing various Diseases faster.
                  --Able to detect earlier stage of Heart, Liver and Diabetes.
                  """)
      with cl2:
             ima=Image.open("diabetes 2.jpg")
             st.image(ima,width=400)


           
 



    if selected=="Services": 
      #st.title(f"WELCOME {selected}")
            select = option_menu(
                            menu_title= None,
                            options = ["Diabetes","Heart Disease","Liver Disease"],
                            icons=["capsule-pill","heart-pulse","capsule"],
                            default_index=0,
                            orientation="horizontal"
                    ) 
            
            if select=="Diabetes":
                   with st.container():
                        # page title
                        st.title('Diabetes Prediction using ML :pill: ')
                        
                        
                        # getting the input data from the user
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            Pregnancies = st.text_input('Number of Pregnancies')
                            
                        with col2:
                            Glucose = st.text_input('Glucose Level')
                        
                        with col3:
                            BloodPressure = st.text_input('Blood Pressure value')
                        
                        with col1:
                            SkinThickness = st.text_input('Skin Thickness value')
                        
                        with col2:
                            Insulin = st.text_input('Insulin Level')
                        
                        with col3:
                            BMI = st.text_input('BMI value')
                        
                        with col1:
                            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
                        
                        with col2:
                            Age = st.text_input('Age of the Person')
                        
                        # code for Prediction
                        diagnosis = ''
                        
                        # creating a button for Prediction
                        
                        if st.button('Diabetes Test Result'):
                            diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
                            
                            
                        st.success(diagnosis)



            if select=="Heart Disease":
                with st.container():
                        # page title
                        st.title('Heart Disease Prediction using ML :pill:')
                        col1, col2, col3 = st.columns(3)
    
                        with col1:
                              age = st.number_input('Age')
        
                        with col2:
                              sex = st.number_input('Sex')
        
                        with col3:
                              cp = st.number_input('Chest Pain types')
        
                        with col1:
                              trestbps = st.number_input('Resting Blood Pressure')
        
                        with col2:
                              chol = st.number_input('Serum Cholestoral in mg/dl')
        
                        with col3:
                              fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
                        with col1:
                              restecg = st.number_input('Resting Electrocardiographic results')
        
                        with col2:
                              thalach = st.number_input('Maximum Heart Rate achieved')
        
                        with col3:
                              exang = st.number_input('Exercise Induced Angina')
        
                        with col1:
                              oldpeak = st.number_input('ST depression induced by exercise')
        
                        with col2:
                              slope = st.number_input('Slope of the peak exercise ST segment')
        
                        with col3:
                              ca = st.number_input('Major vessels colored by flourosopy')
        
                        with col1:
                              thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
                        Heart_diagnosis = ''
    
                        # creating a button for Prediction
    
                        if st.button('Diabetes Test Result'):
                            Heart_diagnosis = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
            
                        st.success(Heart_diagnosis)
        

    
    
            if select=="Liver Disease":
                st.title('Liver Disease  Prediction using ML :pill:')





if __name__ == '__main__':
    st.set_page_config(page_title="AI Healthcare System",
                   page_icon="🩺",
                   layout="wide"
                   )
    

    with st.sidebar:
        selected = option_menu(
            menu_title= "Healthify",
            options = ["Login","Home","About Us","Services"],
            icons=["lock","house","envelope","clipboard2-pulse"],
            default_index=0,
            menu_icon = "activity",
            #orientation="horizontal"
      )
    
    main()
