import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .store import *
def health(r): return JsonResponse({'status':'ok','database':'not used'})
def routes(r): return JsonResponse(ROUTES,safe=False)
def pass_types(r): return JsonResponse(PASS_TYPES,safe=False)
def applications(r):
 a=[dict(x) for x in APPLICATIONS];q=r.GET.get('q','').lower();s=r.GET.get('status','')
 if q:a=[x for x in a if q in json.dumps(x).lower()]
 if s:a=[x for x in a if x['status']==s]
 return JsonResponse(a,safe=False)
def detail(r,i):
 x=get(i);return JsonResponse(x or {'error':'Application not found'},status=200 if x else 404)
@csrf_exempt
def create_application(r): return JsonResponse(create(json.loads(r.body or '{}')),status=201)
@csrf_exempt
def update_application(r,i):
 x=update(i,json.loads(r.body or '{}'));return JsonResponse(x or {'error':'Not found'},status=200 if x else 404)
@csrf_exempt
def feedback_view(r,i):
 x=feedback(i,json.loads(r.body or '{}'));return JsonResponse(x or {'error':'Not found'},status=200 if x else 404)
def dashboard(r):
 total=len(APPLICATIONS);approved=sum(x['status']=='Approved' for x in APPLICATIONS)
 return JsonResponse({'total_applications':total,'approved':approved,'under_review':sum(x['status']=='Under Review' for x in APPLICATIONS),'rejected':sum(x['status']=='Rejected' for x in APPLICATIONS),'expiring_soon':sum(x['status']=='Expiring Soon' for x in APPLICATIONS),'resolution_rate':round(approved*100/total,1),'revenue':sum(x['amount'] for x in APPLICATIONS),'monthly':[{'month':m,'applications':n,'approved':a} for m,n,a in [('Apr',28,22),('May',35,29),('Jun',42,36),('Jul',48,41),('Aug',55,47),('Sep',61,52)]],'route_usage':[{'route':r['code'],'passes':p} for r,p in zip(ROUTES,[31,27,22,18,15])]})
def notifications(r): return JsonResponse(NOTIFICATIONS,safe=False)
