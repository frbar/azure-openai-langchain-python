$file = $args[0]
$allGood = $true

if (-not $env:AZURE_OPENAI_API_KEY) {
    Write-Host "AZURE_OPENAI_API_KEY is not configured."
    $allGood = $false
}

if (-not $env:AZURE_OPENAI_ENDPOINT) {
    Write-Host "AZURE_OPENAI_ENDPOINT is not configured."
    $allGood = $false
}

if (-not $allGood) {
    Write-Host "Please configure the environment variables and try again."
    exit 1
}

if (-not $file) {
    Write-Host "Please provide a file to process."
    exit 1
}

if (-not (Test-Path $file)) {
    Write-Host "File does not exist."
    exit 1
}

## Build and run the docker container

docker build -t langchain-poc .

docker run -e OPENAI_API_KEY=$env:AZURE_OPENAI_API_KEY `
           -e OPENAI_API_BASE=$env:AZURE_OPENAI_ENDPOINT `
           -e FILE=$file `
           langchain-poc