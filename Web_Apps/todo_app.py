import streamlit as st

st.title("Todo List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("New task:")

add_button = st.button("Add Task")

if add_button and new_task:
    st.session_state.tasks.append({"text": new_task, "done": False})
    st.success(f"Task '{new_task}' added!")

st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks yet!")
else:
    for i in range(len(st.session_state.tasks)):
        task = st.session_state.tasks[i]
        col1, col2, col3 = st.columns([6, 1, 1])
        
        with col1:
            if task["done"]:
                st.write(f"✓ {task['text']}")
            else:
                st.write(f"○ {task['text']}")
        
        with col2:
            if st.button("✓", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = True
                st.rerun()
        
        with col3:
            if st.button("🗑", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()