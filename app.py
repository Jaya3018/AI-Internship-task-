import json
import tkinter as tk
from tkinter import scrolledtext

# Load the dataset
with open('dataset.json', 'r') as f:
    data = json.load(f)

# Create a dictionary with lowercase keys and exact responses
conversation_dict = {
    "hello": "Hi there!",
    "how are you?": "I’m good, thanks! How about you?",
    "what’s your name?": "I’m Grok, nice to meet you!",
    "what can you do?": "I can chat with you and help with simple tasks.",
    "goodbye": "See you later!"
}

# Function to predict response with lenient matching
def predict_response(user_input):
    user_input = user_input.lower().strip()  # Normalize input
    # Direct match
    if user_input in conversation_dict:
        return conversation_dict[user_input]
    # Check for key phrases in the input
    if "hello" in user_input:
        return conversation_dict["hello"]
    if "how are you" in user_input:
        return conversation_dict["how are you?"]
    if "name" in user_input:
        return conversation_dict["what’s your name?"]
    if "can you" in user_input or "help" in user_input:
        return conversation_dict["what can you do?"]
    if "bye" in user_input or "goodbye" in user_input:
        return conversation_dict["goodbye"]
    return "Sorry, I don’t understand."

# Function to handle sending a message
def send_message():
    user_input = entry.get().strip()
    if user_input:
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = predict_response(user_input)
        chat_window.insert(tk.END, "Bot: " + response + "\n")
        entry.delete(0, tk.END)
    chat_window.see(tk.END)

# Create the main window
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")

# Create chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
chat_window.pack(padx=10, pady=10)

# Create input field
entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=5)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Bind Enter key to send_message
root.bind('<Return>', lambda event: send_message())

# Start the application
root.mainloop()