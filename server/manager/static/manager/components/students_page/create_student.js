function createUserFetch(){
    fetch("/manager/create_student_api",{
        method: "POST",
        body: JSON.stringify({
            email: $("#email_create_user").val(),
            student_id: $("#student_id_create_user").val(),
            username: $("#username_create_user").val(),
            password: $("#password_create_user").val()
        })
    })
    .then(response => response.json())
    .then((json) => {
        Swal.fire({
            icon: json.status ? 'success' : 'error',
            title: json.status ? 'Created Student' : 'Fail to create student',
            showDenyButton: false,
            showCancelButton: false,
            confirmButtonText: 'OK',
        })
    }).then(()=>{
        setTimeout(function() {
            location.reload();
        }, 2000);
    })
}