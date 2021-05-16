import requests
from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import BeneficiaryDetails
from .forms import BeneficiaryDetailsModelForm


def companyList_view(request):
    url = 'https://tinyurl.com/allcompanylist'
    r = requests.get(url)
    json_data = r.json()
    context = {
        'title': "Company List",
        'json_data': json_data,
    }
    return render(request, 'results/company_list.html', context)


def resultCheck_view(request):
    ipo_result = {}
    if request.POST:
        print(request.POST)
        URL = 'https://tinyurl.com/companyresultcheck'
        data = {
            "companyShareId": request.POST['companyShareId'],
            "boid": request.POST['boid']
        }
        ipo_result = requests.post(url=URL, json=data).json()
        print(ipo_result)
    url = 'https://tinyurl.com/allcompanylist'
    r = requests.get(url)
    companies = r.json()['body']
    context = {
        'title': 'Check Result',
        'companies': companies,
        'ipo_result': ipo_result,
    }
    return render(request, 'results/checkresult.html', context)


def results_view(request, companyShareId=None):
    if companyShareId:
        total_count = 0
        alloted_count = 0
        notalloted_count = 0
        ipo_results = {}
        boid_name = {}
        boids = []
        beneficiary_details = BeneficiaryDetails.objects.filter(user_id=request.user.id)
        for i in beneficiary_details:
            boids.append(i.boid)
            boid_name[i.boid] = i.name
        URL = 'https://tinyurl.com/companyresultcheck'
        for boid in boids:
            data = {
                "companyShareId": companyShareId,
                "boid": boid
            }
            ipo_results[boid_name[boid]] = requests.post(url=URL, json=data).json()
        print(ipo_results)
        for i in ipo_results:
            print(ipo_results[i]['success'])
            total_count += 1
            if ipo_results[i]['success']:
                alloted_count += 1
            if not ipo_results[i]['success']:
                notalloted_count += 1

        context = {
            'title': 'Results',
            'ipo_results': ipo_results,
            'boid_name': boid_name,
            'total_count': total_count,
            'alloted_count': alloted_count,
            'notalloted_count': notalloted_count,
        }
        return render(request, 'results/results.html', context)
    return HttpResponse("Oops! You cannot perfrom this operation.")


def beneficiaryDetails_view(request, b_id=None):
    context = {}
    if request.POST:
        if b_id is not None:
            b_object = get_object_or_404(BeneficiaryDetails, id=b_id)
            form = BeneficiaryDetailsModelForm(data=request.POST, instance=b_object)
            if form.is_valid():
                form.save()
                return redirect("ipo:beneficiarydetails")

        else:
            form = BeneficiaryDetailsModelForm(request.POST)
            if form.is_valid():
                name = request.POST['name']
                boid = request.POST['boid']
                user_id = request.user.id
                beneficiary = BeneficiaryDetails(name=name, boid=boid, user_id=user_id)
                beneficiary.save()
                return redirect("ipo:beneficiarydetails")
    else:
        if b_id is None:
            form = BeneficiaryDetailsModelForm()
        else:
            b_object = get_object_or_404(BeneficiaryDetails, id=b_id)
            form = BeneficiaryDetailsModelForm(instance=b_object)
            context['b_object'] = b_object
    beneficiaries = BeneficiaryDetails.objects.filter(user_id=request.user.id)
    context['title'] = 'Beneficiary Details'
    context['form'] = form
    context['beneficiaries'] = beneficiaries

    return render(request, 'results/beneficiarydetails.html', context)


def beneficiary_delete_view(request, b_id):
    if request.POST:
        b_object = get_object_or_404(BeneficiaryDetails, id=b_id)
        b_object.delete()
        return redirect("ipo:beneficiarydetails")
    return HttpResponse("Cannot perform delete operation")
