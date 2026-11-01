import streamlit as st

st.title("Banking System")

if "accounts" not in st.session_state:
    st.session_state.accounts = [
        {"owner": "Arash", "balance": 1000, "type": "Savings"},
        {"owner": "Kourosh", "balance": 500, "type": "Checking"}
    ]

if "history" not in st.session_state:
    st.session_state.history = []

with st.form("account_form"):
    st.subheader("Add New Account")
    owner = st.text_input("Owner Name:")
    balance = st.number_input("Initial Balance:", min_value=0.0, value=0.0)
    account_type = st.selectbox("Account Type:", ["Savings", "Checking"])
    submit = st.form_submit_button("Add Account")
    
    if submit and owner:
        st.session_state.accounts.append({
            "owner": owner,
            "balance": balance,
            "type": account_type
        })
        st.success(f"Account '{owner}' added!")

st.divider()

st.subheader("Accounts")

if len(st.session_state.accounts) == 0:
    st.info("No accounts yet!")
else:
    for i in range(len(st.session_state.accounts)):
        acc = st.session_state.accounts[i]
        col1, col2 = st.columns([5, 1])
        
        with col1:
            st.write(f"**{acc['owner']}** - {acc['type']}")
            st.caption(f"Balance: {acc['balance']:,}")
        
        with col2:
            if st.button("Delete", key=f"del_acc_{i}"):
                st.session_state.accounts.pop(i)
                st.rerun()

st.divider()

st.subheader("Transaction")

if len(st.session_state.accounts) > 0:
    account_names = [acc["owner"] for acc in st.session_state.accounts]
    selected = st.selectbox("Choose Account:", account_names)
    
    col1, col2 = st.columns(2)
    
    with col1:
        amount = st.number_input("Amount:", min_value=0.0, value=0.0)
    
    with col2:
        st.write("")
        st.write("")
        deposit = st.button("Deposit")
        withdraw = st.button("Withdraw")
    
    account = st.session_state.accounts[account_names.index(selected)]
    
    if deposit and amount > 0:
        account["balance"] = account["balance"] + amount
        st.session_state.history.append(f"DEPOSIT: {amount} to {selected} | Balance: {account['balance']}")
        st.success(f"Deposited {amount} to {selected}!")
        st.rerun()
    
    if withdraw and amount > 0:
        if amount > account["balance"]:
            st.error("Insufficient funds!")
        else:
            account["balance"] = account["balance"] - amount
            st.session_state.history.append(f"WITHDRAW: {amount} from {selected} | Balance: {account['balance']}")
            st.success(f"Withdrew {amount} from {selected}!")
            st.rerun()

st.divider()

st.subheader("Transaction History")

if len(st.session_state.history) == 0:
    st.info("No transactions yet!")
else:
    for record in st.session_state.history:
        st.write(record)