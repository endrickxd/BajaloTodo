import os
import yt_dlp
import uuid
import requests
import logging
import re
from django.conf import settings

logger = logging.getLogger(__name__)

DURATION_LIMIT = 1800

COBALT_INSTANCES = [
    "https://apicobalt.mgytr.top",
    "https://dog.kittycat.boo",
    "https://api.cobalt.liubquanti.click",
    "https://cobaltapi.cjs.nz",
    "https://cobaltapi.kittycat.boo",
    "https://fox.kittycat.boo",
    "https://cobalt.alpha.wolfy.love",
    "https://subito-c.meowing.de",
    "https://api.qwkuns.me",
    "https://cobaltapi.squair.xyz",
    "https://grapefruit.clxxped.lol",
    "https://lime.clxxped.lol",
    "https://nuko-c.meowing.de",
]

def fetch_from_cobalt(url, is_audio=False):
    payload = {
        "url": url,
        "filenamePattern": "pretty"
    }
    if is_audio:
        payload["isAudioOnly"] = True
        payload["aFormat"] = "mp3"
    else:
        payload["vQuality"] = "max"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    for instance in COBALT_INSTANCES:
        try:
            logger.info(f"[COBALT] Trying Cobalt instance: {instance} for URL: {url}")
            response = requests.post(instance, json=payload, headers=headers, timeout=12)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") in ["tunnel", "redirect"] and data.get("url"):
                    return data
                elif data.get("status") == "picker":
                    picker_items = data.get("picker", [])
                    if picker_items:
                        return {
                            "status": "tunnel",
                            "url": picker_items[0].get("url"),
                            "filename": picker_items[0].get("filename") or "download.mp4"
                        }
            else:
                logger.warning(f"[COBALT] Instance {instance} returned status code {response.status_code}")
        except Exception as e:
            logger.warning(f"[COBALT] Error connecting to Cobalt instance {instance}: {str(e)}")
            continue
    return None

def download_via_cobalt(url, is_audio=False):
    if not os.path.exists(settings.DOWNLOADS_DIR):
        os.makedirs(settings.DOWNLOADS_DIR, exist_ok=True)

    cobalt_data = fetch_from_cobalt(url, is_audio)
    if not cobalt_data:
        raise ValueError("No se pudo descargar el archivo a través del fallback de Cobalt. Por favor, intente con otro enlace o más tarde.")

    download_url = cobalt_data.get("url")
    cobalt_filename = cobalt_data.get("filename") or ("download.mp3" if is_audio else "download.mp4")

    # Clean the filename for presentation
    clean_title = "".join([c for c in cobalt_filename if c.isalpha() or c.isdigit() or c in ' -_._']).strip() or "download"
    if not clean_title.endswith('.mp3') and not clean_title.endswith('.mp4'):
        clean_title = clean_title + (".mp3" if is_audio else ".mp4")

    unique_id = str(uuid.uuid4())
    target_ext = 'mp3' if is_audio else 'mp4'
    expected_path = os.path.join(settings.DOWNLOADS_DIR, f"{unique_id}.{target_ext}")

    # Stream the file from the Cobalt tunnel/redirect URL and save it locally
    try:
        response = requests.get(download_url, stream=True, timeout=60)
        response.raise_for_status()
        with open(expected_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        if os.path.exists(expected_path):
            try:
                os.remove(expected_path)
            except:
                pass
        raise ValueError(f"Error al descargar desde el servidor de Cobalt: {str(e)}")

    return expected_path, clean_title

def get_video_info(url):
    url = url.strip()
    try:
        # Try extract using yt_dlp
        return extract_ytdlp_info(url)
    except Exception as e:
        logger.warning(f"[YTDLP] Failed to extract info for {url}, falling back to Cobalt. Error: {str(e)}")
        
        # Determine platform
        platform = "default"
        if "instagram.com" in url:
            platform = "instagram"
        elif "tiktok.com" in url:
            platform = "tiktok"
        elif "facebook.com" in url or "fb.watch" in url:
            platform = "facebook"
        elif "twitter.com" in url or "x.com" in url:
            platform = "twitter"
        elif "youtube.com" in url or "youtu.be" in url:
            platform = "youtube"

        # Validate with Cobalt first before serving default preview
        cobalt_data = fetch_from_cobalt(url)
        if not cobalt_data:
            raise ValueError(f"No se pudo procesar el enlace. Verifica que el enlace sea correcto y de una plataforma soportada.")

        title = cobalt_data.get("filename")
        if title:
            if "." in title:
                title = ".".join(title.split(".")[:-1])
        else:
            title = f"Video de {platform.capitalize()}"

        title = title.replace("_", " ").replace("-", " ").strip()

        # Generate YT thumbnail if youtube, else logo.jpg fallback
        video_thumbnail = "/static/downloader/images/logo.jpg"
        if platform == "youtube":
            yt_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
            if yt_id_match:
                video_thumbnail = f"https://img.youtube.com/vi/{yt_id_match.group(1)}/0.jpg"

        details = {
            'title': title,
            'thumbnail': video_thumbnail,
            'duration': None,
            'duration_formatted': "Desconocido",
            'author': "Desconocido",
            'platform': platform,
            'url': url
        }

        qualities = [{
            'format_id': 'cobalt',
            'resolution': 'Calidad Máxima',
            'extension': 'mp4',
            'size_formatted': 'Desconocido',
            'is_custom_combo': False
        }]

        return {
            'details': details,
            'qualities': qualities
        }

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
    if format_id != 'cobalt':
        try:
            return download_ytdlp(url, format_id, is_audio, audio_quality)
        except Exception as e:
            logger.warning(f"[YTDLP] download failed, trying Cobalt fallback. Error: {str(e)}")

    # Fallback/Primary download using Cobalt
    return download_via_cobalt(url, is_audio)

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
