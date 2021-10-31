import tkinter as tk
import requests
import json

window = tk.Tk()

greeting = tk.Label(text="Movie Details",
                    fg="yellow",
                    bg="black",
                    width=30,
                    height=2)
greeting.pack(fill=tk.BOTH)

frm_user_entry = tk.Frame(master=window)

lbl_movie_name = tk.Label(master=frm_user_entry, text="Enter the movie name: ", height=5, width=40)
lbl_movie_name.pack(side=tk.LEFT, fill=tk.X)

entry = tk.Entry(master=frm_user_entry, width=40)
entry.pack(side=tk.LEFT, fill=tk.X)
frm_user_entry.pack(fill=tk.BOTH) # comment

"""
this is a comment
"""

def fetch_data():
    m_name = entry.get()
    URL = "http://www.omdbapi.com/?t=" + m_name + "&apikey=xxxxxxxx"
    response = requests.get(URL)
    d_response = json.loads(response.text)
    title = d_response["Title"]
    year = d_response["Year"]
    genre = d_response["Genre"]
    director = d_response["Director"]
    plot = d_response["Plot"]
    txt_data.insert(tk.END, f'{title} ({year}) directed by {director} falls under the genre of {genre}. The plot is: {plot}.\n\n')

frm_btn = tk.Frame(master=window, height=20)

button = tk.Button(text="Get movie info",
                    width=20,
                    command=fetch_data)
button.pack()
frm_btn.pack()

txt_data = tk.Text()
txt_data.pack()

window.mainloop()
