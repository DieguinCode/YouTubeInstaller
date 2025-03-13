import os
import subprocess


def download_video(youtube_url, download_path):
    try:
        # Certifique-se de que o diretório existe
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Comando para baixar o vídeo com yt-dlp
        command = [
            "yt-dlp",
            youtube_url,
            "-o", os.path.join(download_path, "%(title)s.%(ext)s"),
            "-f", "bestvideo+bestaudio"
        ]

        # Executando o comando
        subprocess.run(command, check=True)
        print("Vídeo baixado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar o vídeo: {e}")


if __name__ == "__main__":
    # Caminho fixo de download
    download_path = r"C:\Diego\Scripts\youTubeInstaller\Videos"

    # Solicitar o link do YouTube ao usuário
    youtube_url = input("Insira o link do vídeo do YouTube: ").strip()

    # Fazer o download do vídeo
    download_video(youtube_url, download_path)
