from tkinter import *  # Importing all classes and functions from tkinter for GUI creation

import requests  # Importing requests module to handle HTTP requests


# Function to fetch a quote from the Kanye Rest API
def get_quote():
    response = requests.get(url='https://api.kanye.rest')  # Sending a GET request to the API
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    data = response.json()  # Parsing the JSON response to a dictionary
    quote = data['quote']  # Extracting the quote from the response dictionary
    canvas.itemconfig(quote_text, text=quote)  # Updating the canvas text with the new quote


# Setting up the main window for the GUI
window = Tk()  # Creating a new Tkinter window instance
window.title("Kanye Says...")  # Setting the title of the window
window.config(padx=50, pady=50)  # Adding padding around the window

# Setting up the canvas where the background and quote will be displayed
canvas = Canvas(width=300, height=414)   # Creating a canvas with specified width and height
background_img = PhotoImage(file="background.png")  # Loading the background image
canvas.create_image(150, 207, image=background_img)  # Placing the background image in the center of the canvas
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")  # Adding a placeholder text for the quote in the canvas
canvas.grid(row=0, column=0)  # Positioning the canvas in the first row and column of the grid layout

# Setting up the button that fetches and displays a new quote
kanye_img = PhotoImage(file="kanye.png")  # Loading the image for the button
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)  # Creating the button with the image and linking it to the get_quote function
kanye_button.grid(row=1, column=0)  # Positioning the button in the second row and first column of the grid layout


# Starting the Tkinter event loop
window.mainloop()  # Running the Tkinter event loop, waiting for events like button clicks
