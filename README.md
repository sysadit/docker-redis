# Tugas Dockerize Web Counter (Flask,redis,nginx)

praktikum ini ialah implementasi Docker Compose untuk web sederhana.

## Fitur
- **Python Flask**: Aplikasi web utama.
- **Redis**: In-memory data store untuk counter kunjungan.
- **Nginx**: Reverse proxy untuk menangani request masuk.
- **Security**: Menggunakan user non-root dan Alpine image (Best Practices).

## Cara Menjalankan
Cukup jalankan satu perintah:
```bash
docker compose up -d
