function download_icons() {
    var ip_box = document.getElementById("vita_ip");
    ip = ip_box.value;
    var port_box = document.getElementById("port")
    port = port_box.value;
    var path_box = document.getElementById("folder")
    path = path_box.value;
    eel.run_app(ip, port, path);
}

function select() {
    eel.select_folder();
}

eel.expose(show_path);
function show_path(folder_path) {
    var textbox = document.getElementById("folder");
    textbox.value = folder_path;
}

eel.expose(show_confirmation);
function show_confirmation(statement){
    M.toast({html: statement, classes: 'rounded'})
}