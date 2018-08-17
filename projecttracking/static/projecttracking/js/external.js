function do_resize(textbox) {
    var maxrows=100;
    var txt=textbox.value;
    var cols=textbox.cols;

    var arraytxt=txt.split('\n');
    var rows=arraytxt.length;

    for (i=0;i<arraytxt.length;i++)
        rows+=parseInt(arraytxt[i].length/cols);
    if (rows>maxrows) textbox.rows=maxrows;
    else textbox.rows=rows;
}
