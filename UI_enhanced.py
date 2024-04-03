import tkinter as tk
import hashlib
import main
def register():
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("users.txt", "a") as f:
        f.write(f"{username}:{hashed_password}\n")
    print("User created successfully.")
    # Close the registration window
    parent.destroy()
    # Open the main window
    main_window.deiconify()

def login():
    username = username_entry.get()
    password = password_entry.get()
    with open("users.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            user, hashed_password = line.strip().split(":")
            if user == username and hashlib.sha256(password.encode()).hexdigest() == hashed_password:
                print("Login successful.")
                # Close the login window
                parent.destroy()
                # Open the main window
                main_window.deiconify()
                return
    print("Invalid username or password.")

def recommend_recipes():
    # Get the ingredients from the text entry
    ingredients = ingredients_entry.get().split()
    recipes = main.recommend_recipe(ingredients)
    lst = list(recipes["recipies"])
    # Clear the previous results
    recipes_listbox.delete(0, tk.END)
    # Add the new recipes to the listbox
    for recipe in lst:
        recipes_listbox.insert(tk.END, recipe)

# Create the main window
main_window = tk.Tk()
main_window.title("Recipe Recommender")
main_window.geometry("500x500")

# Create ingredients label and entry
ingredients_label = tk.Label(main_window, text="Ingredients (separated by spaces)")
ingredients_label.pack()
ingredients_entry = tk.Entry(main_window)
ingredients_entry.pack()

# Create recipes listbox
recipes_label = tk.Label(main_window, text="Recommended Recipes")
recipes_label.pack()
recipes_listbox = tk.Listbox(main_window,width = 50,height = 10)
recipes_listbox.pack()

# Create get recipe button
get_recipe_button = tk.Button(main_window, text="Get Recipe", command=recommend_recipes)
get_recipe_button.pack()

# Create the registration/login window
parent = tk.Tk()
parent.title("Login")
parent.geometry("300x200")

# Create username label and entry
username_label = tk.Label(parent, text="Username")
username_label.pack()
username_entry = tk.Entry(parent)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(parent, text="Password")
password_label.pack()
password_entry = tk.Entry(parent, show="*")
password_entry.pack()

# Create register button
register_button = tk.Button(parent, text="Register", command=register)
register_button.pack()

# Create login button
login_button = tk.Button(parent, text="Login", command=login)
login_button.pack()

# Hide the main window initially
main_window.withdraw()

# Start the Tkinter event loop
parent.mainloop()