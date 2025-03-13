import os
import subprocess


def download_video(youtube_url, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        command = [
            "yt-dlp",
            "--merge-output-format", "mp4",  # Garante saída final como MP4
            youtube_url,
            "-o", os.path.join(download_path, "%(title)s.%(ext)s"),
            "-f", "bestvideo+bestaudio"
        ]

        subprocess.run(command, check=True)
        print("Vídeo baixado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar o vídeo: {e}")


if __name__ == "__main__":

    path = input("Digite o caminho para a pasta que vai receber o video: ")

    download_path = os.path.join(path, "")

    youtube_url = input("Insira o link do vídeo do YouTube: ").strip()

    download_video(youtube_url, download_path)
