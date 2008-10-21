function addOptionToSelect(selectBox, value, text, selectedByDefault, selected)
{
   selectBox[selectBox.length] = new Option(text, value, selectedByDefault, selected);   
}
function addOptionToSelectOfId(id, value, text, selectedByDefault, selected)
{
   addOptionToSelect(document.getElementById(id), value, text, selectedByDefault, selected);
}
function setValueOfId(id, value)
{
    input = document.getElementById(id);
    input.value = value;
}
function getTextOfSelectedOption(id)
{
    var text = document.getElementById(id);
    if(text.selectedIndex != -1)
	{
	    return text.options[text.selectedIndex].text;
	}
}