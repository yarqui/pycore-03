from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    try:
        if type(date) is not str:
            raise TypeError('Date should be an integer')
        
        current_date = datetime.today()
        ref_date = datetime.strptime(date, '%Y-%m-%d')
        
        return (current_date - ref_date).days
        
    except Exception as err:
        print(f'{type(err)}: {err}')
    
print(get_days_from_today(bool))
print(get_days_from_today('2027-02-02'))
print(get_days_from_today('2027'))