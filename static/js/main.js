window.onload = function(){

  /*===== MENU SHOW Y HIDDEN =====*/
  let navMenu = document.getElementById('nav-menu'),
  toggleMenu = document.getElementById('nav-toggle'),
  closeMenu = document.getElementById('nav-close')
  
  /*SHOW*/
  toggleMenu.addEventListener('click', ()=>{
    navMenu.classList.toggle('show')
  })
  
  /*HIDDEN*/
  closeMenu.addEventListener('click', ()=>{
    navMenu.classList.remove('show')
  })
  
}