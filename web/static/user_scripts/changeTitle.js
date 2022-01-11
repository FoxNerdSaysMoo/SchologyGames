function changeTitle() {
    var form = document.getElementById("titlechanger")
    document.title = form.elements[0].value;
    form.elements[0].value = "";
    return false;
}
