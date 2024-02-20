import streamlit as st
from streamlit_option_menu import option_menu
import altair as alt
import pandas as pd
import streamlit as st



st.title("Roberto Gonzalez Carranza")

col1, col2 = st.columns([2, 1])

col1.subheader("Developer")
col1.image("./images/aaa.png", caption="This is me!", use_column_width=None)

col2.subheader("Contact")
col2.write( """
    * Trujillo, Perú (GMT-5)
    * (+51) 948907318
    * https://github.com/kirito9623
    * https://www.linkedin.com/in/roberto-gonzalez-developer/
    """)




st.subheader("About me")
st.markdown(
    """I am a technology lover, with a passion for using artificial intelligence, i use
    the system thinking and metalearning to achieve my goals.
    I am always looking for new challenges and opportunities to learn and grow.
    I am passionate about web development, psychology, technology, personal growth and weigth lifting.
    My purpose to help other for help me, and i think the technology is the mean to make a just and free world.
    """)


st.subheader("Technologies")

#horizontal menu
def backend():
   
   df = pd.DataFrame({
     'Technology': ["Linux", "PostgreSQL", "Wordpress", "AWS"],
     'Academy': ["Linux Fundation", "University of Michigan", "Self taught", "AWS"],
     })
   st.write(df)
   

def frontend():
    df = pd.DataFrame({
     'Technology': ["HTML", "CSS", "Sass", "Bootstrap"],
     'Academy': ["TECSUP", "TECSUP", "TECSUP", "TECSUP"],
     })
    st.write(df)

def languages():
     df = pd.DataFrame({
     'Language': ["Python", "Go"],
     'Academy': ["Self Taught", "Kodekloud.com"],
     })
     st.write(df)

def others(): 
     df = pd.DataFrame({
     'Language': ["Git", "Docker", "Technical Support","Civil Engineering"],
     'Academy': ["Kodekloud.com", "Kodekloud.com", "Google", "UPAO(Peru))"],
     })
     st.write(df)


selected2 = option_menu(None, ["Backend", "FrontEnd", "Languages", 'Other'], 
    icons=['database', 'window-fullscreen', "code-square", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Backend":
    backend()
elif selected2 == "FrontEnd":
    frontend()
elif selected2 == "Languages":
    languages()
elif selected2 == "Other":
    others()

##work experience

st.subheader("Work Experience")

with st.expander('Professional reinvention - Work In Progress'):
  st.write("""
    * Professional reinvetion: July 2022 - present
       * DATA ANALYSIS PROJECT: 
       *Title: Portfolio
       *Technologies: Python,Streamlite,Linux
       *Link : https://robertogonzalez.streamlit.app/ --- WORK IN PROGRESS""")

with st.expander('Civil Engineering Entrepreneur'):
  st.write("""
    * GLOBAL INGENIEROS - Part time: January 2016 - present
    * Management of all stages of building safety consulting, being the main client the transnational chain CENCOSUD for Metro, Wong, Paris stores in different cities of Peru.
www.globalingenieros.com""")

with st.expander("Junior Developer (Wordpress,CSS,Html)"):
  st.write("""
    * AC ARQUITECTOS - Part time: January 2022 - March 2023
        * Improvement of the webpage, create forms to filter clients.
        * Improvement of the Front end, using plugins and editing the CSS.
        * Initiation of database in Google Earth.
        * Initiation of Customer tracking using Monday.
        * Creation of Advertising Campaigns with Google ADS.
        * Initiation of use LinkedIn Sales Navigator, 60% more business opportunities.""")

with st.expander("Blog Company Co-founder"):
  st.write("""
    * Pondomedia - Part time: October 2014 - December 2015
        * Company that developed blogs for Spanish-speaking audiences using web analysis and SEO (Search Engine Optimization). SEO (Search Engine Optimization)
   """)



col1, col2 = st.columns([2, 1])

col1.subheader("Skills")
col1.write( """
    * Proactive
    * Fast learner
    * Team worker
    """)

col2.subheader("Spoken Languages")
col2.write( """
    * Spanish: Native
    * English: CEFR English - B2 Upper Intermediate
    """)




