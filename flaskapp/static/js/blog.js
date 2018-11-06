function showMenu() {
    $.getJSON( "/api/v1.0/themes", function( data ) {
        $('#navbarCollapse ul li').remove();
        // $('#navbarCollapse ul').append(
        //     $('<li>').attr('class', 'nav-item').append(
        //         $('<a>').attr({class: "nav-link active", href: "https://pcmaster.top",}).append("Pcmaster.top")
        //               ));
        var items = [];
        var data_slide = 0;
        $.each( data.themes, function( key, val ) {
            $('#navbarCollapse ul').append(
                $('<li>').attr('class', 'nav-item').append(
                    $('<a>').attr({class: "nav-link",href: "/blog/theme/" + val.title_slug,}).append(val.title_ru)
                          ));
            // carousel-indicators
            $('#myCarousel ol').append(
                $('<li>').attr({
                    'data-target':"#myCarousel",
                    'data-slide-to':data_slide,
                }).append()
            
            )
            // alert(data_slide);
            // var txt = "<div class="carousel-item"><img class="first-slide" src="static/img/i2.jpg" alt="First slide"><div class="container"><div class="carousel-caption text-left"><h1>Программирование <span class="badge badge-light">2</span></h1><p>Программирование на Python, JavaScript</p><p><a class="btn btn-lg btn-primary" href="#" role="button">Перейти</a></p></div></div></div>";
            // var txt = document.write("<h1>Привет мир!</h1>");
            data_slide++
            $(".carousel-inner").append(`<div class="carousel-item"><img class="first-slide" src="/static/img/i2.jpg" alt="First slide"><div class="container"><div class="carousel-caption text-left"><h1>${val.title_ru} <span class="badge badge-light">${val.summ}</span></h1><p>${val.description}</p><p><a class="btn btn-lg btn-primary" href="${val.title_slug}" role="button">Перейти</a></p></div></div></div>`)
            // .html('<div class="carousel-item"><img class="first-slide" src="/static/img/i2.jpg" alt="First slide"><div class="container"><div class="carousel-caption text-left"><h1>Программирование <span class="badge badge-light">2</span></h1><p>Программирование на Python, JavaScript</p><p><a class="btn btn-lg btn-primary" href="#" role="button">Перейти</a></p></div></div></div>');
        });
       }).done(function( json ) {
        console.log( "Request Accepted");
       }).fail(function( jqxhr, textStatus, error ) {
        var err = textStatus + ', ' + error;
        console.log( "Request Failed: " + err);
       });
  }

$( document ).ready(function() {
    showMenu();
});