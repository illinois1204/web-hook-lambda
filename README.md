# 1. Create local `venv`
Using VSCode

# 2. Install packages
```sh
pip install -r requirements-dev.txt
```

# 3. Running
For external terminal activate `venv`
```sh
.\.venv\Scripts\Activate.ps1
```
> To close `venv` run command `deactivate`

Run app with command or using VSCode launch
```sh
uvicorn app.main:app --host 0.0.0.0 --port 5001 --env-file .env --reload
```
