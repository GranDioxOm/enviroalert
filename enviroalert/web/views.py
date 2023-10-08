from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class FireView(TemplateView):
    template_name = 'fire_main.html'


class FireMap(TemplateView):
    template_name = 'fire_map.html'


class FireLearn(TemplateView):
    template_name = 'fire_learn.html'


class FireReport(TemplateView):
    template_name = 'fire_report.html'


class FireReport2(TemplateView):
    template_name = 'fire_report_2.html'


class FireReport3(TemplateView):
    template_name = 'fire_report_3.html'


class FireReport4(TemplateView):
    template_name = 'fire_report_4.html'


class FireReport5(TemplateView):
    template_name = 'fire_report_5.html'


class FireReport6(TemplateView):
    template_name = 'fire_report_6.html'
