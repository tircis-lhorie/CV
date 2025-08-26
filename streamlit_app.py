import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Lhorie PIRNAY, Ph.D.
##### *Resume* 
''')

image = Image.open('image/picture.jpeg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
- Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Lhorie PIRNAY</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#research">Research</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt("**Doctor of Management and Economics** (Management of Information and Digital Transformation), *University of Namur*, Belgium",
'2018-2024')
st.markdown('''
- Research thesis entitled *Exploring Causalities in Strategic and Performance Management: A Methodological Framework Proposition to Integrate Hard Data and Experts' Knowledge*
''')

txt("**Master's Degree in Business Analysis and Integration**, *University of Namur*, Belgium",
'2016-2018')
st.markdown('''
- Magna Cum Laude
- One semester abroad at Universidad del Pacifico – Lima, Peru
''')

txt("**Bachelors in Economics and Management Science**, *University of Namur*, Belgium",
'2013-2016')
st.markdown('''
- Cum Laude
''')

#####################
st.markdown('''
## Work Experience
''')

txt("**Post-doctoral Researcher**, MINDIT Research Center, University of Namur, Belgium",
"2024 - present")
st.markdown('''
- Conducted applied research in **Business Analysis and Data Integration**.  
- Awarded the **Win4SpinOff grant** to prepare the creation of a university spin-off, focusing on innovative approaches to Business Intelligence and causal analysis.  
- Collaborated with multidisciplinary teams to align research outcomes with **practical business applications**.  
- Published results and presented findings at both **academic conferences** and **industry-oriented events**.  
''')

txt("**Co-founder, TIRCIS Project**, Namur, Belgium",
"2024 - present")
st.markdown('''
- Co-founded **TIRCIS**, a project transforming **Business Intelligence dashboards** into **causal-network insights**.  
- Developed an innovative approach to **anticipate and visualize the impact of managerial decisions** through interconnected KPIs.  
- Engaged with partners and clients to validate the solution’s added value for strategic decision-making.  
- Explore more: [🌐 Website](https://tircis.be) | [💼 LinkedIn](https://www.linkedin.com/company/tircis)
''')

txt("**Founder & Consultant, LP&GD Consult SRL**, Belgium",
"2024 - present")
st.markdown('''
- Founded my own consulting company, delivering services as **Business Analyst**, **BI Analyst**, and **Data Analyst** (functional analysis, dashboards, and strategic decision support).  
- Worked with multiple clients including:  
  - **DigitalCity.brussels** – functional analysis and project management for the Nexus platform (training, conferences, ticketing, billing).  
  - **SONY Depthsensing Solutions** – Business Intelligence dashboards, Finance stack redesign, and advanced data modeling.  
- Provided **strategic insights** and **operational solutions** tailored to clients’ digital transformation needs.  
''')



#####################
st.markdown('''
## Skills
''')
txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')

txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')



#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/chaninn/')
txt2('', 'https://github.com/chaninlab/')
txt2('', 'https://github.com/dataprofessor')
txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
txt2('Publons', 'https://publons.com/a/303133/')
