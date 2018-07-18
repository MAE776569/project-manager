let navBar = $("#navbar"),
    navbarToggler = $("#navbar-toggler"),
    userMenuToggler = $("#user-drop-down-toggler"),
    userMenu = $("#user-dropdown-menu"),
    adminMenuToggler = $("#admin-drop-down-toggler"),
    adminMenu = $("#admin-dropdown-menu"),
    notificationsMenuToggler = $("#notifications-dropdown-toggler"),
    notificationMenu = $("#notifications-dropdown");

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
    if (notificationMenu.css("display") !== "none") {
        notificationsMenuToggler.attr("aria-expanded", "false")
        notificationMenu.slideToggle("fast");
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
    if (notificationMenu.css("display") !== "none") {
        notificationsMenuToggler.attr("aria-expanded", "false")
        notificationMenu.slideToggle("fast");
    }
    if (adminMenuToggler.attr("aria-expanded") == "false")
        adminMenuToggler.attr("aria-expanded", "true")
    else
        adminMenuToggler.attr("aria-expanded", "false")
    adminMenu.slideToggle("fast");
});
notificationsMenuToggler.click(function(){
    if (userMenu.css("display") !== "none") {
        userMenuToggler.attr("aria-expanded", "false")
        userMenu.slideToggle("fast");
    }
    if (adminMenu.css("display") !== "none") {
        userMenuToggler.attr("aria-expanded", "false")
        adminMenu.slideToggle("fast");
    }
    if (notificationsMenuToggler.attr("aria-expanded") == "false")
        notificationsMenuToggler.attr("aria-expanded", "true")
    else
        notificationsMenuToggler.attr("aria-expanded", "false")
    notificationMenu.slideToggle("fast");
});
