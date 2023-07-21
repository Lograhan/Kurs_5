-- создание таблиц в БД postgress.
-- 1. Создание таблицы с компаниями.

CREATE TABLE company
(
	company_id int PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	vacancy_count int NOT NULL
);

-- 2. Создание таблиц с вакансиями.

CREATE TABLE vacancy
(
	vacancy_id int PRIMARY KEY,
	vacancy_name varchar (150) NOT NULL,
	company_id int REFERENCES company(company_id) ON DELETE CASCADE,
	salary_min int,
	salary_max int,
	url varchar (50)
);