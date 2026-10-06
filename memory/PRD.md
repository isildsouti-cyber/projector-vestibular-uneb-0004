
## Update (05/10/2026) - Fluxo de inscrição (inscricao.html)
- Adicionado campo Escolaridade (card entre contato e documento)
- Rodapé: removidos "Início" e "© UNEB" (mantido selo Site Seguro)
- Botão Continuar só habilita com todos os campos obrigatórios válidos
- Máscaras CPF/Data/Celular/CEP + busca automática de endereço via /api/cep
- Validação CPF (algoritmo), data, e-mail, celular (11 dígitos), senha == confirmar senha
- Mostrar/ocultar senha funcional
- Removida a declaração "prestar informações falsas" (não bloqueia mais o botão)
- Continuar -> loader 2s -> nova página de aceite LGPD: /termos-lgpd.html -> /confirmacao.html

## Update (06/10/2026) - Página de sucesso (inscricao-sucesso.html)
- Removidos TODOS os links externos para uneb.selecao.net.br (mantido apenas o texto/aparência de botão): Área do Candidato, Imprimir Comprovante, Nome Social, Arquivos heteroidentificação, Início (rodapé) e logo UNEB do cabeçalho
- Botão "EFETUAR PAGAMENTO" aponta para /pagamento-pix.html (interno)
- Validado via screenshot: 0 links externos, layout intacto

## Update (06/10/2026) - Página de pagamento PIX (pagamento-pix.html) — REMODELADA
- Reescrita completa com identidade visual UNEB (logo /uneb-logo.png, azul #0f4cad), removido todo o legado FGV/Cebraspe/SEDUC-PA/AOCP e o /fgv-chrome.js
- Valor corrigido para R$ 95,00 (antes R$ 180 hardcoded). Fontes corrigidas: confirmacao.html (valor:95/taxa 'R$ 95,00'), dados-inscricao.html (fallback || 95)
- Botão "EFETUAR PAGAMENTO" em inscricao-sucesso.html: removido target=_blank → segue o fluxo na MESMA aba
- Página lê dados reais de sessionStorage (inscricao_dados: NOME/CPF/CURSO/CURSO2/CURSO_ID; inscricao_numero) e exibe: Candidato, CPF, Nº inscrição, Vaga escolhida, Valor R$ 95,00
- Gera PIX via POST /api/pix/generate (valor 95 + cpf + txid) → QR PNG base64 + código copia-e-cola; botão "Copiar código PIX" com feedback
- Botão "Voltar ao resumo da inscrição" → /inscricao-sucesso.html (mesma aba)
- Tracking: /api/track/pix-generated (ao gerar) e /api/track/pix-copied (ao copiar); estados loading/erro/retry; responsivo
- Logo UNEB salvo como arquivo: /app/frontend/public/uneb-logo.png (extraído do base64 da página de sucesso)
- Validado via screenshot + curl: valor 540595.00 no BR Code, QR ok, copiar ok, voltar mesma aba

