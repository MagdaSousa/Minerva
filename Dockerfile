FROM postgres
ENV POSTGRES_PASSWORD localhost
ENV POSTGRES_PASSWORD 4585MLV
ENV POSTGRES_USER desafioMinerva
ENV POSTGRES_DB db_minerva
ENV POSTGRES_PORT 5432
COPY querys.sql /docker-entrypoint-initdb.d/