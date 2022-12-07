$("#0").fadeIn("slow")
let counter = 0;
let flag = true;

$("input[type=radio]").click(function() {
    if(flag){
        let el = $(this);
        parent = el.parent().parent().parent();
        for (let input of parent[0].getElementsByTagName("input")){
            input.checked = false;
        }
        el[0].checked = true;
    }
});

/*
$(".next-btn").click(function() {
    let el = $(this);
    parent = el.parent().parent();
    let card_id = parent[0].id;
    let card_id_nxt = (parseInt(card_id, 10) + 1).toString();
    let card = $("#".concat(card_id))[0];
    parent.css('z-index', -100);
    $("#".concat(card_id)).animate({
        opacity: 0,
        right: "60%",
        },
        300)
    $("#".concat(card_id)).fadeOut(10);
    $("#".concat(card_id_nxt)).delay( 320 ).fadeIn("fast");
    counter++;
    console.log(counter);
    if(counter>=card_count) {
        $("#end-test").delay( 400 ).fadeIn("slow");
    }
});
*/

$(".next-btn").click(function() {
    let el = $(this);
    parent = el.parent().parent();
    let card_id = parent[0].id;
    let card_id_nxt = (parseInt(card_id, 10) + 1).toString();
    let card = $("#".concat(card_id))[0];
    if($('input[name="menos['.concat(card_id).concat(']"]')).is(':checked')
        &&
        $('input[name="mas['.concat(card_id).concat(']"]')).is(':checked')
    ){
        flag = false;
        $("#".concat(card_id)).animate({
            opacity: 0,
            right: "60%",
            },
            300)
        $("#".concat(card_id)).fadeOut(1);
        $("#".concat(card_id_nxt)).delay( 310 ).fadeIn("fast");
        counter++;
        if(counter>=card_count) {
            $("#end-test").delay( 400 ).fadeIn("slow");
        }
        flag = true;
    }else{
        $("#".concat(card_id)).effect( "shake" );
    }
});



