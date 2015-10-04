'use strict';
(function(){
    $( document ).ready(function() {
         $("label[for=id_o]").text('Ordenar por: ');

         $('#id_o').change(function() {
            console.log('Cambiando');
            $('#submit_order').trigger('click');
        });
    });


})();