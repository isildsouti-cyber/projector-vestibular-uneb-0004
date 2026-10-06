/* Remove (nao apenas oculta) o widget VLibras em telas mobile (Android/iOS). */
(function(){
  function isMobile(){
    try{ return window.matchMedia('(max-width:768px)').matches || /Android|iPhone|iPad|iPod|Mobile/i.test(navigator.userAgent||''); }
    catch(e){ return false; }
  }
  function nuke(){
    if(!isMobile()) return;
    var w=document.getElementById('vlibras-access-wrapper'); if(w) w.remove();
    var list=document.querySelectorAll('div[vw]'); for(var i=0;i<list.length;i++){ list[i].remove(); }
    var sts=document.querySelectorAll('style.sf-hidden'); for(var j=0;j<sts.length;j++){ var t=sts[j].textContent||''; if(/vlibras|div\[vw\]/i.test(t)) sts[j].remove(); }
  }
  function start(){
    nuke();
    setTimeout(nuke,300); setTimeout(nuke,1200); setTimeout(nuke,3000);
    try{
      if(isMobile() && window.MutationObserver){
        var mo=new MutationObserver(function(){ nuke(); });
        mo.observe(document.documentElement,{childList:true,subtree:true});
        setTimeout(function(){ mo.disconnect(); }, 8000);
      }
    }catch(e){}
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
