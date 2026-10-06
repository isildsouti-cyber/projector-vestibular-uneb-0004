
## Update (05/10/2026) - Fluxo de inscrição (inscricao.html)
- Adicionado campo Escolaridade (card entre contato e documento)
- Rodapé: removidos "Início" e "© UNEB" (mantido selo Site Seguro)
- Botão Continuar só habilita com todos os campos obrigatórios válidos
- Máscaras CPF/Data/Celular/CEP + busca automática de endereço via /api/cep
- Validação CPF (algoritmo), data, e-mail, celular (11 dígitos), senha == confirmar senha
- Mostrar/ocultar senha funcional
- Removida a declaração "prestar informações falsas" (não bloqueia mais o botão)
- Continuar -> loader 2s -> nova página de aceite LGPD: /termos-lgpd.html -> /confirmacao.html
