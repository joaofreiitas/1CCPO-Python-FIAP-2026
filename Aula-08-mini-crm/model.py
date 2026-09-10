from datetime import date

def model_lead(name, email, company, stage):
    """Estrutra e modela um lead como dicionário"""
    return {
        "name": name,
        "email": email,
        "company": company,
        "stage": stage,
        "created": date.today().isoformat()
    }