from src.maintenance.survival import weibull_survival

def test_survival_at_zero():
    assert weibull_survival(0,2,10)==1.0
