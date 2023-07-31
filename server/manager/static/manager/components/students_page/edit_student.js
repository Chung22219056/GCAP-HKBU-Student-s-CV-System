function editStudent(student_id){
    let filteredStudent = students.filter((student) => {
        return student.student_id == student_id
    })
    
    $("#old_student_id_edit_student").val(student_id)

    $("#email_edit_student").val(filteredStudent[0].email)
    $("#username_edit_student").val(filteredStudent[0].student_name)
    $("#student_id_edit_student").val(filteredStudent[0].student_id)

    let modal = new bootstrap.Modal($("#editUserModal"));
    modal.show()
}


function editStudentFetch(){
    fetch("/manager/edit_student_api",{
        method: "post",
        body: JSON.stringify({
            old_student_id: $("#old_student_id_edit_student").val(),
            email: $("#email_edit_student").val(),
            username: $("#username_edit_student").val(),
            student_id: $("#student_id_edit_student").val()
        })
    }).then(response => response.json())
    .then((json) => {
        Swal.fire({
            icon: json.status ? 'success' : 'error',
            title: json.status ? 'Edited Student' : 'Fail to edit student',
            showDenyButton: false,
            showCancelButton: false,
            confirmButtonText: 'OK',
        })
    })
    .then(()=>{
        setTimeout(function() {
            location.reload();
        }, 2000);
    })
}