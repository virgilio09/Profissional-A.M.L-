$(document).ready(function(){
     // -------------------- #backtotop ----------------------------
     jQuery("#backtotop").click(function () {
        jQuery("body,html").animate({
            scrollTop: 0
        }, 600);
    });
    jQuery(window).scroll(function () {
        if (jQuery(window).scrollTop() > 150) {
            jQuery("#backtotop").addClass("visible");
        } else {
            jQuery("#backtotop").removeClass("visible");
        }
    });

    // ---------------------- dashboard ----------------------------
    var baseUrl   = 'http://127.0.0.1:8000/dashboard/'; 
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $('.rm-servico').on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        
        bootbox.confirm({
            message: "Você realmente deseja remover esse serviço?",
            buttons: {
                confirm: {
                    label: 'Sim',
                    className: 'btn'
                },
                cancel: {
                    label: 'Cancelar',
                    className: 'btn'
                }
            },
            callback: function (result) {
                if(result) {
                    window.location.href = delLink;
                }
            }
        });

    });


    $('#rm-user').on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        
        bootbox.confirm({
            message: "<p>Você realmente deseja apagar sua conta?</p>"+
                     "<p>Seus dados seram apagados de forma permanente</p>",
            buttons: {
                confirm: {
                    label: 'Sim',
                    className: 'btn'
                },
                cancel: {
                    label: 'Cancelar',
                    className: 'btn'
                }
            },
            callback: function (result) {
                if(result) {
                    window.location.href = delLink;
                }
            }
        });

    });

    $('#filter').change(function() {
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });
    
    $('.help-status').on('click',function(){
        bootbox.alert({
            title: 'O que significa um serviço Ativo ou Desativado',
            message: "<p><i class='fa fa-check'></i> <strong>Ativo</strong> - Seu serviço será divulgado no site.</p>"+
                     "<p><i class='fas fa-times'></i> <strong>Desativado</strong> - Seu serviço fica inativo, podendo ser ativado posteriomente.</p"+
                     "<br></br>"+
                     "<p>Para mais informações, clique <a href='/help/'>aqui</a></p>",
    
            buttons: {
                ok: {
                    className: 'btn'
                }
            }
        });
    });
    // preenchimento ciadde e estado home
    var estados_cidades = 'https://gist.githubusercontent.com/letanure/3012978/raw/36fc21d9e2fc45c078e0e0e07cce3c81965db8f9/estados-cidades.json'

    $.getJSON(estados_cidades, function(json_cidades){
  
        $('#estado').change(function(){
            var e = ($(this).val());
            document.querySelector("#cidade").innerHTML = '';
            var cidade_select = document.querySelector("#cidade");
        
            var num_estados = json_cidades.estados.length;
            var j_index = -1;
        
            // aqui eu pego o index do Estado dentro do JSON
            for(var x=0;x<num_estados;x++){
                if(json_cidades.estados[x].sigla == e){
                j_index = x;
                }
            }
        
            if(j_index != -1){
            
                // aqui eu percorro todas as cidades e crio os OPTIONS
                json_cidades.estados[j_index].cidades.forEach(function(cidade){
                var cid_opts = document.createElement('option');
                cid_opts.setAttribute('value',cidade)
                cid_opts.innerHTML = cidade;
                cidade_select.appendChild(cid_opts);
                });
            }else{
                document.querySelector("#cidade").innerHTML = '';
            }
            
        });
    });
    $('#name').change(function(){
        $(this).css('font-weight', '600');
    });

    $('#estado').change(function(){
        $(this).css('font-weight', '600');
    });

    $('#cidade').change(function(){
        $(this).css('font-weight', '600');
    });

    $('#category').change(function(){
        $(this).css('font-weight', '600');
    });

    // ---------- about -------------------
    $('.counter').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        }, {
        duration: 4000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
        });
    });



});