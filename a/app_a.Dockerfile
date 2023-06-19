FROM python:3.9

# Çalışma dizinini /app olarak ayarlıyoruz
WORKDIR /app

# requirements.txt dosyasını kopyalıyoruz
COPY requirements.txt .

# requirements.txt'deki paketleri kuruyoruz
RUN pip install --no-cache-dir -r requirements.txt

# a_application.py dosyasını kopyalıyoruz
COPY app_a.py .

# CMD komutu ile python a_application.py komutunu çalıştırıyoruz
CMD ["python", "app_a.py"]
