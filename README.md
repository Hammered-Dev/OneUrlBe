# OneUrl Backend
This project is the backend server of the OneUrl platform built with [FastAPI](https://fastapi.tiangolo.com/).

OneUrl is a light-weight platform to get your links in one place and access them with a customizable prefix link.

⚠️Warning: Currently, the security functionality has not been implemented yet. Please don't use it in a production environment; using it personally also carries your own risk.

***Notice: this is the backend server, you'll also need [one-url-panel](https://github.com/Hammered-Dev/one-url-panel) as the frontend UI. Also, further instructions will be there.***
## Required Environment Variables
| Key | Ealue | Example | Importance |
| --- | --- | --- | --- |
| POSTGRES_HOST | PostgreSQL host | localhost  127.0.0.1  db  ...| Required |
| POSTGRES_PORT | PostgreSQL host | 5432  7043  ... | Optional (Default = 5432) |
| POSTGRES_USRNAME | PostgreSQL user name | postgres  ... | Optional (Default = postgres) |
| POSTGRES_PASS | PostgreSQL user password | password  ... | Required if you have |
| POSTGRES_DBMANE | PostgreSQL database name | postgres  ... | Optional (Default = postgres) |
| CORS_ALLOWED_ORIGINS | Allowed CORS origin | Optional |
| REDIS_HOST | Redis host | localhost  127.0.0.1  redis  ... | Required |
| REDIS_PORT | Redis port | 6379  ... | Optional (Default = 6379) |
| REDIS_DB | Redis db number | Optional (Default = 0) |

## API docs
The API document will be available under the path below:
1. SwaggerUI: `/docs`
2. Redoc: `/redoc`
## Development
**This project uses [Poetry](https://python-poetry.org/) as a project manager. Please use poetry if you're going to develop above this project**
### Requirements
1. Python >= 3.13
2. VSCode or PyCharm (any IDE you like)
3. Poetry
### Sync project
```bash
poetry sync
```

