$(document).ready(function (e) {

    $(".contenedor-categoria a").click(function (e) {
        e.preventDefault();
        let id = $(this).attr('data-id');

        if ($(this).index() == 0) {
            $(".contenedor-producto").show();
        }else {
            $(".contenedor-producto").hide();
            $(".contenedor-producto").each(function (i,v) {
                if ($(v).attr('data-categoria') == id) {
                    $(v).show();
                }
            });
        }
        //let nombre = $(this).text();
        //$(this).text(nombre + ' *');
        //console.log("ingreso al evento", id, nombre);
    });


    $(".contenedor-producto a").click(function (e) {
        e.preventDefault();
        console.log($(this))
    });


});