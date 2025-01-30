import tkinter as tk
from tkinter import filedialog, Label, Button, messagebox
import os
from PIL import Image, ImageTk
from model import predict_tumor  # Ensure predict_tumor function is updated as per previous guidance

# Create the main application window
root = tk.Tk()
root.title("Brain Tumour Detection")
root.geometry("1000x1000")

def upload_folder():
    # Prompt user to select a folder
    folder_path = filedialog.askdirectory(title="Choose a folder for tumour detection")
    if folder_path:
        # Initialize a list to store the images and predictions
        images_info = []
        
        try:
            # Loop through each file in the folder
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tif')):
                    # Get prediction result for the image
                    result = predict_tumor(file_path)
                    images_info.append((file_path, result))
            
            # Display the images in a grid with predictions
            display_images_in_grid(images_info)
        except Exception as e:
            messagebox.showerror("Prediction Error", "An error occurred while predicting: " + str(e))

def display_images_in_grid(images_info):
    # Clear any previously displayed images and labels
    for widget in grid_frame.winfo_children():
        widget.destroy()

    # Set the number of columns for the grid
    columns = 4
    
    # Loop through images and predictions, place them in a grid
    for index, (img_path, result) in enumerate(images_info):
        # Load and resize the image for display
        img = Image.open(img_path)
        img = img.resize((350, 350), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        # Create labels to display the image
        img_label = Label(grid_frame, image=img_tk, relief="solid", width=350, height=350)
        img_label.image = img_tk  # Keep a reference to avoid garbage collection

        # Place the image in the grid
        row = index // columns
        col = index % columns
        img_label.grid(row=row*2, column=col, padx=10, pady=10)  # Image goes in the first row of its grid slot

        # Create a label to show the prediction result below the image
        result_text = f"{result['Prediction']}\n{result['Predicted Class Probability']:.4f}"
        result_label = Label(grid_frame, text=result_text, font=("Arial", 10), anchor="center", width=20)
        result_label.grid(row=row*2+1, column=col, padx=10, pady=5, sticky="n")  # Prediction text goes in the second row

# Create a label for title
title_label = Label(root, text="Brain Tumour Detection", font=("Helvetica", 16, "bold"), bg="white")
title_label.pack(pady=10)

# Create a button to upload a folder
upload_button = Button(root, text="Upload Folder", command=upload_folder, font=("Arial", 12), bg="green", fg="white")
upload_button.pack(pady=15)

# Create a Canvas and Scrollbar to make the result area scrollable
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# Create a Frame to contain the result label inside the canvas
scrollable_frame = tk.Frame(canvas)

# Create a window on the canvas to place the scrollable frame
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Update the scrollable region of the canvas whenever the content changes
def update_scrollregion(event):
    canvas.config(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", update_scrollregion)

# Frame to hold the grid of images
grid_frame = tk.Frame(scrollable_frame)
grid_frame.pack()

# Run the Tkinter event loop
root.mainloop()
