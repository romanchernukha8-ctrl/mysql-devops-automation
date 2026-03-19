# MySQL DevOps Automation to docker compose from mysql + phpmyadmin, using python CLI

# descriptoin
This project demonstrates how python CLI can start containers, execute sql, update data and backup database

# Tecnologies
-Python
-Docker
-MySQL
-argparse
-pymysql
-dotenv

# Arhitecture project

Developer
   ↓
Python CLI Tool
   ↓
Docker Compose
   ↓
MySQL + phpMyAdmin Containers
   ↓
Database Operations (SQL / Update / Backup)
   ↓
Backup Files (Local Storage)

# Project structure

## Project Structure

## Project Structure

.
├── new_tull.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── .gitlab-ci.yml
├── backups/
└── README.md

# How to run
1. Git clone https://github.com/romanchernukha8-ctrl/mysql-devops-automation.git
2. python new_tull.py (--disk)

# result

scrinshot


## Mini DevOps Project

- Docker Compose setup for MySQL and phpMyAdmin
- Python CLI tool for:
  - starting and managing containers
  - executing SQL queries
  - updating database records
  - creating database backups

## Technologies

Python, Docker, MySQL, argparse, pymysql, python-dotenv
