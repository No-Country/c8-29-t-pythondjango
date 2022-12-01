# GONG

Gong is a Django project scrapper resposable for sharing a list of vacancies for junior profiles.

<br />

## Built With

- [Python](https://www.python.org/) Language

<br />

## Installation


1. Clone the repo

   ```sh
    git clone https://github.com/No-Country/c8-29-t-pythondjango.git
   ```

<br />

2. Set environment variables: be/.env

   You will need to setup some mandatory environment variables. We recommend adding the following in your local ~/.zshrc:

   ```sh
   # Environment Variables
   STAGE="<STAGE>"
   SECRET_KEY="<SECRET_KEY>"
   DATABASE_NAME="<DATABASE_NAME>"
   DATABASE_USER="<DATABASE_USER>"
   DATABASE_PASSWORD="<DATABASE_PASSWORD>"
   DATABASE_HOST="<DATABASE_HOST>"
   DATABASE_PORT="<DATABASE_PORT>"
   ```

   You will need to replace the placeholders above as follows:
   - `<STAGE>` ->  Set this value according to staging area: EX: "DEV|STG|PROD"
   - `<SECRET_KEY>` -> Set this value to provide cryptographic signing. EX: "!z+rsdv-bilz&tw64=zm"
   - `<DATABASE_NAME>` -> Set this value according to database name. EX: "gong"
   - `<DATABASE_USER>` -> Set this value according to database user. EX: "admin"
   - `<DATABASE_PASSWORD>` -> Set this value according to database password. EX: "a#sda@41"
   - `<DATABASE_HOST>` -> Set this value according to database host. EX: "localhost"
   - `<DATABASE_PORT>` -> Set this value according to database port. EX: 5432

<br />

3. We suggest using docker compose for installing and running the project.

   ```bash
    docker compose up
   ```

<br />

4. Go to:
   ```bash
    http://localhost:8540/
   ```


<br />

## Currently Supported Sites:

- [Indeed](https://mx.indeed.com/?r=us)


<br />

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

<br />

## License

[MIT](https://choosealicense.com/licenses/mit/)