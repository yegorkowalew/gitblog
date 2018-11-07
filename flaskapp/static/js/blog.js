function showMenu() {
    $.getJSON( "/api/v1.0/themes", function( data ) {
        $('#navbarCollapse ul li').remove();
        $(".js").remove();
        var items = [];
        var data_slide = 0;
        $.each( data.themes, function( key, val ) {
            $('#navbarCollapse ul').append(
                $('<li>').attr('class', 'nav-item').append(
                    $('<a>').attr({class: "nav-link",href: "/blog/theme/" + val.title_slug,}).append(val.title_ru)
                          ));
            $('#myCarousel ol').append(
                $('<li>').attr({
                    'data-target':"#myCarousel",
                    'data-slide-to':data_slide,
                    'class':'js',
                }).append())
            data_slide++
            $(".carousel-inner").append(`<div class="carousel-item js"><img class="first-slide" src="${val.img}" alt="First slide"><div class="container"><div class="carousel-caption text-left"><h1>${val.title_ru} <span class="badge badge-light">${val.summ}</span></h1><p>${val.description}</p><p><a class="btn btn-lg btn-primary" href="/blog/theme/${val.title_slug}" role="button">Перейти</a></p></div></div></div>`)});
       }).done(function( json ) {
       }).fail(function( jqxhr, textStatus, error ) {
        var err = textStatus + ', ' + error;
        console.log( "Request Failed: " + err);
       });
  }
function showArticles(theme) {
    $.getJSON( "/api/v1.0/articles_count/"+theme, function(data) {
        var i;
        for (i = 0; i < data.articles_count; i++) {
            console.log(i);
            $.getJSON( "/api/v1.0/article/"+theme+'/'+i, function(data) {
                console.log(data);
                $('#articles').append(`
                <div class="row featurette">
                <div class="col-md-9 order-md-2">
                  <h2 class="featurette-heading"><a href="/blog/${data.article.theme_slug}/${data.article.title_slug}">${data.article.title_ru}</a></h2>
                  <p class="lead">${data.article.description}</p>
                  <div class="row justify-content-end text-muted">${data.article.last_update}</div>
                </div>
                <div class="col-md-3 order-md-1">
                  <img class="featurette-image img-fluid mx-auto" src="http://placehold.it/200x200" alt="Generic placeholder image">
                </div>
              </div>
              <hr class="featurette-divider">`);
            });
        }
    }).fail(function() {
        console.log("error");
        });
}
$( document ).ready(function() {
    showMenu();
    showArticles('all');
    // showArticles('domashnee');
    $('nav-item').on('click', function() {
        alert('yo')
   });
});