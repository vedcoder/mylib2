CREATE TABLE books (id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL, author VARCHAR(50) NOT NULL,
    story VARCHAR(100) NOT NULL, link VARCHAR(400) NOT NULL,
    status ENUM('read','not read','in progress') NOT NULL,
    price DECIMAL(5,2) NOT NULL,
    primary key (id)
    );

INSERT INTO BOOKS VALUES (1,'TOM GATES SUPER GOOD SKILLs',
	'liz pichon','a boy with with SUPER GOOD SKILL',
	'http://www.amazon.in/Tom-Gates-10-Skills-Almost/dp/9386041901/ref=sr_1_1?ie=UTF8&qid=1487394064&sr=8-1&keywords=tom+gates+super+good+skills',
	'read',269.0);
