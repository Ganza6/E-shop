$(document).ready(function(){
    var form = $('#form');
    form.on('submit',function(e){
    e.preventDefault();
    var nmb = $('#number').val();
    var submit_btn = $('#submit_btn');
    console.log(submit_btn);
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data("product_name");
    var product_price = submit_btn.data("product_price");
    console.log(product_id);
    console.log(product_name);
    console.log(nmb);
    console.log(product_price);
    console.log
    })
//$("#hidden").css("display", "none;"); // Для скрытия
//$("#hidden").css("display", "block;"); // Для показа
$('#kor').hover(function(){
  $(".basket-items").slideToggle();
});

    });