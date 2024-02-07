document.addEventListener("DOMContentLoaded", () => {
    $("DIV#add_item").click(() => {
        $("UL.my_list").append("<li>Item</li>");
    });
    // not implmented
    $("DIV#remove_item").click(() => {
        $("li").remove();
    });
    $("DIV#clear_list").click(() => {
        $("li").remove();
    });
});
