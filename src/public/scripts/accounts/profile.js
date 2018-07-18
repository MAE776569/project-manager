let profilePictureInput = $("#picture-upload"),
    profilePictureLabel = $("#picture-upload-label-text"),
    saveBtn = document.querySelector("#save-btn"),
    profilePicture = document.querySelector("#profile-picture");

profilePictureInput.on('change', function(){
    if (this.files && this.files.length === 1 &&
        this.files[0].type.search("image") !== -1){
            profilePictureLabel.text(this.files[0].name);
            saveBtn.disabled = false;
        let fileReader = new FileReader();
        fileReader.onload = function (event) {
            profilePicture.src = event.target.result;
        };
        fileReader.readAsDataURL(this.files[0]);
    }
    else{
        saveBtn.disabled = true;
    }
});