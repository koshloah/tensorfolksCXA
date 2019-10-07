var html = "\
<nav class='navbar navbar-inverse navbar-fixed-top'>\
    <div class='container-fluid'>\
        <div class='navbar-header'>\
        <button type='button' class='navbar-toggle collapsed' data-toggle='collapse' data-target='#navbar' aria-expanded='false' aria-controls='navbar'>\
            <span class='sr-only'>Toggle navigation</span>\
            <span class='icon-bar'></span>\
            <span class='icon-bar'></span>\
            <span class='icon-bar'></span>\
        </button>\
            <a class='navbar-brand' href='http://localhost:8060'>\
                <div>\
                    <img src='assets/home.svg' style='height:20px;width:18px;position:relative;top:-6;left:-2;'>\
                     Munch Manager\
                </div>\
            </a>\
        </div>\
        \
        \
        <div id='navbar' class='navbar-collapse collapse'>\
        <ul class='nav navbar-nav navbar-right'>\
            <li><a href='#'>Dashboard</a></li>\
            <li><a href='#'>Settings</a></li>\
            <li><a href='#'>Profile</a></li>\
            <li><a href='#'>Help</a></li>\
        </ul>\
        <form class='navbar-form navbar-right'>\
            <input type='text' class='form-control' placeholder='Search...'>\
        </form>\
        </div>\
    </div>\
</nav>"

document.write(html)
