function changeWidth() {
    var form = document.getElementById("widthchanger")
    var wrapper = document.getElementById("game-wrapper");
    wrapper.style.width = form.elements[0].value;
    return false;
}
