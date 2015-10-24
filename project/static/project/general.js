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
        try {
            if($('#raty')) {
                var hints =  ['Malo', 'Pobre', 'Regular', 'Bueno', 'Excelente']
                $('#raty').raty({score: 3,hints: hints, path: '/static/project/lib/images'});
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
        } catch (err){}


        $('#comment_submit').on('click', function (){
            $("input[name='punctuation']").val($('#raty').raty('score'))
        });


        $('#showImageA').on('click', function (){
            if ($("#imgForm").is(":visible")) {
                $("#imgForm").hide();
            } else {
                $("#imgForm").show();
            }

        });

        var hiddeProfileAll = function() {};

         try {
             hiddeProfileAll = function () {
                $("#posts").hide();
                $("#productos").hide();
                $("#siguiendo").hide();
                $("#seguidores").hide();
            }
         } catch (err) {}


        $('#postsLI').on('click', function (){
            hiddeProfileAll();
            $("#posts").show();
        });
        $('#productosLI').on('click', function (){
            hiddeProfileAll();
            $("#productos").show();
        });

        $('#siguiendoLI').on('click', function (){
            hiddeProfileAll();
            $("#siguiendo").show();
        });

        $('#seguidoresLI').on('click', function (){
            hiddeProfileAll();
            $("#seguidores").show();
        });

    });



})();