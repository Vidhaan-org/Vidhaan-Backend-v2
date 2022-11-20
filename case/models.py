from django.db import models
from django.contrib.auth import get_user_model

import choose

Users = get_user_model()


class Case(models.Model):
    cnr_number = models.CharField(max_length = 200, unique = True)

    case_type = models.CharField(max_length = 50, choices = choose.CASE_TYPE, null = True, blank = True)
    filing_number = models.CharField(max_length=20, null = True, blank = True)
    filing_date = models.DateField(null = True, blank = True)
    registration_number = models.CharField(max_length = 200, null = True, blank = True)
    registration_date = models.DateField(null = True, blank = True)

    first_hearing_date = models.DateField(null = True, blank = True)
    next_hearing_date = models.DateField(null = True, blank = True) # can change by operation 
    stage_of_case = models.CharField(max_length = 50, null = True, blank = True) # can change by operation 
    coram = models.CharField(max_length = 500, null = True, blank = True)
    bench = models.CharField(max_length = 50, null = True, blank = True)
    state = models.CharField(max_length = 50, null = True, blank = True)
    judicial = models.CharField(max_length = 50, null = True, blank = True)
    causelist_name = models.CharField(max_length = 50, null = True, blank = True)

    petitioner = models.ManyToManyField(Users, null = True, blank = True, related_name='case_petitioner')
    respondent = models.ManyToManyField(Users, null = True, blank = True, related_name =  'case_respondent')
    petitioner_advocate = models.ManyToManyField(Users, null = True, blank = True, related_name = 'petitioner_advocate')
    respondent_advocate = models.ManyToManyField(Users, null = True, blank = True, related_name = 'respondent_advocate')
    person_involved = models.ManyToManyField(Users, null = True, blank = True, related_name =  'person_involved')

    under_act = models.CharField(max_length = 500, null = True, blank = True)
    under_section = models.CharField(max_length = 50, null = True, blank = True)

    fir_state = models.CharField(max_length = 50, null = True, blank = True)
    fir_district = models.CharField(max_length = 50, null = True, blank = True)
    fir_police_station = models.CharField(max_length = 50, null = True, blank = True)
    fir_number = models.CharField(max_length = 50, null = True, blank = True)
    fir_year = models.CharField(max_length = 50, null = True, blank = True)

    category = models.CharField(max_length = 150, choices = choose.CASE_CATEGORY, null = True, blank = True)
    sub_category = models.CharField(max_length = 50, null = True, blank = True)

    def petitioners(self):
        return ", ".join([str(p) for p in self.petitioner.all()])

    def respondents(self):
        return ", ".join([str(p) for p in self.respondent.all()])

    def petitioner_advocates(self):
        return ", ".join([str(p) for p in self.petitioner_advocate.all()])

    def respondent_advocates(self):
        return ", ".join([str(p) for p in self.respondent_advocate.all()])
    
    def persons_involved(self):
        return ", ".join([str(p) for p in self.person_involved.all()])
    


class History(models.Model):
    case = models.ForeignKey(Case, null = True,blank = True,related_name='case_history', on_delete = models.CASCADE)
    cause_list_type = models.CharField(max_length = 50, null = True,blank = True)
    judge = models.CharField(max_length = 500, null = True,blank = True)
    business_on_date = models.DateField(null = True, blank = True)
    hearing_date = models.DateField( null = True,blank = True)
    purpose_of_hearing = models.CharField(max_length=50, null = True,blank = True)

    def __str__(self):
        return "%s %s" %(self.cause_list_type, self.purpose_of_hearing)


class Order(models.Model): 
    case = models.ForeignKey(Case, null = True,blank = True,related_name='case_order', on_delete = models.CASCADE)
    judge = models.CharField(max_length = 500, null = True,blank = True)
    order_date = models.DateField(null = True, blank = True)
    order_details = models.FileField(upload_to="order-details/",null = True, blank = True)

    def __str__(self):
        return "%s" %(self.order_date)


class Objection(models.Model):
    case = models.ForeignKey(Case, null = True,blank = True,related_name='case_objection', on_delete = models.CASCADE)
    scrutiny_date = models.DateField(null = True, blank = True)
    objection = models.CharField(max_length = 500, null = True,blank = True)
    compliance_date = models.DateField(null = True, blank = True)
    reciept_date = models.DateField(null = True, blank = True)

    def __str__(self):
        return "%s" %(self.scrutiny_date)


class DocumentDetails(models.Model):
    case = models.ForeignKey(Case, null = True,blank = True,related_name='case_document', on_delete = models.CASCADE)
    date_of_recieving = models.DateField(null = True, blank = True)
    filed_by = models.CharField(max_length = 500, null = True,blank = True)
    advocate = models.ForeignKey(Users,  null = True,blank = True, on_delete = models.CASCADE)
    document = models.FileField(upload_to="document-details/",null = True, blank = True)
    document_type = models.CharField(max_length=50, null = True,blank = True)

    def __str__(self):
        return "%s %s" %(self.advocate, self.document_type)
