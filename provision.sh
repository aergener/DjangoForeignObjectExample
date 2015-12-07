PROJECT_NAME=$1
DB_NAME=$PROJECT_NAME
POSTGRESQL_VERSION=9.3

# Update apt
sudo apt-get update -y

# Install postgresql & create database for this project
sudo apt-get install -y postgresql-$POSTGRESQL_VERSION postgresql-contrib libpq-dev
sudo -u postgres createdb $DB_NAME
echo "create user $PROJECT_NAME superuser password '$PROJECT_NAME';" | sudo -u postgres psql

# Install pip & python requirements
sudo apt-get install -y python-pip python-psycopg2
sudo pip install -r app/requirements.txt

# Migrate django app
python app/$PROJECT_NAME/manage.py makemigrations
python app/$PROJECT_NAME/manage.py migrate
