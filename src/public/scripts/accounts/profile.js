let profilePictureInput = $("#picture-upload"),
    profilePictureLabel = $("#picture-upload-label-text"),
    saveBtn = document.querySelector("#save-btn");

profilePictureInput.on('change', function(){
    if (this.files && this.files.length === 1 &&
        this.files[0].type.search("image") !== -1){
            profilePictureLabel.text(this.files[0].name);
            saveBtn.disabled = false;
    }
    else{
        saveBtn.disabled = true;
    }
});