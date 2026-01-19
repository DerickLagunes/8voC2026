
    window.addEventListener('scroll', () => {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            loadCards();
            loadCards();
            loadCards();
            loadCards();
            }
    });

    function loadCards(){
        var p = document.createElement("p");
        var img = document.createElement("img");
        img.setAttribute("src", "")
        p.innerHTML = "Este es un elemento creado dinamico";
        document.getElementById("contenidoD").appendChild(p);
    }
