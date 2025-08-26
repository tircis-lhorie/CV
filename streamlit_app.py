import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 

col1, col2, spacer = st.columns(3)

with col1:
    image = Image.open('image/picture.jpeg')
    st.image(image, width=150)
with col2:
    st.mardown('''
    # Lhorie PIRNAY, Ph.D.
    ##### *Resume* 
    ''')

st.markdown("## Summary", unsafe_allow_html=True)
st.info('''
- **Business Intelligence consultant and researcher**, experienced in turning complex data into actionable insights for organizations.  
- **Founder of TIRCIS**, a spin-off project that transforms traditional dashboards into **causal KPI networks** to anticipate the impact of managerial decisions.  
- Strong background in **data analysis, functional design, and digital transformation**, with hands-on expertise in **Power BI, SQL, and Python**.  
- Experienced speaker and trainer, passionate about sharing knowledge in **data governance, strategy maps, and data-driven decision-making**.  
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #87ae73;">
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
        <a class="nav-link" href="#consulting-projects">Consulting Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#research">Research</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact-me">Contact Me</a>
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
    st.markdown(a)
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
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt("**Doctor of Management and Economics**, MINDIT Research Center, *University of Namur*, Belgium",
'2018-2024')
st.markdown('''
- Research thesis entitled *Exploring Causalities in Strategic and Performance Management: A Methodological Framework Proposition to Integrate Hard Data and Experts' Knowledge*
''')

st.markdown("")

txt("**Master's Degree in Business Analysis and Integration**, *University of Namur*, Belgium",
'2016-2018')
st.markdown('''
- Magna Cum Laude
- One semester abroad at Universidad del Pacifico – Lima, Peru
''')

st.markdown("")

txt("**Bachelors in Economics and Management Science**, *University of Namur*, Belgium",
'2013-2016')
st.markdown('''
- Cum Laude
''')

#####################
st.markdown('''
## Work Experience
''')

txt("**Post-doctoral Researcher**, MINDIT Research Center, *University of Namur*, Belgium",
"2024 - present")
st.markdown('''
- Conducted applied research in Business Analysis and Data Integration.  
- Awarded the Win4SpinOff grant to prepare the creation of a university spin-off, focusing on innovative approaches to Business Intelligence and causal analysis.  
- Collaborated with multidisciplinary teams to align research outcomes with practical business applications.  
- Published results and presented findings at both academic conferences and industry-oriented events.  
''')

st.markdown("")

txt("**Co-founder**, *TIRCIS Spin-Off Project*, Namur, Belgium",
"2024 - present")
st.markdown('''
- Co-founded TIRCIS, a project transforming Business Intelligence dashboards into causal-network insights.  
- Developed an innovative approach to anticipate and visualize the impact of managerial decisions through interconnected KPIs.  
- Engaged with partners and clients to validate the solution’s added value for strategic decision-making.  
- Explore more: [Website](https://tircis.be) | [LinkedIn](https://www.linkedin.com/company/tircis)
''')

st.markdown("")

txt("**BI Analyst Freelance**, *LP&GD Consult SRL*, Belgium",
"2024 - present")
st.markdown('''
- Founded my own consulting company, delivering services as Business Analyst, BI Analyst, and Data Analyst (functional analysis, dashboards, and strategic decision support).
''')

st.markdown("")

txt("**Teaching Assistant**, *University of Namur*, Belgium",
"2018 - 2023")
st.markdown('''
Teaching assistant for the following courses:
- Operations Research
- Probability and Statistical Inference
- Mathematics for Economics and Management II
- Mathematics for Economics and Management III
- Operations Management and Business Logistics
- Bloc-1 Project: Integrated Teaching Unit
- Simulation course: Business Game
''')

st.markdown("")

txt("**Chair of the board**, *AFS Programmes Interculturels*, Belgium",
"2021 - 2025")
st.markdown('''
AFS is a non-profit organization specializing in intercultural learning for young people. It mainly focuses on hosting and sending youths on exchange programs abroad. Here are the various roles I have held within the organization:
- Member (2021)
- Secretary (2022)
- Vice chair (2023)
- Chair (2024)
''')

st.markdown("")

txt("**Board member and secretary**, *Fondation AFS Stichting*, Belgium",
"2022 - 2024")
st.markdown('''
FAFSS is a companion foundation for the non-profit AFS organization, accredited by the King Baudouin’s Foundation.
''')

#####################
st.markdown('''
## Consulting Projects
''')

txt("**Functional Analyst**, *Digitalcity.Brussels*",
"Dec. 2024 - present")
st.markdown('''
- Designed and followed up the development of an internal management tool.  
- Collaborated with business teams to gather requirements and translate them into detailed specifications.  
- Contributed to the optimization of internal processes through digitalization.
''')

st.markdown("")

txt("**Power BI Analyst & Project Manager**, *SDS – Sony DepthSensing Solutions*",
"Nov. 2024 - present")
st.markdown('''
- Developed and maintained Power BI reports for financial, logistics, and operational monitoring.  
- Implemented robust data models and associated governance processes.  
- Managed BI projects, including coordination with internal and external stakeholders.
''')

st.markdown("")


txt("**Power BI Consultant**, *EPHEC*",
"August 2024")
st.markdown('''
- Delivered a full Power BI project: data modeling, report creation, and insights presentation.  
- Trained users on reading and interpreting dashboards effectively.
''')

st.markdown("")

txt("**BI Consultant**, *skeyes (ex-Belgocontrol)*",
"2021-2024")
st.markdown('''
- Provided advice on KPI interaction visualizations for the *Strategic Performance Management* unit.  
- Proposed an innovative visual model to support strategic decision-making.
''')

st.markdown("")

txt("**Data Visualization Consultant**, *DataLab (King Baudouin Foundation)*",
"2024")
st.markdown('''
- Built a visualization tool for the *3-30-300 method*.  
- Assessed citizens’ well-being across the Belgian territory.  
- Collaborated with public and non-profit actors to highlight social and environmental impact.
''')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', 'Python, R, SQL')
txt3('Web development', 'PHP, HTML, CSS')
txt3('Visualization and Analysis', 'Power BI, Tableau, Looker Studio, Python (matplotlib, seaborn), R (ggplot2)')
txt3('Data Engineering', 'PostgreSQL, SQLServer')
txt3('Database Management', 'Python (psycopg2), SSMS')
txt3('Project Management', 'Agile (SCRUM), UML, BPMN, GANTT')
txt3('Documentation and Reporting', 'LaTeX, MS Office, Google Suite, Jupyter Notebooks')
txt3('Interpersonal', 'Time Management, Leadership, Strong learning ability, Analytical mindset, Synthesis capability')
txt3('Languages', 'French (Native), English (Fluent), Spanish (Intermediate level)')



#####################
st.markdown('''
## Research
''')

st.markdown("My thesis research entitled “Exploring Causalities in Strategic and Performance Management – A Methodological Framework Proposition to Integrate Hard Data and Experts' Knowledge” aimed to create a network view of the indicators and understand the cause-and-effect relationships between them, helping managers make more informed decisions about their strategy.")
st.markdown("""Published scientific work:

- **Pirnay, L. & Burnay, C. (2021, June).**  
  *Data-Driven Strategy Maps: A Hybrid Approach to Strategic and Performance Management Combining Hard Data and Experts’ Knowledge.*  
  In Proceedings of the Doctoral Consortium Papers Presented at the 33rd International Conference on Advanced Information Systems Engineering (CAiSE’21).

- **Pirnay, L., & Burnay, C. (2022).**  
  *How to build data-driven Strategy Maps? A methodological framework proposition.*  
  Data & Knowledge Engineering, 139, 102019.

- **Pirnay, L., & Burnay, C. (2021, May).**  
  *Data-Driven Causalities for Strategy Maps.*  
  In International Conference on Research Challenges in Information Science. Springer, Cham, pp.409–417.

- **Pirnay, L., Deventer, C., & Amaral de Sousa, V. (2023).**  
  *Providing Customer Value through Non-Fungible Tokens: A Preliminary Study.*  
  Published in The 56th Hawaii International Conference on System Sciences (HICSS56).

- **Deventer, C., Amaral de Sousa, V. & Pirnay, L. (2024).**  
  *NFTByBrands: A Proposed-Value Framework for Analysis and Design of NFT Initiatives.*  
  Full-length paper currently under review in the *International Journal of Electronic Commerce*.

- **Lega, M., Giunta, B., Pirnay, L., Simonofski, A., & Burnay, C. (2024).**  
  *Reducing information overload in e-participation: A data-driven prioritization framework for policy-makers.*  
  International Journal of Information Management Data Insights, 4(2), 100264.
""")




#####################
st.markdown('''
## Contact Me
''')

txt2('LinkedIn', 'https://www.linkedin.com/in/chanin-nantasenamat')
txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
