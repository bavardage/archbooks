from django import template
from django.core.urlresolvers import reverse

register = template.Library()
	
@register.simple_tag
def navigation(request):
	return "You are currently at %s" % request.path   

@register.simple_tag
def doformul(form, linkedfields=None, specialfields=None):
	toreturn = ''
	print "linked", linkedfields
	print "special", specialfields
	linkedfields = ([] if not linkedfields else linkedfields)
	specialfields = ([] if not specialfields else specialfields)
	for field in form:
		toreturn += '<li>%s %s %s' % (field.errors,
					      field.label_tag(),
					      field)
		if field.html_name in linkedfields:
			toreturn += '<a href="#" \
 onClick="window.open(\'../%s?popup=%s\');">+</a>' % (
				linkedfields[field.html_name], 
				'id_' + field.html_name
				)
		
		if field.html_name in specialfields:
			toreturn += '<a href="#" \
onClick="window.open(\'' + reverse(specialfields[field.html_name][0], 
				  args=specialfields[field.html_name][1]
				   ) + specialfields[field.html_name][2] + '\');">...</a>'
		toreturn += '<br/>%s</li>' % field.help_text
	return toreturn

