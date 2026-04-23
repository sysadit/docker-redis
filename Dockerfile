FROM python:3.9-alpine

# Bikin user non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy requirement dulu (biar layer cache lebih efisien)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file dari folder app ke image
COPY app/ .

# Ubah kepemilikan file ke user non-root
RUN chown -R appuser:appgroup /app
USER appuser

# Jalankan flask
CMD ["flask", "run", "--host=0.0.0.0"]
