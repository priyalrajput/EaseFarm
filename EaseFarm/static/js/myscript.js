$('.plus-cart').click(function()
{
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success: function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText =
            data.amount
        }
    })
});

