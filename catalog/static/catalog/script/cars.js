const img = [...document.querySelectorAll('.carImg')]
img.forEach(i => {
  if(i.src.includes('null')){
    i.style.display = 'none'
  }
  else {
    i.style.display = 'block'
  }
})


