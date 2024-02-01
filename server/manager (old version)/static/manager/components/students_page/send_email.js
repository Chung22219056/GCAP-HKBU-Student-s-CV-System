var conv = new showdown.Converter({
    metadata: true
});

var simplemde = new SimpleMDE({
    element: document.getElementById("email-content"),
    autoDownloadFontAwesome: false,
    placeholder: "Type here...",
    spellChecker: false
});

function showEmailModal(student_id){
    $("#email-receiver").val(student_id)
    let modal = new bootstrap.Modal($("#emailModal"));
    modal.show()
}

function sendEmailRequestToServer(){
    fetch("/manager/send_email_to_student",{
        method: "POST",
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            student_id: $("#email-receiver").val(),
            email_content: conv.makeHtml(simplemde.value())
        })
    }).then(response => response.json())
    .then((json) => {
        Swal.fire({
            title: json.status ? 'Send email Successfully' : 'Fail to send email',
            text: json.status ? 'Success': 'Error',
            icon: json.status ? 'success' : 'error',
            showCancelButton: true,
            showDenyButton: false,
            showCancelButton: false,
            confirmButtonText: 'OK'
        })
    })
}
