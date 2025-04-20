import os
import streamlit as st

# Define the directory to save files
directory = r"C:\Users\HASEEB\Desktop\project4"  # <-- Change this if needed

# Define the Library class
class Library:
    def __init__(self, book, author, progress):
        self.book = book
        self.author = author
        self.progress = progress

    def __str__(self):
        return f"Book: {self.book}\nAuthor: {self.author}\nProgress: {self.progress}\n"

# Make sure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Streamlit UI
st.title("Book Library Manager")

menu = ["Add a Book", "Remove a Book", "Search for a Book", "View All Books"]
choice = st.sidebar.radio("Menu", menu)

file_name = st.text_input("Enter your file name (no extension):", "my_books").strip()
file_path = os.path.join(directory, f"{file_name}.txt")

# 1. Add a Book
if choice == "Add a Book":
    st.subheader("Add a New Book")
    book = st.text_input("Book Title").capitalize()
    author = st.text_input("Author").capitalize()
    progress = st.text_input("Progress").capitalize()

    if st.button("Add Book"):
        if book and author and progress:
            new_book = Library(book, author, progress)
            with open(file_path, "a") as file:
                file.write(str(new_book))
            st.success(f"Book '{book}' added to {file_name}.txt")
        else:
            st.error("Please fill in all the fields.")

# 2. Remove a Book
elif choice == "Remove a Book":
    st.subheader("Remove a Book")
    remove_book = st.text_input("Enter Book Title to Remove").capitalize()

    if st.button("Remove Book"):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file
