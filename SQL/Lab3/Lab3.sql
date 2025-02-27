USE Banking

--branch table
CREATE TABLE branch(
	branch_name VARCHAR(255),
	branch_city VARCHAR(255) NOT NULL UNIQUE,
	assests VARCHAR(255)
	PRIMARY KEY (branch_name)
);

--customers table
CREATE TABLE customers(
	ID INT IDENTITY(1,1), --auto increments
	name VARCHAR(255) NOT NULL,
	address VARCHAR(255),
	PRIMARY KEY (ID)
);

--loan table
CREATE TABLE loan(
	Loan_number INT,
	branch_name VARCHAR(255),
	amount DECIMAL(15,2),
	type VARCHAR(8),
	PRIMARY KEY (Loan_number),
	CONSTRAINT FK_branch_name
	FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
		ON DELETE SET NULL
		ON UPDATE SET NULL,
	CONSTRAINT CHK_loan_amount
		CHECK(amount >= 5000),
	CONSTRAINT CHK_loan_type
		CHECK(type IN('Personal', 'Student', 'Auto'))
);

--borrower table
CREATE TABLE borrower(
	ID INT,
	loan_number INT,
	PRIMARY KEY (ID, loan_number),
	CONSTRAINT FK_ID
	FOREIGN KEY (ID) REFERENCES customers(ID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_loan_number
	FOREIGN KEY (loan_number) REFERENCES loan(loan_number)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

--account table
CREATE TABLE account(
	account_number INT,
	branch_name VARCHAR(255),
	balance DECIMAL(15,2)
	PRIMARY KEY (account_number),
	CONSTRAINT FK_branch_name2
	FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
		ON DELETE SET NULL
		ON UPDATE SET NULL
);

--depositor table
CREATE TABLE depositor(
	ID INT,
	account_number INT,
	PRIMARY KEY (ID, account_number),
	CONSTRAINT FK_ID2
	FOREIGN KEY (ID) REFERENCES customers(ID)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT FK_account_number
	FOREIGN KEY (account_number) REFERENCES account(account_number)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

delete from account;
delete from borrower;
delete from branch;
delete from customers;
delete from depositor;
delete from loan;
-- Branch Table Inserts
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch1', 'New York');
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch2', 'Los Angeles');
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch3', 'Chicago');
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch4', 'Houston');
--INSERT INTO branch (branch_name, branch_city) VALUES ('Branch5', 'Houston');
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch6', 'Phoenix');
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch7', 'Philadelphia');
--INSERT INTO branch (branch_name) VALUES ('Branch8');
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch9', 'San Diego');
INSERT INTO branch (branch_name, branch_city) VALUES ('Branch10', 'Dallas');

-- Customers Table Inserts
INSERT INTO customers (name, address) VALUES ('Alice Smith', '123 Main St');
INSERT INTO customers (name, address) VALUES ('Bob Johnson', '456 Oak Ave');
INSERT INTO customers (name, address) VALUES ('Carol Williams', '789 Pine Ln');
INSERT INTO customers (name, address) VALUES ('David Brown', '101 Elm St');
INSERT INTO customers (name, address) VALUES ('Eve Davis', '222 Maple Dr');
INSERT INTO customers (name, address) VALUES ('Frank Wilson', '333 Willow Ct');
INSERT INTO customers (name, address) VALUES ('Grace Taylor', '444 Redwood Rd');
--INSERT INTO customers (ID, address) VALUES (8, '555 Cedar Pl');
INSERT INTO customers (name, address) VALUES ('Ivy Thomas', '666 Birch Way');
INSERT INTO customers (name, address) VALUES ('Jack Jackson', '777 Oakwood Cir');

-- Loan Table Inserts
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (101, 'Branch1', 6000, 'Personal');
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (102, 'Branch2', 10000, 'Auto');
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (103, 'Branch3', 15000, 'Student');
--INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (104, 'Branch4', 4000, 'Personal');
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (105, 'Branch6', 12000, 'Auto');
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (106, 'Branch6', 18000, 'Student');
--INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (107, 'Branch7', 7000, 'Mortgage');
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (108, 'Branch9', 11000, 'Auto');
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (109, 'Branch9', 16000, 'Student');
INSERT INTO loan (Loan_number, branch_name, amount, type) VALUES (110, 'Branch10', 9000, 'Personal');

-- Borrower Table Inserts
INSERT INTO borrower (ID, loan_number) VALUES (1, 101);
INSERT INTO borrower (ID, loan_number) VALUES (2, 102);
INSERT INTO borrower (ID, loan_number) VALUES (3, 103);
INSERT INTO borrower (ID, loan_number) VALUES (3, 105);
INSERT INTO borrower (ID, loan_number) VALUES (5, 105);
--INSERT INTO borrower (ID, loan_number) VALUES (6, 100);
INSERT INTO borrower (ID, loan_number) VALUES (7, 108);
INSERT INTO borrower (ID, loan_number) VALUES (8, 108);
INSERT INTO borrower (ID, loan_number) VALUES (9, 109);
--INSERT INTO borrower (ID, loan_number) VALUES (11, 110);

-- Account Table Inserts
INSERT INTO account (account_number, branch_name, balance) VALUES (201, 'Branch1', 1000.00);
INSERT INTO account (account_number, branch_name, balance) VALUES (202, 'Branch2', 5000.50);
INSERT INTO account (account_number, branch_name, balance) VALUES (203, 'Branch4', 2500.75);
INSERT INTO account (account_number, branch_name, balance) VALUES (204, 'Branch4', 7500.25);
--INSERT INTO account (account_number, branch_name, balance) VALUES (205, 'Branch55', 12000.99);
INSERT INTO account (account_number, branch_name, balance) VALUES (206, 'Branch6', 3000.00);
INSERT INTO account (account_number, branch_name, balance) VALUES (207, 'Branch6', 9000.50);
INSERT INTO account (account_number, branch_name, balance) VALUES (208, 'Branch9', 6000.25);
INSERT INTO account (account_number, branch_name, balance) VALUES (209, 'Branch9', 15000.75);
INSERT INTO account (account_number, branch_name, balance) VALUES (210, 'Branch10', 4500.99);

-- Depositor Table Inserts
INSERT INTO depositor (ID, account_number) VALUES (1, 201);
INSERT INTO depositor (ID, account_number) VALUES (2, 202);
INSERT INTO depositor (ID, account_number) VALUES (3, 203);
INSERT INTO depositor (ID, account_number) VALUES (4, 204);
INSERT INTO depositor (ID, account_number) VALUES (5, 206);
--INSERT INTO depositor (ID, account_number) VALUES (6, 222);
INSERT INTO depositor (ID, account_number) VALUES (7, 207);
INSERT INTO depositor (ID, account_number) VALUES (8, 208);
INSERT INTO depositor (ID, account_number) VALUES (9, 209);
INSERT INTO depositor (ID, account_number) VALUES (9, 210);

DELETE
FROM branch
WHERE branch_name = 'Branch10';

SELECT * FROM branch;

DELETE
FROM customers
WHERE ID = 5;

SELECT * FROM customers;
