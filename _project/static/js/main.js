$(document).ready(function () {
    $(".ui.dropdown").dropdown();

    $(".message .close").on("click", function () {
        console.log("click it");
        $(this).closest(".message").transition("fade");
    });
});
