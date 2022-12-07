let flag = false;
$('input').prop("disabled", true);
console.log("por aquí");
$(".question").css('visibility', 'hidden');
$(".question").css('display', 'none');
$("#finish").fadeOut();
$(function() {
    console.log("Doc ready");
    $('input').prop("disabled", true);
    let flag = false;
    $(".question").css('visibility', 'visible');
    $("#pre-load").fadeOut(50);
    $("#1").css('visibility', 'visible');
    $("#1").delay(50).fadeIn();
    $("#test").delay(50).fadeIn();

    $('input[name="question[1]"]').prop("disabled", false);
    flag = true;
    $("input").click(function () {
        console.log(this);
        if(flag){
            flag = false;
            console.log($(this));
            let parent_question = $(this).parent().parent().parent();
            let id_question = parseInt(parent_question[0].id);
            $('input[name="question[' + id_question + ']"]').prop("disabled", true);
            console.log("#" + id_question);
            $("#" + id_question).fadeOut(300);
            if(id_question === question_total){
                $("#finish").delay(300).fadeIn(300, function () {
                    $('input[type="submit"]').prop("disabled", false);
                    $('input').prop("disabled", false);
                    flag = true;
                    });
            }else{
                console.log(id_question + 1);
                $("#" + (id_question + 1)).delay(300).fadeIn(300, function () {
                    $('input[name="question[' + (id_question + 1) + ']"]').prop("disabled", false);
                    flag = true;
                    });
            }
        }
    });

    console.log(question_total);

    $(".card-body").bind("webkitAnimationEnd mozAnimationEnd animationend", function(){
      $(this).removeClass("card-wobble")
    })

    $(".card-body").mouseenter(function(){
        if($(this).hasClass("card-wobble")){
            console.log("ya la tiene")
        }else {
            $(this).addClass("card-wobble");
        }

    })


});