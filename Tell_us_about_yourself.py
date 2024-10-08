import streamlit as st

ss = st.session_state

st.set_page_config(
    page_title="Ceevee",
    page_icon="👋",
)

st.write("# Welcome to Ceevee! 👋")

st.subheader("Your CV", divider=True)
st.file_uploader("Upload your LinkedIn CV", type="pdf", accept_multiple_files=False)

# Initialize the session state to store the list
if 'skills' not in ss:
    ss.skills = []
if 'position' not in ss:
    ss.position = ""
if 'whyResponse' not in ss:
    ss.whyResponse = ""
if "currQ" not in ss:
    ss.currQ = ""
if "currRes" not in ss:
    ss.currRes = ""
if "additionalResponses" not in ss:
    ss.additionalResponses = []
if "addMoreInfo" not in ss:
    ss.addMoreInfo = True

# Create a text input field
st.subheader("Your Socials", divider=True)
user_input = st.text_input("LinkedIn:", "")
user_input = st.text_input("Github:", "")
user_input = st.text_input("Twitter:", "")

# When the user submits an item, add it to the list
if user_input:
    ss.skills.append(user_input)
    user_input=""

num_cols = 2
columns = st.columns(num_cols)
for idx, skill in enumerate(ss.skills):
    col_idx = idx % num_cols # Determine which column to use
    with columns[col_idx]:
        st.write("- " + skill)


st.subheader("Other Documents", divider=True)
st.write("Submit other documents to help us personalise your application. Examples include previous cover letters, blog posts, writing samples.")
st.file_uploader("", type="pdf", accept_multiple_files=False)



if st.button("Submit"):
    st.switch_page("pages/1_Your_Profile.py")
