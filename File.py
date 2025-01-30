import tkinter as tk
from tkinter import filedialog, Label, Button, messagebox
from PIL import Image, ImageTk
from model import predict_tumor  # Ensure predict_tumor function is updated as per previous guidance

# Create the main application window
import tkinter as tk

root = tk.Tk()
root.title("Brain Tumour Detection")
root.geometry("1000x1000")

def upload_image():
    # Prompt user to select an image file
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.tif")],
        title="Choose an image for tumour detection"
    )
    if file_path:
        # Display the selected image
        load_and_display_image(file_path)

        # Get prediction result
        try:
            result = predict_tumor(file_path)
            # Display the prediction result
            result_text = f"Tumour Type: {result['Prediction']}\nProbability: {result['Predicted Class Probability']:.4f}"
            result_label.config(text=result_text, fg="blue")
        except Exception as e:
            messagebox.showerror("Prediction Error", "An error occurred while predicting: " + str(e))

def load_and_display_image(file_path):
    # Load and resize image for display in Tkinter
    img = Image.open(file_path)
    img = img.resize((500, 500), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    
    # Update the label to display the image
    img_label.config(image=img)
    img_label.image = img
    img_label_text.config(text="Uploaded Image:")

# Create a label for title
title_label = Label(root, text="Brain Tumour Detection", font=("Helvetica", 16, "bold"), bg="white")
title_label.pack(pady=10)

# Create a button to upload an image
upload_button = Button(root, text="Upload Image", command=upload_image, font=("Arial", 12), bg="green", fg="white")
upload_button.pack(pady=15)

# Label to display the uploaded image
img_label_text = Label(root, text="", font=("Arial", 12), bg="white")
img_label_text.pack()
img_label = Label(root, bg="white")
img_label.pack(pady=10)

# Label to display the prediction result
result_label = Label(root, text="", font=("Arial", 14), bg="white")
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
