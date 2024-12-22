
Task 2: SQL Task

Objective: Evaluate the candidate's SQL skills, including query writing, data manipulation, and problem-solving.

Send the solution as https://www.db-fiddle.com - you can create new public fiddle and share it.
Here is an example: https://www.db-fiddle.com/f/iE2mKFU3ht97C5aMFkLFnd/2 Please don't work in it, use the "Fork" button to create a copy.
You can choose whatever sql flavour you like.

Problem: Work with a database schema and answer questions
Schema:

Table: Customers
CustomerID (Primary Key, INT)
Name (VARCHAR)
City (VARCHAR)
SignupDate (DATE)

Table: Orders
OrderID (Primary Key, INT)
CustomerID (Foreign Key, INT)
OrderDate (DATE)
Amount (FLOAT)
Questions:

Sample data:

INSERT INTO Customers (CustomerID, Name, City, SignupDate) VALUES
(1, 'Alice Johnson', 'New York', '2023-01-15'),
(2, 'Bob Smith', 'Los Angeles', '2023-02-10'),
(3, 'Charlie Davis', 'Chicago', '2023-03-12'),
(4, 'Diana Garcia', 'Houston', '2023-04-05'),
(5, 'Edward Brown', 'Phoenix', '2023-05-20');

INSERT INTO Orders (OrderID, CustomerID, OrderDate, Amount) VALUES
(101, 1, '2023-07-01', 250.50),
(102, 1, '2023-08-15', 300.00),
(103, 2, '2023-07-10', 150.00),
(104, 3, '2023-06-20', 400.00),
(105, 3, '2023-08-05', 220.00),
(106, 4, '2023-05-18', 500.00),
(107, 5, '2023-11-01', 600.00);


1. Use a CTE to find customers who have placed more than one order
Write a query to identify customers who have placed more than one order. Use a Common Table Expression (CTE) to calculate the number of orders per customer.

2. Use a windowing function to select the first 2 orders for each customer
Write a query to return the first two orders (based on OrderDate) for each customer. Use a windowing function with ROW_NUMBER().

4. Customers who made no orders in the last 6 months

5. Calculate the average Amount of orders grouped by the month and year of OrderDate

https://www.db-fiddle.com/f/iUwTZ6rQNgkpW92orpd3e7/2