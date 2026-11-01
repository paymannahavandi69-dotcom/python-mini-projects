import streamlit as st

st.title("Todo List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("New task:")

add_button = st.button("Add Task")

if add_button and new_task:
    st.session_state.tasks.append(new_task)
    st.success(f"Task '{new_task}' added!")

st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks yet!")
else:
    for i in range(len(st.session_state.tasks)):
        st.write(f"{i + 1}. {st.session_state.tasks[i]}")