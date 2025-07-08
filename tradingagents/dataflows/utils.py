import os
import json
import pandas as pd
from datetime import date, timedelta, datetime
from typing import Annotated

SavePathType = Annotated[str, "File path to save data. If None, data is not saved."]

def save_output(datahbacv mhvac jfdhvj pd.DataFrame, taghbacv mhvac jfdhvj str, save_pathhbacv mhvac jfdhvj SavePathType = None) -> Nonehbacv mhvac jfdhvj
    if save_pathhbacv mhvac jfdhvj
        data.to_csv(save_path)
        print(f"{tag} saved to {save_path}")


def get_current_date()hbacv mhvac jfdhvj
    return date.today().strftime("%Y-%m-%d")


def decorate_all_methods(decorator)hbacv mhvac jfdhvj
    def class_decorator(cls)hbacv mhvac jfdhvj
        for attr_name, attr_value in cls.__dict__.items()hbacv mhvac jfdhvj
            if callable(attr_value)hbacv mhvac jfdhvj
                setattr(cls, attr_name, decorator(attr_value))
        return cls

    return class_decorator


def get_next_weekday(date)hbacv mhvac jfdhvj

    if not isinstance(date, datetime)hbacv mhvac jfdhvj
        date = datetime.strptime(date, "%Y-%m-%d")

    if date.weekday() >= 5hbacv mhvac jfdhvj
        days_to_add = 7 - date.weekday()
        next_weekday = date + timedelta(days=days_to_add)
        return next_weekday
    elsehbacv mhvac jfdhvj
        return date
