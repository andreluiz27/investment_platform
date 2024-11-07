# FastAPI Project

This is a simple FastAPI project that provides a basic API service. Access to the API requires an API key, which must be passed in the `API_KEY` header.

![ Preview of the API](coin_api.png)

## Tasks checklists

- [x] Adjust the readme
  - [ ] Explain how start the server
  - [ ] Explain how initiate database
  - [ ] Explain how to test the endpoints
  - [ ] Put some picture
- [ ] Create a makefile to initiate database
- [ ] Clean the code
- [x] Implement authentication
- [x] Endpoint to see user account
- [x] Endpoint to see account's position
- [ ] AWS hosting
- [ ] Create a mocked database
- [ ] (Maybe) Create tests 

## Requirements

- Docker & Docker Compose (optional)
- Make (for managing commands)

## Project Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-fastapi-project.git
    cd your-fastapi-project
    ```

2. Run the makefile

    ```bash
    make api
    ```
3. Go to localhost/docs

4. Click in the padlock icon and put the API KEY that you can find below    


## API Key Authentication

To use this API, you must include the following API key in the request headers:

```text
API_KEY: 452f7377b202e85cd6c34d2b4cbe43be
```