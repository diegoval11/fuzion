function toggleMenu() {
    document.body.classList.toggle('menu-open');
    document.querySelector('.more-functions-container').classList.toggle('menu-opened');

    $(document).ready(function(){
        $('.nav-link').on('click', function(e){
            e.preventDefault();
            var url = $(this).data('url');
            $.get(url, function(data){
                $('#content').html($(data).find('#content').html());
            });
        });
    });


}

function formatDate(input) {
    // Eliminar todos los caracteres que no sean números
    var value = input.value.replace(/\D/g, '');

    // Dividir la cadena en partes
    var day = value.substring(0, 2);
    var month = value.substring(2, 4);
    var year = value.substring(4, 8);

    // Crear la nueva cadena formateada
    if (value.length > 4) {
        input.value = `${day}/${month}/${year}`;
    } else if (value.length > 2) {
        input.value = `${day}/${month}`;
    } else {
        input.value = day;
    }
}