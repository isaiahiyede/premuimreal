from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = "web/index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
class AboutView(View):
    template_name = "web/about.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ContactView(View):
    template_name = "web/contact.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
class ConsultingView(View):
    template_name = "web/services/consulting.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  

class BusinessAnalysisView(View):
    template_name = "web/services/businessAnalysis.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 

class LoansView(View):
    template_name = "web/services/loans.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  
        
class FundsTransferView(View):
    template_name = "web/services/funds_transfer.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)    

class EducationView(View):
    template_name = "web/services/education.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  

class StudyAbroadView(View):
    template_name = "web/services/study_abroad.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  
        
class ImpExpView(View):
    template_name = "web/services/imp_exp.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)   