from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import os
import json
import mimetypes
from urllib.parse import quote
from .utils import get_video_info, download_video_or_audio

def index(request):
    return render(request, 'downloader/index.html')

def analyze_video(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)
    
    url = None
    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
            url = data.get('url')
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'JSON inválido.'}, status=400)
    else:
        url = request.POST.get('url')

    if not url:
        return JsonResponse({'status': 'error', 'message': 'Se requiere una URL válida.'}, status=400)
    
    url = url.strip()

    try:
        data = get_video_info(url)
        return JsonResponse({
            'status': 'success',
            'details': data['details'],
            'qualities': data['qualities']
        })
    except ValueError as ve:
        return JsonResponse({'status': 'error', 'message': str(ve)}, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Ocurrió un error inesperado al analizar el video: {str(e)}'
        }, status=500)

def download_file(request):
    url = request.GET.get('url')
    format_id = request.GET.get('format_id', 'best')
    download_type = request.GET.get('type', 'video')
    audio_quality = request.GET.get('audio_quality', '192')

    if not url:
        return HttpResponse("Falta la URL del video.", status=400)

    is_audio = (download_type == 'audio')

    try:
        file_path, display_filename = download_video_or_audio(
            url=url,
            format_id=format_id,
            is_audio=is_audio,
            audio_quality=audio_quality
        )

        if not os.path.exists(file_path):
            return HttpResponse("El archivo no pudo ser descargado en el servidor.", status=500)

        def file_iterator(path, chunk_size=8192):
            try:
                with open(path, 'rb') as f:
                    while True:
                        chunk = f.read(chunk_size)
                        if not chunk:
                            break
                        yield chunk
            finally:
                try:
                    os.remove(path)
                    print(f"[INFO] Cleaned up temporary file: {path}")
                except Exception as e:
                    print(f"[ERROR] Failed to remove temporary file {path}: {e}")

        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type:
            mime_type = 'audio/mpeg' if is_audio else 'video/mp4'

        file_size = os.path.getsize(file_path)
        
        response = StreamingHttpResponse(file_iterator(file_path), content_type=mime_type)
        
        encoded_filename = quote(display_filename)
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{encoded_filename}"
        response['Content-Length'] = file_size
        
        return response

    except ValueError as ve:
        return HttpResponse(f"Error de validación: {str(ve)}", status=400)
    except Exception as e:
        return HttpResponse(f"Error en el servidor al descargar: {str(e)}", status=500)
