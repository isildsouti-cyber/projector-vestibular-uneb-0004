/* UNEB chrome (header + footer) injected on inscription-flow secondary pages */
(function(){
  var LOGO = "/uneb-logo.png";
  var css = ""
   + "#fgv-chrome-top,#fgv-chrome-footer{font-family:'Segoe UI',Roboto,Arial,sans-serif}"
   + "#fgv-chrome-top .fgv-sites-bar{background:#0f4cad;height:5px}"
   + "#fgv-chrome-top .fgv-logo-bar{background:#ffffff;border-bottom:1px solid #e6ebf2;padding:16px 20px;display:flex;align-items:center;justify-content:center}"
   + "#fgv-chrome-top .fgv-logo-bar img{height:64px;width:auto;display:inline-block}"
   + "#fgv-chrome-footer{background:#0d3a86;color:#fff;padding:36px 24px 22px;margin-top:40px}"
   + "#fgv-chrome-footer .wrap{max-width:1120px;margin:0 auto}"
   + "#fgv-chrome-footer .brand{text-align:center;padding-bottom:18px;border-bottom:1px solid rgba(255,255,255,.14);font-size:16px;font-weight:800;letter-spacing:.3px}"
   + "#fgv-chrome-footer .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px;padding-top:24px}"
   + "#fgv-chrome-footer h4{font-size:14px;font-weight:700;margin-bottom:8px;color:#8fc0ff}"
   + "#fgv-chrome-footer p,#fgv-chrome-footer a.link{font-size:13px;line-height:1.55;color:#e4e9ef;text-decoration:none;display:block;margin:0}"
   + "#fgv-chrome-footer .copy{text-align:center;font-size:12px;color:#c7d6f2;padding-top:22px;margin-top:22px;border-top:1px solid rgba(255,255,255,.14)}"
   /* hide any leftover native chrome */
   + "#aocp-header-host,#aocp-footer,#barra-fgv,header.fixed-top,header[role=banner],nav.navbar,footer[role=contentinfo]{display:none!important}"
   + "body.__cebraspe-applied .layout-container,body.__cebraspe-applied{padding-top:0!important;margin-top:0!important}"
   + "@media(max-width:768px){html,body{overflow-x:hidden;max-width:100vw}#fgv-chrome-top .fgv-logo-bar{padding:12px}#fgv-chrome-top .fgv-logo-bar img{height:52px!important;max-width:80%!important}#fgv-chrome-footer{padding:28px 18px 20px}}";
  var st=document.createElement('style'); st.id='__fgv_chrome_css'; st.textContent=css; document.head.appendChild(st);

  var header = ''
   + '<div class="fgv-sites-bar"></div>'
   + '<div class="fgv-logo-bar"><a href="/inicio.html"><img alt="UNEB - Universidade do Estado da Bahia" src="'+LOGO+'"></a></div>';
  var footer = ''
   + '<div class="wrap">'
   + '<div class="brand">Universidade do Estado da Bahia \u2014 Vestibular 2027</div>'
   + '<div class="cols">'
   + '<div><h4>Endere\u00e7o</h4><p>Rua Silveira Martins, 2555, Cabula<br>Salvador - BA, CEP: 41150-000</p></div>'
   + '<div><h4>Atendimento ao candidato</h4><p>(71) 3117-2200</p><p>vestibular@uneb.br</p></div>'
   + '<div><h4>Processo Seletivo</h4><p>Vestibular 2027</p><p>Inscri\u00e7\u00f5es de 15/09 a 08/10/2026</p></div>'
   + '</div>'
   + '<div class="copy">\u00a9 UNEB \u2014 Universidade do Estado da Bahia. Todos os direitos reservados.</div>'
   + '</div>';

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
