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

        if($('#raty')) {
            var hints =  ['Malo', 'Pobre', 'Regular', 'Bueno', 'Excelente']
            $('#raty').raty({score: 3,hints: hints, half: true,path: '/static/project/lib/images'});
             var avarage_score = 0;
             var comments = 0;
             $("div[name='past_score']").each(function(){

                var params = {};
                params.score = $(this).text();
                params.path = '/static/project/lib/images';
                params.readOnly = true;
                $(this).text('');
                $(this).raty(params);
                avarage_score += parseFloat(params.score);
                ++comments;
             });



             var params = {};
             params.score = avarage_score/comments;
             params.path = '/static/project/lib/images';
             params.readOnly = true;
             $("#avarage_score").raty(params);

        };

        $('#comment_submit').on('click', function (){
            $("input[name='score']").val()
        });

    });



})();