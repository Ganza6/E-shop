$(document).ready(function(){
    var basket = {};
    $.each($.cookie(), function (index, value) {
        var id ='';
        var item ='';
        if (index[0]=='.'&& value!='null'){
            for(i = 4;i<index.length;i++){
                id+=index[i];
            }
            for(i=0;value[i]!='X';i++){
                item+=value[i];
            }
            basket[id]=item;
        }
    });
    $.each(basket,function (index,value) {
        $( "li.empty" ).remove();
        $('.basket-items ul').append("<li class='id'>"+value+'<a href="" class="delete-item">X</a>'+"</li>");
        $('.id').last().addClass(''+index) ;
    });


    var form = $('#form');
    form.on('submit',function(e){
    e.preventDefault();
    var nmb = Number($('#number').val());
    if (!Number.isInteger(nmb) || nmb==0){
                return
    }
    $( "li.empty" ).remove();
    var submit_btn = $('#submit_btn');
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data("product_name");
    var product_price = submit_btn.data("product_price");
    var number="";
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
        $('.id').last().addClass(''+product_id) ;



    $("#number").val('');
    $.cookie(".id "+product_id, $("."+product_id).text());
    });

    $('#kor').hover(function(){
      $(".basket-items").slideToggle();
    });

    $(document).on('click','.delete-item',function (e) {
        e.preventDefault();
        var id = "."+$(this).parent().attr("class");
        $.cookie(id,null,-1);
        var number_id='';
        for (i = 4;i<id.length;i++){
            number_id += id[i];
        }
        $( "li."+number_id ).remove()//доделать что если список пуст вывести "заглушку"
    });


    });