from django.http import HttpResponse

import i18n
i18n.set('locale', 'ar')
i18n.load_path.append('local')

def index(request):
    return HttpResponse(i18n.t('foo.hi'))