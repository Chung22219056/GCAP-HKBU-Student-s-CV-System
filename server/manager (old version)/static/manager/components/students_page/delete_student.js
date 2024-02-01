function confirmationOfDeleteStudent(){
    return Swal.fire({
        title: 'Are You Sure Delete The Student ?',
        showDenyButton: true,
        showCancelButton: false,
        confirmButtonText: 'Yes',
        denyButtonText: 'No',
        customClass: {
            actions: 'my-actions',
            cancelButton: 'order-1 right-gap',
            confirmButton: 'order-2',
            denyButton: 'order-3',
        }
    })
}

function deleteStudent(student_id){
    confirmationOfDeleteStudent().then((result)=>{
        if(!result.isConfirmed){
            return
        }

        fetch("/manager/delete_student_api",{
            method: "POST",
            body: JSON.stringify({
                "student_id": student_id
            })
        }).then(response => response.json())
        .then((json) => {
            Swal.fire({
                icon: json.status ? 'success' : 'error',
                title: json.status ? 'Removed Student' : 'Fail to remove student',
                showDenyButton: false,
                showCancelButton: false,
                confirmButtonText: 'OK',
            })
        })
        .then(() => {
            setTimeout(function() {
                location.reload();
            }, 2000);
        })
    })

}
