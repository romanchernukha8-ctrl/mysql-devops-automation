import argparse
import subprocess
import time
import os
from datetime import datetime
from pathlib import Path

import pymysql
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3307")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
}

MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")

BACKUP_DIR = BASE_DIR / "backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser(description="DevOps MYSQL Utility")

parser.add_argument("--disk", help="Show directory listing")
parser.add_argument("--memory", action="store_true", help="Show directory size")
parser.add_argument("--sql", action="store_true", help="Run Docker MySQL + test SELECT")
parser.add_argument("--mysql", action="store_true", help="Find user by name and email")
parser.add_argument("--update", action="store_true", help="Update username by id")
parser.add_argument("--backup", action="store_true", help="Backup MySQL database")

args = parser.parse_args()

def connect_db():
    return pymysql.connect(**MYSQL_CONFIG)

def query_user_by_name_and_email(username: str, email: str):
    with connect_db() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE user_name = %s AND email = %s",
                (username, email),
            )
            result = cursor.fetchall()
            print(result)


def update_user_name(user_id: int, new_name: str):
    with connect_db() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET user_name = %s WHERE id = %s;",
                (new_name, user_id),
            )
            connection.commit()
            print("Rows updated:", cursor.rowcount)

def docker_mysql_test_select():
    env = os.environ.copy()
    env["MYSQL_PWD"] = MYSQL_ROOT_PASSWORD

    subprocess.run(
        ["docker", "compose", "up", "-d"],
        check=True
    )
    print("Waiting for MySQL..")
    time.sleep(8)

    subprocess.run(
        ["docker", "exec",
            "-e", f"MYSQL_PWD={MYSQL_ROOT_PASSWORD}",
            "mysql",
            "mysql",
            "-u", "root",
            os.getenv("MYSQL_DATABASE"),
            "-e", "SELECT * FROM users WHERE id > 3;"
         ],
        env=env,
        check=True
    )

def backup_mysql():
    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = BACKUP_DIR / f"{MYSQL_CONFIG['database']}_{today}.sql"

    env = os.environ.copy()
    env["MYSQL_PWD"] = MYSQL_CONFIG["password"]

    print(f"Create backup: {backup_file}")

    subprocess.run(
        [
            "mysqldump",
            "--no-tablespaces",
            "-h", MYSQL_CONFIG["host"],
            "-P", str(MYSQL_CONFIG["port"]),
            "-u", MYSQL_CONFIG["user"],
            MYSQL_CONFIG["database"]
        ],
        env=env,
        stdout=open(backup_file, "w"),
        check=True
    )
    print("Backup completed successfully.")

if args.disk:
    subprocess.run(["ls", "-a"])
    exit()

if args.memory:
    user_dir = input("Введите название директории: ")
    subprocess.run(["ls", "-lh", user_dir])
    exit()

if args.sql:
    docker_mysql_test_select()
    exit()

if args.mysql:
    user_name = input("Введите user_name: ")
    email = input("Введите email: ")
    query_user_by_name_and_email(user_name, email)
    exit()

if args.update:
    user_id = int(input("Введите ID пользователя: "))
    new_name = input("Введите новое user_name: ")
    update_user_name(user_id, new_name)
    exit()

if args.backup:
    backup_mysql()
    exit()
