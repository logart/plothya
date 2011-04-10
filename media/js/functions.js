function ui.remove_photo(photo_id){
    $("div").$(".photo").$("#"+photo_id).remove();
}

function remove_photo(photo_id){
    ui.remove_photo(photo_id);
}
