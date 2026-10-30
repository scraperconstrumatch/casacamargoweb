"""Publicación manual: solo index.html en la raíz de la cuenta FTP."""
import hashlib
import io
import os
from pathlib import Path
import ssl
from ftplib import FTP_TLS


def digest(data):
    return hashlib.sha256(data).hexdigest()


def retrieve(ftp, name):
    output = io.BytesIO()
    ftp.retrbinary("RETR " + name, output.write)
    return output.getvalue()


def publish(ftp, content):
    if b"<html" not in content.lower() or b"Casa Camargo" not in content:
        raise ValueError("El archivo local no parece ser la página Casa Camargo.")
    # La cuenta publicador tiene public_html como raíz. No entrar en subcarpetas.
    ftp.cwd("/")
    previous = retrieve(ftp, "index.html")
    if b"Casa Camargo" not in previous:
        raise ValueError("La página remota no coincide. Revisar la raíz FTP antes de publicar.")
    if previous == content:
        print("La página ya coincide; no se modificó ningún archivo.")
        return
    backup = "index-respaldo-" + digest(previous) + ".html"
    ftp.storbinary("STOR " + backup, io.BytesIO(previous))
    if retrieve(ftp, backup) != previous:
        raise ValueError("No se pudo verificar el respaldo; publicación cancelada.")
    temporary = "index-pendiente-" + digest(content) + ".html"
    ftp.storbinary("STOR " + temporary, io.BytesIO(content))
    if retrieve(ftp, temporary) != content:
        raise ValueError("La transferencia no coincide; publicación cancelada.")
    ftp.rename(temporary, "index.html")
    if retrieve(ftp, "index.html") != content:
        raise ValueError("La verificación final falló; conservar y restaurar el respaldo.")
    print("index.html publicado y verificado. Respaldo: " + backup)


def main():
    names = ("FTP_SERVER", "FTP_USERNAME", "FTP_PASSWORD")
    if not all(os.environ.get(name) for name in names):
        raise ValueError("Faltan secretos FTP.")
    content = (Path(__file__).resolve().parents[1] / "index.html").read_bytes()
    with FTP_TLS(context=ssl.create_default_context(), timeout=60) as ftp:
        ftp.connect(os.environ["FTP_SERVER"], 21)
        ftp.login(os.environ["FTP_USERNAME"], os.environ["FTP_PASSWORD"])
        ftp.prot_p()
        ftp.set_pasv(True)
        publish(ftp, content)


if __name__ == "__main__":
    main()
