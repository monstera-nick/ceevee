import streamlit as st

st.title("Your profile!")
st.write("Here is the data we gathered. Please double check the information is correct")

st.subheader("Personal Details", divider=True)
with st.form("personal_details"):
   summary = st.text_area("Summary", "Backend Software Engineer with experience in building scalable, reliable systems and optimizing workflows for performance. Skilled in cloud infrastructure, backend architecture, and full-stack development. Passionate about creating secure, user-centric solutions and collaborating with cross-functional teams to drive success.")
   name = st.text_input("First Name", "Pranav")
   name = st.text_input("Last Name", "Narahari")

   st.form_submit_button('Save changes')

st.subheader("Your Work Experience", divider=True)
with st.form("work_experience"):
    description = st.text_area("AI Coder @ Outlier AI, Inc",
         "Developing and refining backend solutions to enhance AI model performance and ensure system reliability in production environments."
         "\n\n"
         "Collaborating cross-functionally to code backend solutions in Python and Java, optimizing for scalability and safety in AI systems.")

    description = st.text_area("Freelance Software Consultant",
         "Designed scalable blockchain services for secure, zero-code contract creation."
         "\n\n"
         "Led full-stack development, optimizing performance and user experience with TypeScript, MongoDB, and Rust."
         "\n\n"
         "Revamped web tools, securing the first paying customer and reducing user-facing errors by 50%."
         )

    description = st.text_area("Citizens",
         "Spearheaded digital transformation projects, automating the migration of hundreds of applications from on-prem to cloud, reducing migration time by 95%."
         "\n\n"
         "Owned end-to-end development for internal on-prem to cloud migration services, improving system reliability and scaling cloud training API infrastructure."
         "\n\n"
         "Achieved a 95% reduction in migration time (from 3 weeks to 30 minutes) through backend automation and optimization of AWS infrastructure."
         )
    st.form_submit_button('Save changes')

st.subheader("Your Skills", divider=True)

import streamlit as st

# Initialize the list in session state if it doesn't already exist
if 'my_list' not in st.session_state:
    st.session_state['my_list'] = []

# Display the list and provide a delete button for each item
st.session_state["my_list"] = [
    "Python",
    "Java",
    "TypeScript",
    "AWS",
    "Distributed Systems",
    "Automation",
    "React.js / Vue.js",
    "Solidity / Web3",
    "Cloud Migration & Automation",
    "TDD / Unit Testing"
]

for i, item in enumerate(st.session_state['my_list']):
    col1, col2 = st.columns([8, 2])  # To arrange items with delete buttons
    with col1:
        st.write(item)
    with col2:
        if st.button('Delete', key=i):  # Each button needs a unique key
            pass

# Add new item
new_item = st.text_input("Add a new item to the list")
if st.button('Add Item'):
    if new_item:  # Only add if there is some text
        st.session_state['my_list'].append(new_item)


if st.button("Go to job application"):
    st.switch_page("pages/2_Job Application.py")
