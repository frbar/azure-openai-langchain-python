# Getting started

Configure environment variables first:
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`

```powershell

docker build -t langchain-poc .
docker run -e OPENAI_API_KEY=$env:AZURE_OPENAI_API_KEY `
           -e OPENAI_API_BASE=$env:AZURE_OPENAI_ENDPOINT `
           -e FILE=joke.py `
           langchain-poc

```