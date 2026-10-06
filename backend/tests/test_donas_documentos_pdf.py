"""Tests for PDF documento display fix in donas admin panel."""
import os
import base64
import pytest
import requests

def _read_env(key):
    for p in ('/app/frontend/.env',):
        try:
            with open(p) as f:
                for line in f:
                    if line.strip().startswith(f'{key}='):
                        return line.strip().split('=', 1)[1]
        except Exception:
            pass
    return None

BASE_URL = (os.environ.get('REACT_APP_BACKEND_URL') or _read_env('REACT_APP_BACKEND_URL') or '').rstrip('/')
assert BASE_URL, 'REACT_APP_BACKEND_URL not configured'

ADMIN_USER = 'donas'
ADMIN_PASS = 'Seinao10@@'
REAL_CPF = '21878979744'
TEST_CPF = '00000000191'

PNG_B64 = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='
# Minimal PDF
MINI_PDF_BYTES = b'%PDF-1.1\n1 0 obj<<>>endobj\ntrailer<<>>\n%%EOF'
PDF_B64 = base64.b64encode(MINI_PDF_BYTES).decode()


@pytest.fixture(scope='module')
def admin_token():
    r = requests.post(f'{BASE_URL}/api/admin/auth/login',
                      json={'username': ADMIN_USER, 'password': ADMIN_PASS}, timeout=15)
    assert r.status_code == 200, f'Login failed: {r.status_code} {r.text}'
    token = r.json().get('token')
    assert token
    return token


@pytest.fixture(scope='module')
def headers(admin_token):
    return {'Authorization': f'Bearer {admin_token}'}


# --- Bug fix: real candidate with PDF documents ---

def test_listar_documentos_donas_pdf(headers):
    r = requests.get(f'{BASE_URL}/api/admin/documentos', params={'q': REAL_CPF}, headers=headers, timeout=15)
    assert r.status_code == 200, r.text
    items = r.json().get('items', [])
    assert len(items) >= 1, 'DONAS DA SILVA not returned'
    doc = next((d for d in items if d['cpf'] == REAL_CPF), None)
    assert doc is not None
    assert doc['frente_mime'] == 'application/pdf', f"frente_mime={doc['frente_mime']}"
    assert doc['verso_mime'] == 'application/pdf', f"verso_mime={doc['verso_mime']}"


def test_get_documento_frente_pdf(admin_token):
    r = requests.get(f'{BASE_URL}/api/admin/documentos/{REAL_CPF}/frente',
                     params={'token': admin_token}, timeout=15)
    assert r.status_code == 200
    assert r.headers.get('content-type', '').startswith('application/pdf'), r.headers.get('content-type')
    assert r.content[:4] == b'%PDF'


def test_get_documento_verso_pdf(admin_token):
    r = requests.get(f'{BASE_URL}/api/admin/documentos/{REAL_CPF}/verso',
                     params={'token': admin_token}, timeout=15)
    assert r.status_code == 200
    assert r.headers.get('content-type', '').startswith('application/pdf')
    assert r.content[:4] == b'%PDF'


# --- Regression: image thumbnails still work ---

def test_image_regression_and_pdf_sniff(headers, admin_token):
    """Create test cadastro with PNG data-URL frente and raw-b64 PDF verso, verify mimes."""
    payload = {
        'cpf': TEST_CPF,
        'doc_tipo': 'RG',
        'doc_frente': f'data:image/png;base64,{PNG_B64}',
        'doc_verso': PDF_B64,  # raw base64 without prefix
    }
    r = requests.post(f'{BASE_URL}/api/track/documents', json=payload, timeout=15)
    assert r.status_code in (200, 201), f'track/documents: {r.status_code} {r.text}'

    # Verify listing
    r = requests.get(f'{BASE_URL}/api/admin/documentos', params={'q': TEST_CPF}, headers=headers, timeout=15)
    assert r.status_code == 200
    items = r.json().get('items', [])
    doc = next((d for d in items if d['cpf'] == TEST_CPF), None)
    assert doc is not None, 'test doc not found'
    assert doc['frente_mime'].startswith('image/'), f"frente_mime={doc['frente_mime']}"
    assert doc['verso_mime'] == 'application/pdf', f"verso_mime={doc['verso_mime']}"

    # Verify serving content-types
    r_f = requests.get(f'{BASE_URL}/api/admin/documentos/{TEST_CPF}/frente',
                      params={'token': admin_token}, timeout=15)
    assert r_f.status_code == 200
    assert r_f.headers.get('content-type', '').startswith('image/')

    r_v = requests.get(f'{BASE_URL}/api/admin/documentos/{TEST_CPF}/verso',
                       params={'token': admin_token}, timeout=15)
    assert r_v.status_code == 200
    assert r_v.headers.get('content-type', '').startswith('application/pdf')

    # Cleanup - try common admin endpoints
    cleanup_tried = False
    for url in [f'{BASE_URL}/api/admin/cadastros/{TEST_CPF}',
                f'{BASE_URL}/api/admin/candidatos/{TEST_CPF}']:
        try:
            rd = requests.delete(url, headers=headers, timeout=10)
            cleanup_tried = True
            if rd.status_code in (200, 204):
                break
        except Exception:
            pass
    # Not asserting cleanup - reported in logs
    print(f'Cleanup attempted: {cleanup_tried}')
