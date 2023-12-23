FROM kivy/buildozer:latest

WORKDIR /app
COPY . /app

# Cria um ambiente virtual e instala as dependências
RUN python3 -m venv venv && \
    /bin/sh -c "source venv/Scripts/activate && pip install -r requirements.txt"

# Inicializa o buildozer
CMD ["/bin/sh", "-c", "source venv/Scripts/activate && buildozer android debug"]
