function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        if (cookie.trim().startsWith('csrftoken=')) {
            return cookie.split('=')[1];
        }
    }
    return '';
}


function eliminarComercial(id) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: '¡No podrás recuperar este comercial!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
    }).then(result => {
        if (result.isConfirmed) {
            fetch(`/comerciales/eliminar/${id}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRFToken(),
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    Swal.fire('¡Eliminado!', data.message, 'success').then(() => {
                        location.reload();
                    });
                } else {
                    Swal.fire('Error', data.error || 'No se pudo eliminar el Comercial.', 'error');
                }
            });
        }
    });
}

function editarComercial(id) {
    fetch(`/comerciales/editar/${id}/`)
        .then(response => response.text())
        .then(data => {
            Swal.fire({
                title: 'Actualizar Comercial',
                html: data,
                showCancelButton: true,
                confirmButtonText: 'Actualizar',
                cancelButtonText: 'Cancelar',
                focusConfirm: false,
                preConfirm: () => {
                    const form = document.querySelector("form");
                    const formData = new FormData(form);

                    return fetch(form.action, {
                        method: 'POST',
                        body: formData,
                        headers: {
                            'X-CSRFToken': getCSRFToken(),
                            'X-Requested-With': 'XMLHttpRequest',
                        },
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.message) return data.message;
                        throw new Error('Error al guardar cambios');
                    })
                    .catch(error => {
                        Swal.showValidationMessage(`Error: ${error.message}`);
                    });
                },
            }).then(result => {
                if (result.isConfirmed) {
                    Swal.fire('¡Éxito!', 'Comercial actualizado correctamente', 'success').then(() => {
                        location.reload();
                    });
                }
            });
        });
}