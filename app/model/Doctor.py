from pkgutil import extend_path
from app.model.Person import Person

class Doctor(Person):
    id                      = "";
    crm                     = "";
    clinical_specialization = "";
    ref_people              = "";    
    
    def __init__(self, crm,clinical_specialization, ref_people):
        self.crm = crm;
        self.clinical_specialization = clinical_specialization;
        self.ref_people;
            