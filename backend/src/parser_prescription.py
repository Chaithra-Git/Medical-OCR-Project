from backend.src.parser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines': self.get_field('medicines')

        }

    def get_field(self,field_name):

        pattern_dict={
            'patient_name':{'pattern':'Name:(.*)Date','flags':0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()

    # def get_name(self):
    #     pattern = 'Name:(.*)Date'
    #     matches = re.findall(pattern,self.text)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_address(self):
    #     pattern = 'Address:(.*)\n'
    #     matches = re.findall(pattern, self.text)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_medicines(self):
    #     pattern = 'Address[^\n]*(.*)Directions'
    #     matches = re.findall(pattern, self.text,flags = re.DOTALL)
    #     if len(matches) > 0:
    #         return matches[0].strip()



if __name__=='__main__':
    document_txt ='''
        Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    pp = PrescriptionParser(document_txt)
    print(pp.parse())