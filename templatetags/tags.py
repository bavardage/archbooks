from django import template

register = template.Library()
	
@register.simple_tag
def navigation(request):
	return "You are currently at %s" % request.path   

@register.simple_tag
def doformul(form, specialfields=None):
	toreturn = ''
	for field in form:
		toreturn += '<li>%s %s %s' % (field.errors,
					      field.label_tag(),
					      field)
		if field.html_name in specialfields:
			toreturn += '<a href="#" \
 onClick="window.open(\'../%s?popup=%s\');">+</a>' % (
				specialfields[field.html_name], 
				'id_' + field.html_name
				)
		toreturn += '<br/>%s</li>' % field.help_text
	return toreturn

