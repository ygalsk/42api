# Use a Debian/Ubuntu base image
FROM ubuntu:latest

# Install PostgreSQL and dependencies
RUN apt-get update && apt-get install -y \
    sudo\
    postgresql \
    postgresql-contrib \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Expose PostgreSQL port
EXPOSE 5432

# Initialize PostgreSQL database (optional, you can modify this as needed)
RUN service postgresql start && \
    sudo -u postgres psql -c "CREATE DATABASE ${POSTGRES_DB};" && \
    sudo -u postgres psql -c "CREATE USER ${POSTGRES_USER} WITH PASSWORD '${POSTGRES_PASSWORD}';" && \
    sudo -u postgres psql -c "ALTER ROLE ${POSTGRES_USER} SET client_encoding TO 'utf8';" && \
    sudo -u postgres psql -c "ALTER ROLE ${POSTGRES_USER} SET default_transaction_isolation TO 'read committed';" && \
    sudo -u postgres psql -c "ALTER ROLE ${POSTGRES_USER} SET timezone TO 'UTC';" && \
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ${POSTGRES_DB} TO ${POSTGRES_USER};"

# Start PostgreSQL server
CMD ["postgres"]