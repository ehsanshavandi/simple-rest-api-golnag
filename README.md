# simple-rest-api-golnag
This is a simple rest api using beego framework 

## Installation

Install simple-rest-api-golnag with npm

```bash
  go mod tidy
```
    
## Running Tests

To run performance tests, run the following command

```bash
  cd tests && locust -f locust-test.py -H http://localhost:8080
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/ehsanshavandi/simple-rest-api-golnag.git
```

Go to the project directory

```bash
  cd simple-rest-api-golnag
```

Install dependencies

```bash
  go mod tidy
```

Start the server

```bash
  bee run -downdoc=true  -gendoc=true
```

