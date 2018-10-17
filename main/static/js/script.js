$(document).ready(function(){
    var form = $('#form');
    form.on('submit',function(e){
    e.preventDefault();
    var nmb = Number($('#number').val());
    if (!Number.isInteger(nmb) || nmb==0){
                return
    }
    var submit_btn = $('#submit_btn');
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data("product_name");
    var product_price = submit_btn.data("product_price");
    var number="";
    if ($(".id").attr('class') == "id"+" "+product_id){
        var all_text = ($("."+product_id).text());
        for(i = 0; i < all_text.length; i++){
            if (all_text[i]=='x'){
                for(q = i+2;all_text[q]!=' ';q++){
                    number += all_text[q];
                }
                break;
            }
        }
        number = Number(number)+nmb;
        $( "."+ product_id).remove();
        $('.basket-items ul').append("<li class='id'>"+product_name+' '+product_price+'₽'+' x '+number+' шт '+
            '<a href="" class="delete-item">X</a>'+"</li>");
        $('.id').addClass(''+product_id) ;
    }
    else{
    $('.basket-items ul').append("<li class='id'>"+product_name+' '+product_price+'₽'+' x '+nmb+' шт '+
        '<a href="" class="delete-item">X</a>'+"</li>");
    $('.id').addClass(''+product_id) ;
    $( "li.empty" ).remove();}

    $("#number").val('');
    // $.cookie(".id "+product_id, $("."+product_id).text());
    // var q = $.cookie('.id 2');
    // $.cookie("qeqwe", 3);
    // console.log(q); начинаю куки
    });



    $('#kor').hover(function(){
      $(".basket-items").slideToggle();
    });

    $(document).on('click','delete-item',function (e) {
        e.preventDefault();
        $(this).closest('li').remove();

    });


    });