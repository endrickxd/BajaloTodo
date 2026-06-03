document.addEventListener('DOMContentLoaded', () => {
    const analyzeForm = document.getElementById('analyze-form');
    const videoUrlInput = document.getElementById('video-url');
    const submitBtn = document.getElementById('submit-btn');
    
    const loadingSection = document.getElementById('loading-section');
    const errorCard = document.getElementById('error-card');
    const errorMessage = document.getElementById('error-message');
    const closeErrorBtn = document.getElementById('close-error');
    const resultSection = document.getElementById('result-section');
    
    const videoThumbnail = document.getElementById('video-thumbnail');
    const videoDuration = document.getElementById('video-duration');
    const platformBadge = document.getElementById('platform-badge');
    const videoTitle = document.getElementById('video-title');
    const videoAuthor = document.getElementById('video-author');
    
    const videoOptionsBody = document.getElementById('video-options-body');
    const audioOptionsBody = document.getElementById('audio-options-body');
    
    let currentVideoUrl = '';

    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');
    
    if (localStorage.getItem('theme') === 'light') {
        document.body.classList.add('light-theme');
        themeIcon.className = 'fa-solid fa-sun';
    } else {
        document.body.classList.remove('light-theme');
        themeIcon.className = 'fa-solid fa-moon';
    }
    
    themeToggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('light-theme');
        const isLight = document.body.classList.contains('light-theme');
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
        themeIcon.className = isLight ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
    });

    const platformDemoButtons = document.querySelectorAll('.platform-tag');
    platformDemoButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            if (btn.disabled || btn.hasAttribute('disabled')) return;
            
            const currentVal = videoUrlInput.value.trim();
            const demoUrl = btn.getAttribute('data-url');
            
            if (currentVal === '') {
                if (demoUrl) {
                    videoUrlInput.value = demoUrl;
                    videoUrlInput.focus();
                    submitAnalysis(demoUrl);
                }
            } else {
                videoUrlInput.focus();
                submitAnalysis(currentVal);
            }
        });
    });

    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const targetTab = btn.getAttribute('data-tab');
            document.querySelectorAll('.tab-content').forEach(panel => {
                panel.classList.remove('active');
            });
            document.getElementById(targetTab).classList.add('active');
        });
    });

    closeErrorBtn.addEventListener('click', () => {
        errorCard.classList.add('hidden');
    });

    analyzeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const url = videoUrlInput.value.trim();
        if (url) {
            submitAnalysis(url);
        }
    });

    async function submitAnalysis(url) {
        currentVideoUrl = url;

        errorCard.classList.add('hidden');
        resultSection.classList.add('hidden');
        loadingSection.classList.remove('hidden');
        
        videoUrlInput.disabled = true;
        submitBtn.disabled = true;

        try {
            const csrfTokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
            const csrfToken = csrfTokenInput ? csrfTokenInput.value : '';

            const response = await fetch('/analyze/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ url: url })
            });

            if (!response.ok) {
                const text = await response.text();
                throw new Error(text || `Error ${response.status}`);
            }

            const data = await response.json();
            
            if (data.status === 'success') {
                displayResults(data.details, data.qualities);
            } else {
                showError(data.message || 'No se pudo analizar el enlace.');
            }
        } catch (error) {
            console.error('Error analyzing url:', error);
            if (error.message && error.message.includes('CSRF')) {
                showError('Error de validación de seguridad (CSRF). Por favor recarga la página.');
            } else {
                showError('No se pudo procesar la URL. Verifica que sea un enlace de Facebook, Twitter (X), Instagram o TikTok.');
            }
        } finally {
            loadingSection.classList.add('hidden');
            videoUrlInput.disabled = false;
            submitBtn.disabled = false;
        }
    }

    function displayResults(details, qualities) {
        videoThumbnail.src = '/static/downloader/images/logo.jpg';
        videoDuration.textContent = details.duration_formatted;
        
        platformBadge.className = 'platform-badge';
        platformBadge.innerHTML = '';
        if (details.platform === 'youtube') {
            platformBadge.classList.add('youtube');
            platformBadge.innerHTML = '<i class="fa-brands fa-youtube"></i>';
        } else if (details.platform === 'instagram') {
            platformBadge.classList.add('instagram');
            platformBadge.innerHTML = '<i class="fa-brands fa-instagram"></i>';
        } else if (details.platform === 'tiktok') {
            platformBadge.classList.add('tiktok');
            platformBadge.innerHTML = '<i class="fa-brands fa-tiktok"></i>';
        } else if (details.platform === 'facebook') {
            platformBadge.classList.add('facebook');
            platformBadge.innerHTML = '<i class="fa-brands fa-facebook"></i>';
        } else if (details.platform === 'twitter') {
            platformBadge.classList.add('twitter');
            platformBadge.innerHTML = '<i class="fa-brands fa-x-twitter"></i>';
        }

        videoTitle.textContent = details.title;
        videoAuthor.textContent = details.author;

        videoOptionsBody.innerHTML = '';
        if (qualities && qualities.length > 0) {
            qualities.forEach(q => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${q.resolution}</strong></td>
                    <td><span class="platform-tag btn-sm" style="cursor:default">${q.extension.toUpperCase()}</span></td>
                    <td>${q.size_formatted}</td>
                    <td class="text-right">
                        <button class="btn btn-download btn-sm video-dl-btn" data-format="${q.format_id}">
                            <i class="fa-solid fa-download"></i> Descargar
                        </button>
                    </td>
                `;
                
                const dlBtn = tr.querySelector('.video-dl-btn');
                dlBtn.addEventListener('click', () => {
                    triggerDownload(dlBtn, q.format_id, 'video');
                });
                
                videoOptionsBody.appendChild(tr);
            });
        } else {
            videoOptionsBody.innerHTML = `<tr><td colspan="4" class="text-muted text-center">No hay calidades de video disponibles.</td></tr>`;
        }

        audioOptionsBody.innerHTML = '';
        const audioQualities = [
            { label: 'Alta Calidad', bitrate: '320 kbps', val: '320' },
            { label: 'Calidad Media', bitrate: '192 kbps', val: '192' },
            { label: 'Ahorro de Datos', bitrate: '128 kbps', val: '128' }
        ];

        audioQualities.forEach(a => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><strong>${a.label}</strong></td>
                <td><span class="platform-tag btn-sm" style="cursor:default">MP3</span></td>
                <td>${a.bitrate}</td>
                <td class="text-right">
                    <button class="btn btn-download btn-sm audio-dl-btn" data-bitrate="${a.val}">
                        <i class="fa-solid fa-music"></i> Descargar MP3
                    </button>
                </td>
            `;

            const dlBtn = tr.querySelector('.audio-dl-btn');
            dlBtn.addEventListener('click', () => {
                triggerDownload(dlBtn, 'bestaudio', 'audio', a.val);
            });

            audioOptionsBody.appendChild(tr);
        });

        document.getElementById('tab-video-btn').click();
        resultSection.classList.remove('hidden');
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    const successToast = document.getElementById('success-toast');
    const closeToastBtn = document.getElementById('close-toast');
    let toastTimer;

    function showSuccessToast() {
        if (!successToast) return;
        successToast.classList.remove('hidden');
        void successToast.offsetWidth;
        successToast.classList.add('show');
        
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => {
            hideSuccessToast();
        }, 6000);
    }

    function hideSuccessToast() {
        if (!successToast) return;
        successToast.classList.remove('show');
        setTimeout(() => {
            successToast.classList.add('hidden');
        }, 400);
    }

    if (closeToastBtn) {
        closeToastBtn.addEventListener('click', () => {
            clearTimeout(toastTimer);
            hideSuccessToast();
        });
    }

    function triggerDownload(button, formatId, type, bitrate = '') {
        button.classList.add('downloading');
        const originalHtml = button.innerHTML;
        button.innerHTML = `<i class="fa-solid fa-circle-notch fa-spin"></i> Procesando...`;

        const queryParams = new URLSearchParams({
            url: currentVideoUrl,
            format_id: formatId,
            type: type
        });
        if (type === 'audio') {
            queryParams.append('audio_quality', bitrate);
        }

        window.location.href = `/download/?${queryParams.toString()}`;

        // Show conversion success alert toast
        showSuccessToast();

        setTimeout(() => {
            button.classList.remove('downloading');
            button.innerHTML = originalHtml;
        }, 12000);
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorCard.classList.remove('hidden');
        errorCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
});
