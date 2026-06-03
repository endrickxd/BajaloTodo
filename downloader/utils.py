import os
import yt_dlp
import uuid
from django.conf import settings

DURATION_LIMIT = 1800

def get_video_info(url):
    url = url.strip()
    if "youtube.com" in url or "youtu.be" in url:
        raise ValueError("La descarga de videos de YouTube se encuentra actualmente en desarrollo.")
    return extract_ytdlp_info(url)

def extract_ytdlp_info(url):
    ydl_opts = {
        'skip_download': True,
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            raise ValueError(f"No se pudo extraer información del enlace. Error: {str(e)}")
        
        if not info:
            raise ValueError("No se pudo obtener información del video.")

        duration = info.get('duration')
        if duration and duration > DURATION_LIMIT:
            raise ValueError(
                f"El video es demasiado largo ({int(duration // 60)} minutos). "
                f"El límite máximo es de {int(DURATION_LIMIT // 60)} minutos."
            )

        extractor = info.get('extractor', '').lower()
        platform = "default"
        if "instagram" in extractor:
            platform = "instagram"
        elif "tiktok" in extractor:
            platform = "tiktok"
        elif "facebook" in extractor:
            platform = "facebook"
        elif "twitter" in extractor or "x.com" in url or "twitter.com" in url:
            platform = "twitter"

        details = {
            'title': info.get('title', 'Video de redes sociales'),
            'thumbnail': info.get('thumbnail') or info.get('thumbnails', [{}])[-1].get('url', ''),
            'duration': duration,
            'duration_formatted': format_duration(duration),
            'author': info.get('uploader') or info.get('creator') or 'Desconocido',
            'platform': platform,
            'url': url
        }

        qualities = []
        qualities.append({
            'format_id': 'best',
            'resolution': 'Calidad Máxima',
            'extension': 'mp4',
            'size_formatted': 'Desconocido',
            'is_custom_combo': False
        })

        return {
            'details': details,
            'qualities': qualities
        }

def download_video_or_audio(url, format_id, is_audio=False, audio_quality='192'):
    url = url.strip()
    if "youtube.com" in url or "youtu.be" in url:
        raise ValueError("La descarga de videos de YouTube se encuentra actualmente en desarrollo.")
    return download_ytdlp(url, format_id, is_audio, audio_quality)

def download_ytdlp(url, format_id, is_audio=False, audio_quality='192'):
    if not os.path.exists(settings.DOWNLOADS_DIR):
        os.makedirs(settings.DOWNLOADS_DIR, exist_ok=True)

    unique_id = str(uuid.uuid4())
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }

    if is_audio:
        outtmpl = os.path.join(settings.DOWNLOADS_DIR, f"{unique_id}.%(ext)s")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': audio_quality,
            }],
        })
    else:
        outtmpl = os.path.join(settings.DOWNLOADS_DIR, f"{unique_id}.%(ext)s")
        ydl_opts.update({
            'format': format_id,
            'outtmpl': outtmpl,
            'merge_output_format': 'mp4',
        })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'video')
        clean_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c in ' -_']).strip() or "download"
        
        ydl.download([url])

        target_ext = 'mp3' if is_audio else 'mp4'
        expected_path = os.path.join(settings.DOWNLOADS_DIR, f"{unique_id}.{target_ext}")

        if not os.path.exists(expected_path):
            files = os.listdir(settings.DOWNLOADS_DIR)
            found = False
            for f in files:
                if f.startswith(unique_id):
                    expected_path = os.path.join(settings.DOWNLOADS_DIR, f)
                    target_ext = f.split('.')[-1]
                    found = True
                    break
            if not found:
                raise FileNotFoundError("El archivo descargado no pudo ser encontrado en el servidor.")

        display_filename = f"{clean_title}.{target_ext}"
        return expected_path, display_filename

def format_duration(seconds):
    if not seconds:
        return "Desconocido"
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

def format_size(bytes_sz):
    if not bytes_sz:
        return "Desconocido"
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_sz < 1024.0:
            return f"{bytes_sz:.1f} {unit}"
            break
        bytes_sz /= 1024.0
    return f"{bytes_sz:.1f} TB"
