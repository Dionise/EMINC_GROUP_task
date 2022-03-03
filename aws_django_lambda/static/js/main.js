$('#serach').on('click', function(e){      
    e.preventDefault();
        $.ajax({  
      type: 'POST',
            url:'',
            data: { 
                  csrfmiddlewaretoken: '{{ csrf_token }}',
                  key: $('.key').val(),
                 },

            success: function(){
                $('#message').html('<h2>Aded to cart</h2>!</h2>')
                    }
    });
    }); 