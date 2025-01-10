# 1. Create local `venv`
Using VSCode

# 2. Install packages
#### Dependencies:
```sh
pip install -r requirements.txt
```
#### Server:
```sh
pip install "uvicorn[standard]"
```

# 3. Running
For external terminal activate `venv`
```sh
.\.venv\Scripts\Activate.ps1
```
> To close `venv` run command `deactivate`

Run app
```sh
uvicorn main:app --host 0.0.0.0 --port 5001 --reload
```
