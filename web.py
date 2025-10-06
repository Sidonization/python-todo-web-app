import streamlit as st
import functions
import os


if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, "w") as file_local:
        pass

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.set_todos(todos)
    st.session_state["new_todo"] = ""


st.title("TODO web app")
st.subheader("You can enter and complete TODO items in this app")

st.text_input(label="Enter a todo",
              placeholder="Type here then press enter",
              on_change=add_todo,
              key="new_todo")

st.write("List of TODOs")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()
