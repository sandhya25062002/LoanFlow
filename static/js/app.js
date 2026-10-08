(function(){
  var $=function(s,c){return(c||document).querySelector(s)},$$=function(s,c){return[].slice.call((c||document).querySelectorAll(s))};
  // mobile sidebar
  var sb=$('#sidebar'),mb=$('#menuBtn');
  if(mb&&sb){mb.addEventListener('click',function(){var o=sb.classList.toggle('open');mb.setAttribute('aria-expanded',o)})}
  // password visibility
  $$('[data-toggle-password]').forEach(function(b){b.addEventListener('click',function(){
    var i=$(b.dataset.togglePassword),show=i.type==='password';i.type=show?'text':'password';b.textContent=show?'Hide':'Show';b.setAttribute('aria-pressed',show)})});
  // modals
  function closeAll(){$$('.modal.open').forEach(function(m){m.classList.remove('open')})}
  $$('[data-modal-open]').forEach(function(b){b.addEventListener('click',function(){var m=$(b.dataset.modalOpen);m.classList.add('open');var f=$('button,input',m);f&&f.focus()})});
  $$('[data-modal-close]').forEach(function(b){b.addEventListener('click',closeAll)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')closeAll()});
  // loading state on submit
  $$('form[data-loading]').forEach(function(f){f.addEventListener('submit',function(){var b=$('[type=submit]',f);if(b){b.classList.add('is-loading');b.disabled=true}})});
  // client-side table search/filter (progressive enhancement; server filtering still applies)
  var q=$('[data-table-search]');
  if(q){var rows=$$('#dataTable tbody tr');q.addEventListener('input',function(){var v=q.value.toLowerCase();rows.forEach(function(r){r.hidden=r.textContent.toLowerCase().indexOf(v)<0})})}
  // status bar widths from data attributes
  $$('[data-w]').forEach(function(e){e.style.width=e.dataset.w+'%'});
})();
