FROM python:3.10
WORKDIR /PY_PROJETO
COPY .        
RUN pip install -r requirements.txt
CMD ["python", "seu_programa.py"]
