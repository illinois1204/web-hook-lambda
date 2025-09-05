# 1. Create local `venv`
```sh
python -m venv .venv
```
```sh
py -3.x -m venv .venv
```

# 2. Install packages
Activate `venv`
```sh
.\.venv\Scripts\Activate.ps1
```
> To close `venv` run command `deactivate`
```sh
pip install -r requirements.txt
```

# 3. Running
Run app with command or using VSCode launch
```sh
uvicorn app.main:app --host 0.0.0.0 --port 5001 --env-file .env --reload
```
