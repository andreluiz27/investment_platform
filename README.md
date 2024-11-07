# FastAPI Project

This is a simple FastAPI project that provides a basic API service. Access to the API requires an API key, which must be passed in the `API_KEY` header.

![ Preview of the API](investor_api.png)

## Tasks checklists

- [x] Adjust the readme
  - [x] Explain how start the server
  - [x] Explain how initiate database
  - [ ] Explain how to test the endpoints
  - [x] Put some picture
- [x] Create a makefile to initiate database
- [x] Clean the code
- [x] Implement authentication
- [x] Endpoint to see user account
- [x] Endpoint to see account's position
- [ ] AWS hosting
- [x] Create a mocked database
- [ ] (Maybe) Create tests 
- [ ] HTTPS certified

## Requirements

- Docker & Docker Compose (optional)
- Make (for managing commands)

## Project Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/andreluiz27/investment_platform.git
     ```

2. Run the makefile to start the api and the databse check before if the ports used in compose are opened, if not, make sure to open or change the ports

    ```bash
    make api
    ```
3. Run the make command to create the database

    ```bash
    make init-database:
    ```
4. Load a mocked database
    ```bash
    make load-mocked-db:
    ```






## API Key Authentication

To use this API, you must include the following API key in the request headers:

```text
API_KEY: 452f7377b202e85cd6c34d2b4cbe43be
```