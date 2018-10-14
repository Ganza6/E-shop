$(document).ready(function(){
    var form = $('#form');
    form.on('submit',function(e){
    e.preventDefault();
    var nmb = $('#number').val();
    var submit_btn = $('#submit_btn');
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data("product_name");
    var product_price = submit_btn.data("product_price");
    $('.basket-items ul').append("<li>"+product_name+' '+product_price+'₽'+' x '+nmb+' шт '+'<a href="" class="delete-item">X</a>'+"</li>");
    $( "li.empty" ).remove();
    });

    $('#kor').hover(function(){
      $(".basket-items").slideToggle();
    });

    $(document).on('click','delete-item',function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    });


    });