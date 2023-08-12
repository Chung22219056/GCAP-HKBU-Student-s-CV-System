var educations = []
var workExperiences = []
var base64ImgProfileIcon = ''
var languages = []
var skills = []




function handleSaveEducationData() {
    let institution = $("#institution").val()
    let program = $("#program").val()
    let startDate = $("#startDate").val()
    let endDate = $("#endDate").val()

    educations.push({ "institution": institution, "program": program, "startDate": startDate, "endDate": endDate })

    //clear input fields
    $("#institution").val('')
    $("#program").val('')
    $("#startDate").val('')
    $("#endDate").val('')

    //close modal
    $("#edcutionModal").modal("hide")
    renderDataInEducationField()
}



function renderDataInEducationField() {
    $("#education-field").empty()

    if (educations.length === 0) {
        $("#education-field").append(`<h6 class="text-secondary"><center>There are no eduation in here.</center></h6>`)
    } else {
        educations.forEach((education, index) => {
            $("#education-field").append(
                `
                <div class="card bg-light mb-3">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-9">
                                <h5 class="card-title"><i class="fa-solid fa-building-columns"></i> ${education.institution}</h5>
                                <h6 class="text-secondary"><strong style="white-space: pre-wrap;line-break: auto;">${education.program}</strong></h6>
                                <h6 class="text-secondary">${education.startDate} to ${education.endDate}</h6>
                            </div>
                            <div class="col-3">
                                <button class="btn btn-danger float-end" onClick="handleDeleteEducationRecord(${index})"><i class="fa-solid fa-trash"></i></button>
                            </div>
                        
                        </div>
                    </div>
                </div>
                `
            )
        })
    }

}

function handleDeleteEducationRecord(index) {
    educations.splice(index, 1)
    renderDataInEducationField()
}

function handleSaveWorkExperienceData() {
    let companyName = $("#companyName").val()
    let description = $("#workExperienceDescription").val()
    let startDate = $("#workExpStartDate").val()
    let endDate = $("#workExpEndDate").val()

    workExperiences.push({ "companyName": companyName, "description": description, "startDate": startDate, "endDate": endDate })

    //clear input fields
    $("#companyName").val('')
    $("#workExperienceDescription").val('')
    $("#workExpStartDate").val('')
    $("#workExpEndDate").val('')

    //close modal
    $("#workExperienceModal").modal("hide")
    renderDataInWorkExperienceField()

}

function handleDeleteWorkExperience(index) {
    workExperiences.splice(index, 1)
    renderDataInWorkExperienceField()
}

function renderDataInWorkExperienceField() {
    $("#workExperience-field").empty()

    if (workExperiences.length === 0) {
        $("#workExperience-field").append(`<h6 class="text-secondary"><center>There are no work experience data in here.</center></h6>`)
    } else {
        workExperiences.forEach((workExperience, index) => {
            console.log(workExperience)
            $("#workExperience-field").append(`
            <div class="card bg-light mb-3">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-9">
                                <h5 class="card-title"><i class="fa-solid fa-building"></i> ${workExperience.companyName}</h5>
                                <h6 class="text-secondary"><strong>${workExperience.description}</strong></h6>
                                <h6 class="text-secondary">${workExperience.startDate} to ${workExperience.endDate}</h6>
                            </div>
                            <div class="col-3">
                                <button class="btn btn-danger float-end" onClick="handleDeleteWorkExperience(${index})"><i class="fa-solid fa-trash"></i></button>
                            </div>
                        
                        </div>
                    </div>
                </div>
            
            `)
        })
    }
}

function fetchRequsetCreateCV() {
    console.log("fetchRequsetCreateCV")
    $('input[name^=lanuage]').map(function (idx, elem) {
        languages.push($(elem).val())
        return $(elem).val();
    }).get();


    $('input[name^=skill]').map(function (idx, elem) {
        skills.push($(elem).val())
        return $(elem).val();
    }).get();

    // console.log(languages)

    if (base64ImgProfileIcon == '') {
        base64ImgProfileIcon = $('#icon-preview').attr('src');
    }
    // console.log(base64ImgProfileIcon)

    fetch("/student/edit_Cv", {
        method: "POST",
        body: JSON.stringify({
            base64ImgProfileIcon: base64ImgProfileIcon,
            cvName: $("#cv-name").val(),
            firstName: $("#first-name").val(),
            lastName: $("#last-name").val(),
            nickName: $("#nick-name").val(),
            email: $("#email").val(),
            phone: $("#phone").val(),
            bio: $("#bio").val(),
            educations: educations,
            workExperiences: workExperiences,
            languages: languages,
            skills: skills
        })
    }).then(response => response.json()).then((json) => {
        Swal.fire({
            title: 'CV Status',
            text: json.status ? 'Create CV Successfully' : 'Fail to create CV',
            icon: json.status ? 'success' : 'error',
            showCancelButton: true,
            showDenyButton: false,
            showCancelButton: false,
            confirmButtonText: 'OK'
        })

        //if server save CV successfully than redirect the page to "cvRecord" after 2 seconds
        if (json.status) {
            setTimeout(function () {
                window.location.href = "/student/cvRecord";
            }, 2000);
        }
    })

}
