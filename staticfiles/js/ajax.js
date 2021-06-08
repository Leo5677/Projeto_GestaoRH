function utilizouHoraExtra(id) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/registros/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (result) {
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });

}

function naoUtilizouHoraExtra(id) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/registros/nao-utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (result) {
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas_nao_utilizadas);
        }
    });

}



