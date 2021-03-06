FILE_NAME="development.yml"
USER="jchun2"
DB_NAME="django-app"

build:
	docker compose -f $(FILE_NAME) up --build -d --remove-orphans

up:
	docker compose -f $(FILE_NAME) up -d

down:
	docker compose -f $(FILE_NAME) down

logs:
	docker compose -f $(FILE_NAME) logs

migrate:
	docker compose -f $(FILE_NAME) run --rm api python3 manage.py migrate

makemigrations:
	docker compose -f $(FILE_NAME) run --rm api python3 manage.py makemigrations

collectstatic:
	docker compose -f $(FILE_NAME) run --rm api python3 manage.py collectstatic
	--no-input --clear

superuser:
	docker compose -f $(FILE_NAME) run --rm api python3 manage.py createsuperuser

down-v:
	docker compose -f $(FILE_NAME) down -v

# To inspect volumes
volume:
	docker volume inspect django-src_local_postgres_data

authors-db:
	docker compose -f $(FILE_NAME) exec postgres psql --username=$(USER) --dbname=$(DB_NAME)
