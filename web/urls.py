from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.IndexView.as_view(), name="web.index"),
    path("about/", view=views.AboutView.as_view(), name="web.about"),
    path("contact/", view=views.ContactView.as_view(), name="web.contact"),
    path("services/study_abroad", view=views.StudyAbroadView.as_view(), name="web.services.study_abroad"),
    path("services/loans", view=views.LoansView.as_view(), name="web.services.loans"),
    path("services/imp_exp", view=views.ImpExpView.as_view(), name="web.services.imp_exp"),
    path("services/edu", view=views.EducationView.as_view(), name="web.services.education"),
    path("services/consulting", view=views.ConsultingView.as_view(), name="web.services.consulting"),
    path("services/business", view=views.BusinessAnalysisView.as_view(), name="web.services.business"),
    path("services/funds_transfer", view=views.FundsTransferView.as_view(), name="web.services.funds_transfer"),
]