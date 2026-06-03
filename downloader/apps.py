from django.apps import AppConfig
import os

class DownloaderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'downloader'

    def ready(self):
        try:
            import static_ffmpeg
            print("[INFO] Initializing static-ffmpeg paths...")
            static_ffmpeg.add_paths()
            print("[INFO] static-ffmpeg paths initialized successfully.")
        except Exception as e:
            print(f"[WARNING] Failed to initialize static-ffmpeg: {e}")

