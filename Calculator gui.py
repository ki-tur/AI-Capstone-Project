import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except:
        output.config(text="Error", fg="red")

# Create window
app = tk.Tk()
app.title("Calculator 💖")
app.geometry("300x200")
app.configure(bg="#FFC0CB")  # light pink background

# Input field
entry = tk.Entry(app, font=("Arial", 14), bd=3, relief="ridge", justify="center")
entry.pack(pady=15)

# Add Calculate Button
btn = tk.Button(
    app,
    text="Calculate",
    command=calculate,
    bg="#FF69B4",   # hot pink
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)
btn.pack(pady=10)

# Output label
output = tk.Label(
    app,
    text="",
    bg="#FFC0CB",
    fg="black",
    font=("Arial", 12)
)
output.pack(pady=10)

# Run app
app.mainloop()