install-local:
	python -m pip install --upgrade pip
	pip install -r requirements_local.txt --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"
