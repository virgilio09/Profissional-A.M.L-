$(document).ready(function(){

// // ------------------- formulario add serviço ----------------
    
//     // mask
    $('.cep').mask('00000-000');

    var SPMaskBehavior = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
      },
      spOptions = {
        onKeyPress: function(val, e, field, options) {
            field.mask(SPMaskBehavior.apply({}, arguments), options);
          }
      };
      
      $('.sp_celphones').mask(SPMaskBehavior, spOptions);

    //  preenchimento automatico pelo cep
    function limpa_formulário_cep() {
        // Limpa valores do formulário de cep.
        $("#rua").val("");
        $("#bairro").val("");
        $("#cidade").val("");
        $("#uf").val("");
    }
    //Quando o campo cep perde o foco.
    $("#cep").blur(function() {

        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                $("#rua").val("...");
                $("#bairro").val("...");
                $("#cidade").val("...");
                $("#uf").val("...");
                $("#ibge").val("...");

                //Consulta o webservice viacep.com.br/
                $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
                    console.log(dados);
                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#rua").val(dados.logradouro);
                        $("#bairro").val(dados.bairro);
                        $("#cidade").val(dados.localidade);
                        $("#uf").val(dados.uf);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulário_cep();
                        bootbox.alert("CEP não encontrado.");
                
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                bootbox.alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    });

    $.validator.addMethod('fileMax', function(value, element, param) {
        var count = 0;
        count =element.files.length;
       
        return this.optional(element) || (count <= param)
    }, 'A quantidade máxima é de {0} imagens');
    
     
    $.validator.addMethod('filesize', function(value, element, param) {
        var count = 0;
        for (var i = 0; i < element.files.length; i++) {
        count += element.files[i].size;
        }
        return this.optional(element) || (count <= param)
    }, 'O tamanho máxima é de {0} byte');

    // validacao
    $("#form-servicos").validate({
        rules:{
            nome:{
                minlength: 3
            },
            descricao:{
                minlength: 10
            },
            image:{
                fileMax: 5,
                // filesize: 600000 //max size 600 kb,
            },
           
        },
        messages:{
            status:{
                required: "Por favor, defina o status",
            },
            nome:{
                required: "Por favor, informe seu nome",
                minlength: "O nome deve ter pelo menos 3 caracteres" 
            },
            categoria:{
                required: "Por favor, ecolha uma categoria",
            },
            email:{
                required: "Por favor, informe um email"
            
            },
            telefone01:{
                required: "Por favor, informe um telefone e/ou celular"
            
            },
            descricao:{
                required: "Por favor, informe uma descrição",
                minlength: "A descrição deve ter pelo menos 10 caracteres" 
            },
            
            cep:{
                required: "Por favor, informe seu cep"
            
            },
            rua:{
                required: "Por favor, informe a rua"
            
            },
            numero:{
                required: "Por favor, informe o número"
            
            },
            bairro:{
                required: "Por favor, informe o bairro"
            
            },
            estado:{
                required: "Por favor, informe o estado"
            
            },
            cidade:{
                required: "Por favor, informe a cidade"
            
            },
            
            
        }
    });
    
    $("#form-comment").validate({
        rules:{
            nome:{
                minlength: 3
            },
            comment:{
                minlength: 5
            },
        },
        messages:{
            nome:{
                required: "Por favor, informe seu nome",
                minlength: "O nome deve ter pelo menos 3 caracteres" 
            },
            comment:{
                required: "Por favor, informe seu comentário",
                minlength: "A descrição deve ter pelo menos 5 caracteres" 
            },
        }

    });

});