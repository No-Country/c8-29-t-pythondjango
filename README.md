![enter image description here](https://i.ibb.co/Z185qVT/Logo.png)

# Índice

1. [Descripción del proyecto](#descripcion)
2. [Tecnologías aplicadas](#tecnologias)
3. [Integrantes](#roles)
4. [Deploy](#deploy)

<a name="descripcion"></a>

# Descripción

Gong is a Django project scrapper resposable for sharing a list of vacancies for junior profiles.

## Video Promocional

[![IMAGE ALT TEXT](https://i.ibb.co/Z185qVT/Logo.png)](https://www.youtube.com/watch?v=eHo5N90C0MI&ab_channel=EmilioCarrozzino) "StayUp")

## Tecnologias

### **FrontEnd**

-   **JavaScript** &nbsp; <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" rel="nofollow"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript"  width="30" height="30" style="max-width: 100%;"> </a>

### **BackEnd**

-   **Django**&nbsp; <a href="https://nodejs.org" rel="nofollow"> <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/django/django-plain.svg" alt="django" width="40" height="40" style="max-width: 100%;"> </a>

- [Python](https://www.python.org/) Language

### **UI/UX**

-   **Figma**&nbsp; <a href="https://www.figma.com/" rel="nofollow"> <img src="https://camo.githubusercontent.com/ed93c2b000a76ceaad1503e7eb9356591b885227e82a36a005b9d3498b303ba5/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f6669676d612f6669676d612d69636f6e2e737667" alt="figma" width="25" height="25" data-canonical-src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" style="max-width: 100%;"> </a>

| Developer               | Rol      | LinkedIn                                             | GitHub - Behance                    |
| ----------------------- | -------- | ---------------------------------------------------- | ----------------------------------- |
| Emilio Carrozzino            | UX / UI  | https://www.linkedin.com/in/           | https://www.https://github.com/ |
| Lucin Perez          | Backend  | https://www.linkedin.com/in/lucin-perez-725921232/             | https://github.com/lucin21      |
| Carlos Guerrero       | Devops  |                                                      | https://github.com/Carlgro |
| Melany Goncalves         | UX / UI  | https://www.linkedin.com/in/         | https://github.com/github.com/MelyGoncalves/        |




## Installation

1. Clone the repo

   ```sh
    git clone https://github.com/No-Country/c8-29-t-pythondjango.git
   ```

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

3. We suggest using docker compose for installing and running the project.

   ```bash
    docker compose up
   ```

4. Go to:
   ```bash
    http://localhost:8540/
   ```


## Currently Supported Sites:

- [Indeed](https://mx.indeed.com/?r=us)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

[MIT](https://choosealicense.com/licenses/mit/)
