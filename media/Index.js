function cercar() {
    criteri = $("#cerca").val()
    console.log(criteri)
    // criteri = criteri::first-letter.toUpperCase();
    // console.log(criteri)
    if (criteri!="") {
        console.log(criteri)
        criteri.toLowerCase()
        $.get("/cerca?criteri="+criteri,function (data) {
           console.log(data);
           $("#resultats").children().remove()
           $.each(data, function (index, element) {
               console.log(index);
               console.log(element);
               a = $("<a href=\"/personatge/"+element.id+"\">")
               resultat = $("<div id=\"sortida\">")
               img = $("<img src=\""+element.imatge+"\">")
               p = $("<p>"+element.nom+"</p>")
               resultat.append(img)
               resultat.append(p)
               a.append(resultat)
               $("#resultats").append(a)
           })
       })
    }
}