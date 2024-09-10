import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    try:
        if st.session_state['new_todo'] == '':
            return
        else:
            new_todo = st.session_state['new_todo']
            todos.append(new_todo + "\n")
            functions.write_todos(todos)
    except:
        return

def clear_text():
    st.session_state['new_todo'] = ''

def on_change_wrapper():
    add_todo()
    clear_text()


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = 'Enter a todo', label_visibility='hidden',
              placeholder="Add a new todo...",
              on_change=on_change_wrapper,
              key = 'new_todo')

st.session_state