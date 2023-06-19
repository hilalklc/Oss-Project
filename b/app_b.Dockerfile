FROM python:3.9

# Çalışma dizinini /app olarak ayarlıyoruz
WORKDIR /app

# requirements.txt dosyasını kopyalıyoruz
COPY requirements.txt .

# requirements.txt'deki paketleri kuruyoruz
RUN pip install --no-cache-dir -r requirements.txt

# b_application.py dosyasını kopyalıyoruz
COPY app_b.py .

# CMD komutu ile python b_application.py komutunu çalıştırıyoruz
CMD ["python", "app_b.py"]
