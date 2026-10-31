import streamlit as st

st.title("Calculator")
st.write("A simple calculator built with Streamlit")

a = st.number_input("Enter first number:", value=0.0)

b = st.number_input("Enter second number:", value=0.0)

operation = st.selectbox("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])

calculate = st.button("Calculate")

if calculate:
    if operation == "Add":
        result = a + b
    elif operation == "Subtract":
        result = a - b
    elif operation == "Multiply":
        result = a * b
    elif operation == "Divide":
        if b == 0:
            st.error("Cannot divide by zero!")
            result = None
        else:
            result = a / b
    
    if result is not None:
        st.success(f"Result: {result}")