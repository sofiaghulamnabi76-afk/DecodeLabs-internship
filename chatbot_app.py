import tkinter as tk
from tkinter import scrolledtext

# Bot Response Function
def get_response(user):
    user = user.lower().strip()

    if user == "hello":
        return "Hello! How are you?"

    elif user == "hi":
        return " Hi! Nice to meet you SOPHIA ."

    elif user == "how are you":
        return " I'm fine. Thanks for asking!"

    elif user == "your name":
        return " My name is RuleBot."

    elif user == "who made you":
        return " I was created using Python."

    elif user == "thanks":
        return " You're welcome!"

    elif user == "good morning":
        return "Good Morning!"

    elif user == "good night":
        return " Good Night!"

    elif user == "help":
        return """ Available Commands

 hello
 hi
 how are you
 your name
 who made you
 thanks
 good morning
 good night
 bye
"""

    elif user == "bye":
        return " Goodbye! Have a nice day."

    else:
        return " Sorry! I don't understand. Type 'help'."
# Send Message
def send_message(event=None):
    user = entry.get().strip()

    if user == "":
        return

    response = get_response(user)

    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, " You: " + user + "\n", "user")
    chat.insert(tk.END, " Bot: " + response + "\n\n", "bot")
    chat.config(state=tk.DISABLED)

    chat.yview(tk.END)
    entry.delete(0, tk.END)

# Quick Buttons
def send_text(text):
    entry.delete(0, tk.END)
    entry.insert(0, text)
    send_message()
# Clear Chat
def clear_chat():
    chat.config(state=tk.NORMAL)
    chat.delete(1.0, tk.END)

    chat.insert(tk.END, " Welcome to AI ChatBot!\n", "bot")
    chat.insert(tk.END, "Type 'help' to see available commands.\n\n", "bot")

    chat.config(state=tk.DISABLED)
# Main Window
root = tk.Tk()
#root.iconbitmap("icon.ico")
root.title("🤖 AI Desktop ChatBot - Version 2.0")

# Window automatically maximized
root.state("zoomed")

# Minimum size
root.minsize(900, 600)

# Allow resizing
root.resizable(True, True)

# Background
root.configure(bg="#121212")
# Header
header = tk.Label(
    root,
    text=" AI ChatBot",
    bg="#075E54",
    fg="white",
    font=("Arial", 18, "bold"),
    pady=12,
)

header.pack(fill=tk.X)

# Chat Area
chat = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    bg="#1E1E1E",
    fg="white",
    font=("Calibri", 12),
)

chat.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

chat.tag_config("user", foreground="#25D366", font=("Calibri", 12, "bold"))
chat.tag_config("bot", foreground="#00BFFF", font=("Calibri", 12))

chat.config(state=tk.NORMAL)
chat.insert(tk.END, "🤖 Welcome to AI Desktop ChatBot!\n", "bot")
chat.insert(tk.END, "Hello! I'm your personal AI Assistant.\n", "bot")
chat.insert(tk.END, "Type 'help' to see all commands.\n\n", "bot")
chat.config(state=tk.DISABLED)

# Entry
entry = tk.Entry(
    root,
    font=("Calibri", 13),
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
)

entry.pack(fill=tk.X, padx=10, pady=5)

entry.bind("<Return>", send_message)

# Send Button
send_btn = tk.Button(
    root,
    text="📤 Send",
    bg="#25D366",
    fg="white",
    font=("Arial", 11, "bold"),
    command=send_message,
)

send_btn.pack(pady=5)


# Quick Buttons

frame = tk.Frame(root, bg="#121212")
frame.pack(pady=5)

tk.Button(frame, text="😊 Hello", command=lambda: send_text("hello")).grid(row=0, column=0, padx=5)

tk.Button(frame, text="📖 Help", command=lambda: send_text("help")).grid(row=0, column=1, padx=5)

tk.Button(frame, text="👋 Bye", command=lambda: send_text("bye")).grid(row=0, column=2, padx=5)
tk.Button(
    frame,
    text="😂 Joke",
    command=lambda: send_text("tell me a joke")
).grid(row=0, column=3, padx=5)

# Clear Button
clear = tk.Button(
    root,
    text="🧹 Clear Chat",
    bg="red",
    fg="white",
    command=clear_chat,
)

clear.pack(pady=10)
# Footer
footer = tk.Label(
    root,
    text="❤️ Developed by SOPHIA | AI Desktop ChatBot v2.0",
    bg="#121212",
    fg="gray",
    font=("Arial", 10),
)

footer.pack(pady=5)

root.mainloop()