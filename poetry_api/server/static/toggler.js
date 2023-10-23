let togglers = [...document.querySelectorAll(".poemDescription button")]


const toggler = (e) => {
    let desc = document.querySelector(`#${e.target.parentElement.id} p`)
    desc.style.visibility === "hidden" ? desc.setAttribute("style", "visibility: visible;") : desc.setAttribute("style", "visibility: hidden;")
    
}

for (let i = 0; i < togglers.length; i++) {
    togglers[i].addEventListener('click', toggler)
    
}