<h1 align="center">Hi there, I'm Maksat 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">nFactorial Incubator - отборочный тур</h3>

This is a simple CRUD (Create, Read, Update, Delete) system written in Python using JSON file as the database. 
It allows the user to perform basic operations on a list of products, including creating a new product, viewing all products, 
updating an existing product, deleting a product, and sorting the products.

## Getting Started

Before using the system, you need to make sure that you have the latest version of Python and the json module installed. 
The json module is a standard Python library and does not require additional installation.

To use the program, follow these steps:
1. Clone this repository to your local machine using the command
```console
git clone https://github.com/nazarbekmb/NoSQL_database.git
```
2. Run the program by executing the CRUD.py file using the command
```console
python mainv.py
```

## Usage

1. Creating Data
To create new data in the JSON file, run the script and enter "1" at the prompt. You will be asked to enter the product ID, name, and diagonal. If the product ID already exists in the file, the system will prompt you to enter a new product ID. Once you enter all the information, the system will save it to the JSON file.

2. Reading Data
To view the data in the JSON file, run the script and enter "2" at the prompt. The system will display all the data in the file, including the product ID, name, and diagonal.

3. Updating Data
To update existing data in the JSON file, run the script and enter "3" at the prompt. You will be asked to enter the product ID of the data you want to update. If the product ID exists, the system will prompt you to enter the new name and diagonal values. Once you enter the new values, the system will save them to the JSON file.

4. Deleting Data
To delete existing data from the JSON file, run the script and enter "4" at the prompt. You will be asked to enter the product ID of the data you want to delete. If the product ID exists, the system will delete the data from the JSON file.

5. Sorting Data
To sort the data in the JSON file, run the script and enter "5" at the prompt. You will be prompted to choose how you want to sort the data: by product ID, name, or diagonal. Once you choose a sorting method, the system will sort the data and display it.

6. Exiting the System
To exit the system, run the script and enter "6" at the prompt. The system will close.

*Note: The JSON file must be named "product.json" and be located in the same directory as the Python script.*

## Feedback
If you liked this project, I would be grateful if you could add Star to the repository.
