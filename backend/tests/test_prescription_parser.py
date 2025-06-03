from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_maria():
    document_txt = '''
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

    return PrescriptionParser(document_txt)

@pytest.fixture()
def doc_2_empty():
    return PrescriptionParser('')


def test_get_name(doc_1_maria,doc_2_empty):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_empty.get_field('patient_name') == None

def test_get_address(doc_1_maria):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'

def test_get_medicines(doc_1_maria):
    assert doc_1_maria.get_field('medicines') == 'K\n\n    Prednisone 20 mg\n    Lialda 2.4 gram'

def test_parse(doc_1_maria,doc_2_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria['patient_name'] =='Marta Sharapova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['medicines'] == 'K\n\n    Prednisone 20 mg\n    Lialda 2.4 gram'

    record_empty = doc_2_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None
    }