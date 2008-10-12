function addOptionToSelect(selectBox, value, text, selectedByDefault, selected)
{
   selectBox[selectBox.length] = new Option(text, value, selectedByDefault, selected);   
}
function addOptionToSelectOfId(id, value, text, selectedByDefault, selected)
{
   addOptionToSelect(document.getElementById(id), value, text, selectedByDefault, selected);
}