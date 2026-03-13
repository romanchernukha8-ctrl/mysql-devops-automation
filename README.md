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
GitHub
   ↓
Docker Image
   ↓
AWS ECR
   ↓
Kubernetes (EKS)
   ↓
LoadBalancer
   ↓
User

# Project structure

Структура 

## Project Structure

.
├── app.py
├── requirements.txt
├── Dockerfile
├── k8s
│   ├── deployment.yaml
│   └── service.yaml
└── README.md

# How to run
1. Git clone https://github.com/romanchernukha8-ctrl/mysql-devops-automation.git
2. python new_tull.py (--disk)

# result

scrinshot


Мини DevOps-проект:
- Docker Compose для MySQL + phpMyAdmin
- Python CLI для:
  - запуска контейнеров
  - выполнения SQL-запросов
  - обновления данных
  - резервного копирования базы

Технологии:
Python, Docker, MySQL, argparse, pymysql, dotenv
