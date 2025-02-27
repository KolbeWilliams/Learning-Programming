use ECommerce

--Customers Table
CREATE TABLE Customers (
	customer_id INT,
	first_name VARCHAR(15),
	middle_initial CHAR(1),
	last_name VARCHAR(15),
	email VARCHAR(30),
	phone VARCHAR(15),
	address VARCHAR(30)
	PRIMARY KEY (customer_id)
);

--Products Table
CREATE TABLE Products (
	product_id INT,
	name VARCHAR(30),
	description VARCHAR(250),
	price DECIMAL(10,2),
	category_id INT,
	image_url VARCHAR(100),
	stock_quantity INT,
	PRIMARY KEY (product_id)
);

--Orders Table
CREATE Table Orders (
	order_id INT,
	customer_id INT,
	order_date VARCHAR(10),
	total_amount INT,
	status VARCHAR(15),
	PRIMARY KEY (order_id)
);

--Items Table
CREATE TABLE Items (
	item_id INT,
	order_id INT,
	product_id INT,
	quantity INT,
	unit_price INT
	PRIMARY KEY (item_id)
);

--Categories Table
CREATE TABLE Categories (
	category_id INT,
	name VARCHAR(30),
	PRIMARY KEY (category_id)
);

--Reviews Table
CREATE TABLE Reviews (
	review_id INT,
	product_id INT,
	customer_id INT,
	rating DECIMAL(10,2),
	comment VARCHAR(100)
	PRIMARY KEY (review_id)
);

--Add the foreign keys
ALTER TABLE Products
ADD FOREIGN KEY (category_id) REFERENCES Categories(category_id)

ALTER TABLE Orders
ADD FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)

ALTER TABLE Items
ADD FOREIGN KEY (order_id) REFERENCES Orders(order_id)

ALTER TABLE Items
ADD FOREIGN KEY (product_id) REFERENCES Products(product_id)

ALTER TABLE Reviews
ADD FOREIGN KEY (product_id) REFERENCES Products(product_id)

ALTER TABLE Reviews
ADD FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)