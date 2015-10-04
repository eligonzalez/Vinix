'use strict';
(function(){
    $( document ).ready(function() {
         $("label[for=id_o]").text('Ordenar por: ');

         $('#id_o').change(function() {
            console.log('Cambiando');
            $('#submit_order').trigger('click');
        });


        $('#showPassword').click(function() {
            if (!$(this).is(':checked')) {
                $('#changePassword').slideUp().hide( "slow" );
            } else {
                $('#changePassword').slideDown().show( "slow" );
            }
        });
    });



})();