let navBar = $("#navbar");
let navbarToggler = $("#navbar-toggler");
let userMenuToggler = $("#user-drop-down-toggler");
let userMenu = $("#user-dropdown-menu");
let adminMenuToggler = $("#admin-drop-down-toggler")
let adminMenu = $("#admin-dropdown-menu");

navbarToggler.click(function (){
    if (navbarToggler.attr("aria-expanded") == "false")
        navbarToggler.attr("aria-expanded", "true")
    else
        navbarToggler.attr("aria-expanded", "false")
    navBar.toggleClass("hide");
});
userMenuToggler.click(function(){
    if (adminMenu.css("display") !== "none") {
        userMenuToggler.attr("aria-expanded", "false")
        adminMenu.slideToggle("fast");
    }
    if (userMenuToggler.attr("aria-expanded") == "false")
        userMenuToggler.attr("aria-expanded", "true")
    else
        userMenuToggler.attr("aria-expanded", "false")
    userMenu.slideToggle("fast");
});
adminMenuToggler.click(function(){
    if (userMenu.css("display") !== "none"){
        userMenuToggler.attr("aria-expanded", "false")
        userMenu.slideToggle("fast");
    }
    if (adminMenuToggler.attr("aria-expanded") == "false")
        adminMenuToggler.attr("aria-expanded", "true")
    else
        adminMenuToggler.attr("aria-expanded", "false")
    adminMenu.slideToggle("fast");
});
