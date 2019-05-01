document.addEventListener('DOMContentLoaded', function() {
    const jsonOutputElementId = document.getElementById('codex-editor').getAttribute('output-id');
    const jsonOutputElement = document.getElementById(jsonOutputElementId);
    let initialContent = undefined;
    try {
        initialContent = JSON.parse(jsonOutputElement.value);
    } catch(e) {}
    const editor = new EditorJS({
        holder : 'codex-editor',
        onChange: () => {
            editor.save().then( result => {
                jsonOutputElement.value = encodeURI(JSON.stringify(result, null, 0));
            });
        },
        tools: { 
            header: Header,
            checklist: Checklist
        },
        data: initialContent || {}
     });
}, false);