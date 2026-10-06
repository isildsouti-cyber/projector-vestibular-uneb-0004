#!/usr/bin/env python3
"""Seed ~80 test inscriptions reproducing the exact frontend fetch payloads
across 3 behavior buckets and mobile/desktop devices, then verify admin panel."""
import json, random, time, urllib.request, urllib.error, os, re

API = None
with open('/app/frontend/.env') as f:
    for line in f:
        if line.startswith('REACT_APP_BACKEND_URL='):
            API = line.strip().split('=', 1)[1]
API = API.rstrip('/')
print('API =', API)

UA_DESKTOP = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
UA_MOBILE = "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36"
UA_IPHONE = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"

NOMES = ["Ana Clara Souza","Bruno Almeida Lima","Carla Ferreira Santos","Diego Oliveira Costa",
"Eduarda Ramos Silva","Felipe Nunes Rocha","Gabriela Martins Dias","Henrique Barros Melo",
"Isabela Cardoso Pinto","João Pedro Teixeira","Karina Lopes Araujo","Lucas Gomes Freitas",
"Mariana Azevedo Reis","Nicolas Correia Moraes","Olivia Fernandes Cruz","Paulo Ricardo Campos",
"Queila Monteiro Sa","Rafael Carvalho Nogueira","Sabrina Duarte Pires","Thiago Ribeiro Macedo",
"Ursula Vieira Prado","Vitor Hugo Andrade","Wesley Tavares Brito","Yasmin Castro Leal",
"Zeca Moreira Fonseca","Amanda Borges Vargas","Caio Pereira Guimaraes","Debora Cunha Peixoto",
"Elias Santana Farias","Fernanda Rios Batista"]
SOBRENOMES = ["Silva","Santos","Oliveira","Souza","Lima","Costa","Pereira","Rodrigues","Almeida","Nascimento","Carvalho","Araujo"]

CURSOS = [
    ("Ciências Contábeis (Bacharelado) - Matutino - CAMPUS I - SALVADOR - UNEB","CC-MAT"),
    ("Direito (Bacharelado) - Noturno - CAMPUS I - SALVADOR - UNEB","DIR-NOT"),
    ("Enfermagem (Bacharelado) - Integral - CAMPUS I - SALVADOR - UNEB","ENF-INT"),
    ("Pedagogia (Licenciatura) - Noturno - CAMPUS XIII - ITABERABA - UNEB","PED-NOT"),
    ("Engenharia de Produção Civil - Matutino - CAMPUS I - SALVADOR - UNEB","EPC-MAT"),
    ("Administração (Bacharelado) - Noturno - CAMPUS III - JUAZEIRO - UNEB","ADM-NOT"),
    ("Medicina (Bacharelado) - Integral - CAMPUS I - SALVADOR - UNEB","MED-INT"),
    ("Letras (Licenciatura) - Vespertino - CAMPUS IV - JACOBINA - UNEB","LET-VES"),
]
LOCAIS = ["SALVADOR","TEIXEIRA DE FREITAS","FEIRA DE SANTANA","VITORIA DA CONQUISTA","JUAZEIRO","ILHEUS","BARREIRAS","JACOBINA"]
CONCURSO = "Vestibular - 2027 - UNEB - Universidade do Estado da Bahia"

def gen_cpf():
    n = [random.randint(0,9) for _ in range(9)]
    for _ in range(2):
        s = sum((len(n)+1-i)*v for i,v in enumerate(n))
        d = (s*10) % 11
        n.append(0 if d==10 else d)
    return ''.join(map(str,n))

def fmt_cpf(c):
    return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"

def post(path, payload, ua):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(API+path, data=data, method='POST',
        headers={'Content-Type':'application/json','User-Agent':ua})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode()[:120]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:160]
    except Exception as e:
        return 0, str(e)[:160]

def do_registration(nome, cpf, email, curso, cod, local, ua):
    extra = {
        "nome": nome, "cpf": fmt_cpf(cpf), "email": email,
        "concurso": CONCURSO, "edital": "Vestibular 2027",
        "stage": "inscricao_finalizada", "finalized": True,
        "cargo_titulo": curso, "cargo_codigo": cod, "cargo_titulo2": "",
        "localidade": local, "valor": 95, "taxa": "R$ 95,00",
        "form_data": {"NOME": nome, "CPF": fmt_cpf(cpf), "EMAIL": email,
                      "CELULAR": "(71) 9"+str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999)),
                      "CURSO": curso, "LOCAL_PROVA": local}
    }
    return post('/api/track/registration', {"page":"/confirmacao.html","user_agent":ua,"extra":extra}, ua)

def do_pix(path, nome, cpf, curso, cod, ua):
    extra = {"nome": nome, "cpf": fmt_cpf(cpf), "valor": 95, "cargo_titulo": curso,
             "cargo_codigo": cod, "concurso": CONCURSO, "stage": path.split('-')[-1]}
    return post('/api/'+path, {"page":"/pagamento-pix.html","user_agent":ua,"extra":extra}, ua)

# ---- Build 80 jobs ----
random.seed(42)
TOTAL = 80
jobs = []
for i in range(TOTAL):
    base = NOMES[i % len(NOMES)]
    nome = base if i < len(NOMES) else f"{base.split()[0]} {random.choice(SOBRENOMES)} {random.choice(SOBRENOMES)}"
    cpf = gen_cpf()
    first = base.split()[0].lower()
    email = f"{first}{i}@teste.com"
    curso, cod = random.choice(CURSOS)
    local = random.choice(LOCAIS)
    # device: ~half mobile
    ua = random.choice([UA_DESKTOP, UA_DESKTOP, UA_MOBILE, UA_IPHONE])
    device = 'mobile' if ('Mobile' in ua or 'iPhone' in ua) else 'desktop'
    # bucket: A=reg+gen+copy, B=reg+gen, C=reg only
    b = i % 3  # 0->A,1->B,2->C roughly even
    bucket = 'A' if b==0 else ('B' if b==1 else 'C')
    jobs.append(dict(nome=nome,cpf=cpf,email=email,curso=curso,cod=cod,local=local,ua=ua,device=device,bucket=bucket))

counts = {'A':0,'B':0,'C':0}
dev = {'mobile':0,'desktop':0}
ok_reg=ok_gen=ok_cop=0
errs=[]
for j in jobs:
    counts[j['bucket']]+=1; dev[j['device']]+=1
    s,_ = do_registration(j['nome'],j['cpf'],j['email'],j['curso'],j['cod'],j['local'],j['ua'])
    if s==200: ok_reg+=1
    else: errs.append(('reg',s,_))
    if j['bucket'] in ('A','B'):
        s,_ = do_pix('track/pix-generated', j['nome'],j['cpf'],j['curso'],j['cod'],j['ua'])
        if s==200: ok_gen+=1
        else: errs.append(('gen',s,_))
    if j['bucket']=='A':
        s,_ = do_pix('track/pix-copied', j['nome'],j['cpf'],j['curso'],j['cod'],j['ua'])
        if s==200: ok_cop+=1
        else: errs.append(('cop',s,_))

print("=== SEED DONE ===")
print("buckets:", counts, " (A=reg+gen+copy, B=reg+gen, C=reg only)")
print("devices:", dev)
print(f"ok_registration={ok_reg}/{TOTAL}  ok_pix_generated={ok_gen}/{counts['A']+counts['B']}  ok_pix_copied={ok_cop}/{counts['A']}")
if errs:
    print("ERRORS (first 5):", errs[:5])
