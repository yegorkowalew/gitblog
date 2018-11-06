function showMenu() {
    $.getJSON( "/api/v1.0/themes", function( data ) {
        $('#navbarCollapse ul li').remove();
        $('#navbarCollapse ul').append(
            $('<li>').attr('class', 'nav-item').append(
                $('<a>').attr({class: "nav-link active", href: "https://pcmaster.top",}).append("Pcmaster.top")
                      ));
        var items = [];
        $.each( data.themes, function( key, val ) {
            $('#navbarCollapse ul').append(
                $('<li>').attr('class', 'nav-item').append(
                    $('<a>').attr({class: "nav-link",href: "/blog/theme/" + val.title_slug,}).append(val.title_ru)
                          ));
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