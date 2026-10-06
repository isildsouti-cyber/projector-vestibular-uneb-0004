/* FGV chrome (header + footer) injected on inscription-flow pages to match /termos */
(function(){
  var LOGO = "data:image/png;base64,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";
  var css = ""
   + "#fgv-chrome-top,#fgv-chrome-footer{font-family:'Segoe UI',Roboto,Arial,sans-serif}"
   + "#fgv-chrome-top .fgv-sites-bar{background:#001a2c;height:26px;display:flex;align-items:center;justify-content:center;font-size:12px;color:#d0d7de;letter-spacing:.3px}"
   + "#fgv-chrome-top .fgv-sites-bar span{background:#2b3844;padding:3px 14px;border-radius:2px}"
   + "#fgv-chrome-top .fgv-logo-bar{background:#002D4D;padding:20px;text-align:center}"
   + "#fgv-chrome-top .fgv-logo-bar img{height:30px;width:auto;display:inline-block}"
   + "#fgv-chrome-footer{background:#002D4D;color:#fff;padding:40px 24px 22px}"
   + "#fgv-chrome-footer .wrap{max-width:1200px;margin:0 auto}"
   + "#fgv-chrome-footer .brand{text-align:center;padding-bottom:18px;border-bottom:1px solid rgba(255,255,255,.12)}"
   + "#fgv-chrome-footer .brand img{height:26px}"
   + "#fgv-chrome-footer .top-links{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 32px;padding:16px 0;border-bottom:1px solid rgba(255,255,255,.12);text-transform:uppercase;font-size:12px;font-weight:600;letter-spacing:.6px}"
   + "#fgv-chrome-footer .top-links a{color:#fff;text-decoration:none;opacity:.85}"
   + "#fgv-chrome-footer .top-links a:hover{opacity:1;color:#01BFBF}"
   + "#fgv-chrome-footer .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:24px;padding-top:24px}"
   + "#fgv-chrome-footer h4{font-size:14px;font-weight:700;margin-bottom:8px;color:#01BFBF}"
   + "#fgv-chrome-footer p,#fgv-chrome-footer a.link{font-size:13px;line-height:1.55;color:#e4e9ef;text-decoration:none;display:block;margin:0}"
   + "#fgv-chrome-footer .social{display:flex;gap:10px;margin-top:6px}"
   + "#fgv-chrome-footer .social a{width:30px;height:30px;display:inline-flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,.35);border-radius:50%;color:#fff;font-size:12px;text-decoration:none}"
   /* hide native Cebraspe/AOCP chrome */
   + "#aocp-header-host,#aocp-footer,#barra-fgv,header.fixed-top,header[role=banner],nav.navbar,footer[role=contentinfo]{display:none!important}"
   + "body.__cebraspe-applied .layout-container,body.__cebraspe-applied{padding-top:0!important;margin-top:0!important}"
   + "@media(max-width:768px){#fgv-chrome-top .fgv-logo-bar{padding:16px}#fgv-chrome-top .fgv-logo-bar img{height:auto!important;width:auto!important;max-width:78%!important}}";
  var st=document.createElement('style'); st.id='__fgv_chrome_css'; st.textContent=css; document.head.appendChild(st);

  var header = ''
   + '<div class="fgv-sites-bar"><span>Sites FGV</span></div>'
   + '<div class="fgv-logo-bar"><a href="/inicio.html"><img alt="FGV Conhecimento" src="'+LOGO+'"></a></div>';
  var footer = ''
   + '<div class="wrap">'
   + '<div class="brand"><a href="/inicio.html"><img alt="FGV Conhecimento" src="'+LOGO+'"></a></div>'
   + '<div class="top-links"><a href="javascript:void(0)" onclick="return false">C\u00f3digo de \u00c9tica</a><a href="javascript:void(0)" onclick="return false">Termos de Uso</a><a href="javascript:void(0)" onclick="return false">Aviso de Privacidade</a><a href="javascript:void(0)" onclick="return false">\u00c1rea Restrita</a></div>'
   + '<div class="cols">'
   + '<div><h4>Rio de Janeiro</h4><p>Rua Jornalista Orlando Dantas, 36.<br>CEP: 22231-010</p></div>'
   + '<div><h4>S\u00e3o Paulo</h4><p>Av. Paulista, 542, 7\u00ba andar.<br>CEP: 01311-000</p></div>'
   + '<div><h4>Contrate-nos</h4><p>sac@cebraspe.org.br</p><p>61 3448-0100</p></div>'
   + '<div><h4>Atendimento aos candidatos</h4><p>61 3448-0100</p><p>sac@cebraspe.org.br</p></div>'
   + '<div><h4>Siga nas redes</h4><div class="social"><a href="javascript:void(0)" onclick="return false" title="Facebook">f</a><a href="javascript:void(0)" onclick="return false" title="Instagram">ig</a><a href="javascript:void(0)" onclick="return false" title="LinkedIn">in</a><a href="javascript:void(0)" onclick="return false" title="YouTube">yt</a></div></div>'
   + '</div></div>';

  function mount(){
    if(!document.getElementById('fgv-chrome-top')){
      var h=document.createElement('div'); h.id='fgv-chrome-top'; h.innerHTML=header;
      document.body.insertBefore(h, document.body.firstChild);
    }
    if(!document.getElementById('fgv-chrome-footer')){
      var f=document.createElement('div'); f.id='fgv-chrome-footer'; f.innerHTML=footer;
      document.body.appendChild(f);
    }
  }
  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
