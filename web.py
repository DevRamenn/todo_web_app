import streamlit as st
import functions

todos = functions.get_todo_list()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("my To-Do App")
st.subheader("Manage To-Do Lists")
st.write("Your To-Do Lists")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Write Todo", placeholder="Add a new todo...", on_change=add_todo,
              key="new_todo")

# st.session_state
