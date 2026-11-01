import streamlit as st

st.title("Contact Manager")

if "contacts" not in st.session_state:
    st.session_state.contacts = []

with st.form("contact_form"):
    st.subheader("Add New Contact")
    name = st.text_input("Name:")
    phone = st.text_input("Phone:")
    email = st.text_input("Email:")
    submit = st.form_submit_button("Add Contact")
    
    if submit and name and phone:
        st.session_state.contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })
        st.success(f"Contact '{name}' added!")

st.divider()

st.subheader("Your Contacts")

if len(st.session_state.contacts) == 0:
    st.info("No contacts yet!")
else:
    for i in range(len(st.session_state.contacts)):
        contact = st.session_state.contacts[i]
        col1, col2 = st.columns([5, 1])
        
        with col1:
            st.write(f"**{contact['name']}**")
            st.caption(f"Phone: {contact['phone']} | Email: {contact['email']}")
        
        with col2:
            if st.button("Delete", key=f"delete_{i}"):
                st.session_state.contacts.pop(i)
                st.rerun()

st.divider()

search = st.text_input("Search by name:")

if search:
    found = False
    for contact in st.session_state.contacts:
        if search.lower() in contact["name"].lower():
            st.write(f"**{contact['name']}**")
            st.caption(f"Phone: {contact['phone']} | Email: {contact['email']}")
            found = True
    
    if not found:
        st.warning("No contact found!")