function deleteNote(noteId) {
    console.log("Deleting note with ID:", noteId); // <--- log this
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href="/";
    });
}