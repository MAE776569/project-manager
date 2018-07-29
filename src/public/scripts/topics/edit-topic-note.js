tinymce.init({
    selector: '#note',
    height: 300,
    theme: 'modern',
    plugins: `preview paste 
        searchreplace autolink directionality code 
        visualblocks visualchars fullscreen image 
        link media template codesample table charmap 
        hr pagebreak nonbreaking anchor toc insertdatetime 
        advlist lists textcolor wordcount 
        imagetools contextmenu colorpicker textpattern help`,
    removed_menuitems: 'newdocument',
    toolbar: `undo redo | styleselect | bold italic | link image 
        alignleft aligncenter alignright`,
    
    style_formats_merge: true,
    style_formats: [
        {
            title: 'Tags', items: [
                {title: 'span', inline:'span'},
                {title: 'section', block: 'section'}
            ]
        },
    ],
    //valid_children: "+section[*]"
});