# OneUrl Backend
This is the backend server of OneUrl platform built with [Fastapi](https://fastapi.tiangolo.com/).

OneUrl is a light-weight platform to get your links in one place and access them with a customizable prefix link.

***Notice: this is the backend server, you'll also need [one-url-panel](https://github.com/Hammered-Dev/one-url-panel) as the frontend UI. Also, further instruction wiil also be there.***
## Required Environment Variables
| Key | Ealue | Example | Importance |
| --- | --- | --- | --- |
| POSTGRES_HOST | PostgreSQL host | localhost  127.0.0.1  db  ...| Required |
| POSTGRES_PORT | PostgreSQL host | 5432  7043  ... | Optional (Default = 5432) |
| POSTGRES_USRNAME | PostgreSQL user name | postgres  ... | Optional (Default = postgres) |
| POSTGRES_PASS | PostgreSQL user password | password  ... | Required if you have |
| POSTGRES_DBMANE | PostgreSQL database name | postgres  ... | Optional (Default = postgres) |
## API docs
The API document will be available under the path below:
1. SwaggerUI: `/docs`
2. Redoc: `/redoc`
## Development
**This project uses [Poetry](https://python-poetry.org/) as package manager, please use poetry if you're going to develop above this project**
### Requirements
1. python >= 3.13
2. vscode or pycharm (any IDE you like)
3. Poetry
### Sync project
```bash
poetry sync
```
