Mini Project Collection (Flask + MongoDB + Python Tasks)
This project includes several small, beginner-friendly applications built using Flask, MongoDB, and Python libraries like Pandas and Pillow.

Features & Tasks Covered
1. Weather App (API Endpoint)
User enters a city name.

Weather data is fetched from OpenWeatherMap API.

Shows temperature, humidity, weather condition, wind speed, and an icon.

Files:
app.py, templates/index.html, static/style.css



2. Sales Data Processor (CSV Analysis)
Reads a CSV file with sales data.

Calculates total sales for each product category.

Saves results into a new CSV file.

Files:
sales_processor.py, sales_data.csv, category_sales.csv



3. Book Manager with MongoDB
Stores book details in a MongoDB collection.

Performs 3 actions:

Finds books by a specific author.

Finds the most recent book.

Updates the publication year of a book.

File:
mongo_books.py



4. Image Upload & Processing
User uploads an image.

Creates 2 thumbnails (100x100 and 200x200).

Adds a watermark to the original image.

Displays all processed images.

Files:
image_app.py, templates/upload_form.html, uploads/, processed/



How to Run
1. Install Required Packages
pip install flask pillow pandas requests pymongo

2. Start Each Program
➤ Weather App
python app.py
Go to http://localhost:5000

➤ Sales Processor
python sales_processor.py

➤ MongoDB Book Manager
Ensure MongoDB is running, then:
python mongo_books.py

➤ Image Processor
python image_app.py
Open browser: http://localhost:5000

Folder Structure
project/

<img width="186" height="327" alt="image" src="https://github.com/user-attachments/assets/ed94b007-5952-4882-b1d4-f7b225d63703" />


Notes
Make sure MongoDB is running for database scripts.
Internet is needed for the weather app (API call).
Ensure arial.ttf is installed for watermarking.
